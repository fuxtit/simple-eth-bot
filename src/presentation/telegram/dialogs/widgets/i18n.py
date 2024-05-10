from typing import Any, Dict

from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text
from fluentogram import TranslatorRunner


class I18NFormat(Text):
    def __init__(self, text: str, when: WhenCondition = None):
        super().__init__(when=when)
        self.text = text

    async def _render_text(
            self,
            data: Dict[str, Any],
            manager: DialogManager
    ) -> str:
        i18n: TranslatorRunner = manager.middleware_data.get('i18n')

        if i18n is None:
            raise ValueError('There is no "i18n" argument in middlewares')

        if data:
            return i18n.get(self.text, **data)
        return i18n.get(self.text)
