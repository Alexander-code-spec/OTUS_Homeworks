import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, User
from views.forms.users import ProductForm

users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def list_user():
    # Достаем пользователей из БД
    users = User.query.order_by(User.id).all()

    # Рендерим шаблон со списком
    return render_template(
        "users/list.html",
        users=users,
    )


def save_product(user_name):
    # Пробуем сделать комит в БД, обрабатывая возможные ошибки
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save user {user_name}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save product with name {user_name}!")


@users_app.route("/<int:user_id>/", methods=["GET", "POST"], endpoint="details")
def get_product_by_id(user_id: int):
    # подтягиваем пользователя из БД
    user = User.query.get(user_id)

    # Если нет пользователя, то выдать исключение
    if user is None:
        raise NotFound(f"User with id #{user_id} not found!")

    # Создадим экземпляр формы для заполнения
    form = ProductForm()

    # Если тип запроса "GET", то отрендерим details с запрашиваемым пользователем
    if request.method == "GET":
        return render_template(
            "users/details.html",
            user=user,
            form=form,
        )

    # Если POST запрос, то вытащим пользовательские данные для обновления с формы, проверив на повторы
    user_name = form.data["name"]

    if user.name == user_name:
        raise BadRequest(f"this user is already named {user_name}")
    if User.query.filter_by(name=user_name).count():
        raise BadRequest(f"user with name {user_name!r} already exists!")

    # Заполним поля для БД
    user.name = user_name
    user.is_new = form.data["is_new"]

    # Делаем комит в БД
    save_product(user_name)

    # Обновляем шаблон
    return redirect(url_for("users_app.details", user_id=user.id))


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    # Создаем экземпляр формы для ввода данных по пользователям
    form = ProductForm()

    # Если запрос "GET", то отрендерим
    if request.method == "GET":
        return render_template("users/add.html", form=form)

    # Валидируем форму
    if not form.validate_on_submit():
        return render_template("users/add.html", form=form)

    user = User(name=form.data["name"], email=form.data["email"], is_new=form.data["is_new"])

    db.session.add(user)

    save_product(user.name)

    return redirect(url_for("users_app.details", user_id=user.id))
