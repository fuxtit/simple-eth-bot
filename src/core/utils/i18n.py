from fluent_compiler.bundle import FluentBundle

from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {
            'en': ('en', 'ru'),
            'ru': ('ru', 'en')
        },
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale='ru-RU',
                    filenames=['..\..\..\locales\\ru\messages.ftl', '..\..\..\locales\\ru\\buttons.ftl'])),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en-US',
                    filenames=['..\..\..\locales\en\messages.ftl', '..\..\..\locales\\en\\buttons.ftl']))
        ],
    )
    return translator_hub
