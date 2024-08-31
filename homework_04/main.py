"""
Домашнее задание №4
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

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL, fetch_json
from homework_04.models import async_engine, Session, Base, User, Post


async def create_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, users: dict):
    users = [User(name=user["name"], username=user["username"], email=user["email"]) for user in users]
    session.add_all(users)
    await session.commit()


async def create_posts(session: AsyncSession, posts: dict):
    posts = [Post(title=post["title"], body=post["body"], user_id=post["userId"]) for post in posts]
    session.add_all(posts)
    await session.commit()


async def async_main() -> None:
    await create_tables()
    async with asyncio.TaskGroup() as tg:
        all_users = tg.create_task(fetch_json(USERS_DATA_URL))
        all_posts = tg.create_task(fetch_json(POSTS_DATA_URL))
    async with Session() as session:
        await create_users(session, all_users.result())
        await create_posts(session, all_posts.result())


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
