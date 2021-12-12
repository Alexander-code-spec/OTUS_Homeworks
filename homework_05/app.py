"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, Blueprint, render_template

app = Flask(__name__)
my_app = Blueprint("my_app", __name__)

app.register_blueprint(my_app, url_prefix="/about/")


@app.route("/", endpoint="home")
def root():
    return render_template(
        "base.html",
    )


@app.route("/about/", endpoint="about")
def get_about():
    return render_template(
        "base.html",
    )

if __name__ == "__main__":
    app.run(debug=True)
