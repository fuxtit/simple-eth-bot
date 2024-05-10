from aiogram.fsm.state import State, StatesGroup


class MainSG(StatesGroup):
    main_menu = State()
    check_eth_price = State()
    settings = State()
    alerts = State()


class AlertSG(StatesGroup):
    create_alert = State()
