from abc import ABC, abstractmethod


class AbstractDbAdapter(ABC):

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def add_user(self, tg_id: int, username: str, chat_id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_by_tg_id(self, tg_id: int):
        raise NotImplementedError
