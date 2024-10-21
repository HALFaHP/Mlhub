from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Upload'),
        KeyboardButton(text='Select')
    ],
    [
        KeyboardButton(text='Use')
    ]
],
    resize_keyboard=False,
    input_field_placeholder='Create with it')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='First model(linear regression)', url='https://youtube.com')
    ]
])