from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Row, Button, Group

from src.presentation.telegram.states import MainSG
from src.presentation.telegram.dialogs.widgets.i18n import I18NFormat

from src.infrastructure.services.eth import EthService


async def eth_price_getter(
        dialog_manager: DialogManager,
        eth_service: EthService,
        **_: Any,
):
    if dialog_manager.event.from_user:
        price = await eth_service.get_eth_price()
        return {'price': price}


async def to_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MainSG.main_menu)


async def to_price(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MainSG.check_eth_price)


async def to_alerts(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MainSG.alerts)


async def to_settings(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=MainSG.settings)


async def back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back()


main_dialog = Dialog(
    Window(
        I18NFormat('start-menu'),
        Row(
            Button(
                text=I18NFormat('price-btn'),
                id='price_btn',
                on_click=to_price,
            ),
            Button(
                text=I18NFormat('alert-btn'),
                id='alert_btn',
                on_click=to_alerts
            ),
            Button(
                text=I18NFormat('settings-btn'),
                id='settings_btn',
                on_click=to_settings
            ),
        ),
        state=MainSG.main_menu,
    ),
    Window(
        I18NFormat('price-info'),
        Button(
            text=I18NFormat('update-price'),
            id='update_price',
            on_click=to_price,
        ),
        Button(
            text=I18NFormat('back'),
            id='back',
            on_click=back
        ),
        state=MainSG.check_eth_price,
        getter=eth_price_getter
    ),

    Window(
        I18NFormat('alerts-menu'),
        Button(
            text=I18NFormat('back'),
            id='back',
            on_click=to_menu
        ),

        state=MainSG.alerts
    ),

    Window(
        I18NFormat('settings-menu'),
        Group(
            Button(
                text=I18NFormat('en-btn'),
                id='en'
            ),
            Button(
                text=I18NFormat('ru-btn'),
                id='ru'
            ),
            Button(
                text=I18NFormat('back'),
                id='back',
                on_click=to_menu
            ),
            width=2
        ),

        state=MainSG.settings
    )

)
