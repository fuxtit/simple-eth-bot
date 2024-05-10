from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message, User
from fluentogram import TranslatorHub


class I18nMiddleware(BaseMiddleware):
    def __init__(
            self,
            hub: TranslatorHub,
    ):
        super().__init__()
        self.hub = hub

    async def __call__(
            self,
            handler: Callable[
                [Union[Message, CallbackQuery], Dict[str, Any]],
                Awaitable[Any],
            ],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        lang = user.language_code
        data['i18n'] = self.hub.get_translator_by_locale(lang)

        return await handler(event, data)
