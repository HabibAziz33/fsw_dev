from aiogram import Bot, Dispatcher, executor
import os
from dotenv import load_dotenv
from aiogram.types import Message, CallbackQuery, LabeledPrice
load_dotenv()
from work import *
from keyboards import *

bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message : Message):
    await message.reply('Здравствуйте что-бы пользоваться ботом пожалуйста отправьте номер!')
async def num(message : Message):
    await message.reply('''
    Здравствуйте это бот команды ⬛FSW Developers!\n
В данном боте вы можете приобрести наши услуги и товары!
    
В наличии у нас есть:
<b>🚀 Создание ботов.</b> Ваш бот будет принимать больше заказов и прибыль так же увеличиться! \n
<b>🖥 Парсинг.</b> Вы можете получить информацию с сайта! \n
<b>💻 Создание сайтов(Бэк-энд).</b> Скоро.... \n
''')


































@dp.message_handler(commands='admin', user_id=['631357872','710258253'])
async def admin(message: Message):
    await message.reply('''
    Приветствую Админ!
    Ввыбери действий!
    ''')
executor.start_polling(dp)





