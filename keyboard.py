from aiogram import types


class Keyboard:
    def __init__(self):
        pass

    def main(self):
        keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        free_games = types.KeyboardButton(text='Free games')
        indie_games = types.KeyboardButton(text='Indie games')
        racing_games = types.KeyboardButton(text='Racing games')
        keyboard_main.add(free_games, indie_games, racing_games)
        return keyboard_main
