from aiogram import Bot, Dispatcher, executor
from keyboard import Keyboard
from Parser import Parser
import logging

TOKEN = '1326804226:AAEzbUO8vc3QFYTO9YAJpYQl3RcYeHf1kuk'

CATEGORIES = {
    'Free games': 'https://store.steampowered.com/genre/Free%20to%20Play/',
    'Indie games': 'https://store.steampowered.com/tags/ru/%D0%98%D0%BD%D0%B4%D0%B8/',
    'Racing games': 'https://store.steampowered.com/tags/ru/%D0%93%D0%BE%D0%BD%D0%BA%D0%B8/'
}
logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)
keyboard = Keyboard()
parser = Parser()


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Welcome', reply_markup=keyboard.main())


@dp.message_handler(content_types=['text'])
async def msg(message):
    text = message.text
    msg1 = 'Извините, я вас не понимаю'
    msg2 = ''

    if text in CATEGORIES:
        url = CATEGORIES[text]
        msg = parser.parse(url)
        msg1 = msg[0:len(msg) // 2]
        msg2 = msg[len(msg) // 2: len(msg)]
    await bot.send_message(message.chat.id, msg1, reply_markup=keyboard.main())
    if msg2: await bot.send_message(message.chat.id, msg2, reply_markup=keyboard.main())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
