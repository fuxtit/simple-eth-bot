from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.interfaces.database_adapter import AbstractDbAdapter
from src.infrastructure.database.models import UserModel


class DbAdapter(AbstractDbAdapter):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        return await self.session.commit()

    async def add_user(self, tg_id: int, username: str, chat_id: int):
        return await self.session.execute(
            insert(UserModel).values(
                tg_id=tg_id, username=username, chat_id=chat_id
            )
        )

    async def get_by_tg_id(self, tg_id: int):
        return await self.session.get(UserModel, tg_id)
