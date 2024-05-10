from abc import ABC, abstractmethod


class AbstractEthClient(ABC):

    @abstractmethod
    async def get_eth_price(self) -> float:
        raise NotImplementedError
