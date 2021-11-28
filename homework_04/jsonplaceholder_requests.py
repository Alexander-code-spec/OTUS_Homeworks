"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    """
    Запрос данных в формате json
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_users_data():
    """
    Запрос данных пользователей
    """
    async with ClientSession() as session:
        json_data = await fetch_json(session, USERS_DATA_URL)
    return json_data


async def fetch_post_data():
    """
    Запрос постов пользователей
    """
    async with ClientSession() as session:
       json_data = await fetch_json(session, POSTS_DATA_URL)
    return json_data
