import asyncio
import logging

from aiohttp import ClientSession

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ChatType, ParseMode
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from fluentogram import TranslatorHub

from src.core.config import settings
from src.core.utils.i18n import create_translator_hub

from src.infrastructure.services.eth import EthService

from src.presentation.telegram.states import MainSG
from src.presentation.telegram.middlewares.i18n import I18nMiddleware
from src.presentation.telegram.dialogs.main_menu import main_dialog

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    if message.from_user:
        await dialog_manager.start(state=MainSG.main_menu, mode=StartMode.RESET_STACK)


async def main() -> None:
    session: ClientSession = ClientSession()

    bot: Bot = Bot(settings['bot.token'], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp: Dispatcher = Dispatcher()

    translator_hub: TranslatorHub = create_translator_hub()

    dp['eth_service'] = EthService(session, settings['etherscan_token'])

    dp.message.register(cmd_start, CommandStart())
    dp.message.filter(F.chat.type == ChatType.PRIVATE)

    for middleware in [
        I18nMiddleware(translator_hub),
    ]:
        dp.message.middleware(middleware)
        dp.callback_query.middleware(middleware)

    dp.include_routers(main_dialog)
    setup_dialogs(dp)

    logger.info('Bot comes to life')

    try:
        await dp.start_polling(bot)
    finally:
        await session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.warning('Bot killed')
