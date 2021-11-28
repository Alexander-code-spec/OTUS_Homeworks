"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from models import User, Session, engine, Base, Post
from jsonplaceholder_requests import fetch_post_data, fetch_users_data


async def create_tables():
    """
    Дропаем, а затем создаем таблицы по моделям
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(user_data: List[dict]):
    """
    Создаем массив пользовталей по моедели и записываем в БД
    """
    users = [
        User(name=data["name"], username=data["username"], email=data["email"])
        for data in user_data
    ]

    async with Session() as session:
        async with session.begin():
            session.add_all(users)


async def create_post(posts_data: List[dict]):
    """
    Создаем массив постов пользователей и загружаем в БД
    """
    posts = [
        Post(title=data["title"], body=data["body"], user_id=data["userId"])
        for data in posts_data
    ]

    async with Session() as session:
        async with session.begin():
            session.add_all(posts)


async def async_main():
    """
    Функция диспетчер
    """
    # Переменные для загрузки данных
    users_data: List[dict]
    posts_data: List[dict]

    # Создаем таблицы по моделям
    await create_tables()

    # Подтягиваем данные для загрузки в БД
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_post_data(),
    )

    # Вносим записи по пользователям
    await create_user(users_data)

    # Вносим данные по постам
    await create_post(posts_data)


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
