from aiogram.utils.keyboard import InlineKeyboardBuilder

def config_gif():
    builder = InlineKeyboardBuilder()
    builder.raw(
        builder.button('Создать'),
    )