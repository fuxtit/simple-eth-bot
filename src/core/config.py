from dynaconf import Dynaconf

from aiogram.utils.token import validate_token
from dynaconf import Validator

validators = [
    Validator(
        names='bot.token', condition=validate_token, must_exist=True
    ),
    Validator(
        names='etherscan_token', is_type_of=str, must_exist=True
    )
]

settings = Dynaconf(
    settings_files=[
        'config//settings.toml'
    ],
    validators=validators,
)