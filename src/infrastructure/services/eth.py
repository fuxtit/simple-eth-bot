import json

from aiohttp import ClientSession

from src.core.interfaces.eth import AbstractEthClient


class EthService(AbstractEthClient):
    def __init__(self, session: ClientSession, api_token: str):
        self.session = session
        self.api_token = api_token

    async def get_eth_price(self) -> float:
        async with self.session.get(
                f'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={self.api_token}'
        ) as response:
            data = await response.text()
            eth_price_data = json.loads(data)
            return eth_price_data['result']['ethusd'][:7]
