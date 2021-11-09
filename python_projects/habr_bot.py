from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp.client import request
from config import TOKEN
from random import randint
import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
invite = #NEED YOUR CHAT_ID

button_help = KeyboardButton('/help')
button_categories = KeyboardButton('/categories')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    chat_id = message.chat.id
    name = message.chat.first_name
    print(chat_id)
    if chat_id != invite:
        await message.reply("Where your invite code?")
        print("Неудачная попытка запуска бота юзером", name)
    else:
        await message.reply("Бот для чтения статей с habr.com\n/help - для помощи.", reply_markup=markup)
        print("Удачный запуск бота, открыта клавиатура юзером", name)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    chat_id = message.chat.id
    name = message.chat.first_name
    if chat_id != invite:
        await message.reply("Where your invite code?")
        print("Неудачная попытка обратиться к помощи юзером", name)
    else:
        await message.reply("Бот для чтения статей с habr.com.\nПо запросу из категорий будет показана популярная за день\неделю статья.\n\n┌\help──────────────────⊸\n│\n├  Бот отвечает на команды:\n│       ├ /start - запуск, перезапуск бота\n│       ├ /help - вывод этого сообщения\n│       ├ /categories - просмотр категорий")
        print("Удачное обращение к помощи юзером", name)

markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_categories)

inline_button_categories_infosec = InlineKeyboardButton('Информационная безопасность',       callback_data='InfoSec')
inline_button_categories_dev = InlineKeyboardButton('Программирование',                      callback_data='Dev')
inline_button_categories_popscien = InlineKeyboardButton('Научно-популярное',                callback_data='PopScien')
inline_button_categories_diy = InlineKeyboardButton('DIY',                                   callback_data='DIY')
inline_button_categories_gadgets = InlineKeyboardButton('Гаджеты',                           callback_data='Gadgets')
inline_button_categories_devmic = InlineKeyboardButton('Программирование микроконтроллеров', callback_data='DevMic')
inline_button_categories_servadm = InlineKeyboardButton('Серверное администрирование',       callback_data='ServAdm')
inline_button_categories_devops = InlineKeyboardButton('DevOps',                             callback_data='DevOps')
inline_button_categories_net = InlineKeyboardButton('Сетевые технологии',                    callback_data='Network')
inline_button_categories_nix = InlineKeyboardButton('*nix',                                  callback_data='Nix')
inline_button_categories_robotics = InlineKeyboardButton('Робототехника',                    callback_data='Robot')
inline_button_categories_sysdev = InlineKeyboardButton('Системное программирование',         callback_data='SysDev')


inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_button_categories_devmic, inline_button_categories_infosec, inline_button_categories_servadm, inline_button_categories_sysdev)
inline_kb_full.add(inline_button_categories_net, inline_button_categories_robotics)
inline_kb_full.row(inline_button_categories_dev, inline_button_categories_popscien)
inline_kb_full.row(inline_button_categories_gadgets, inline_button_categories_devops)
inline_kb_full.row(inline_button_categories_diy, inline_button_categories_nix)

@dp.message_handler(commands=['categories'])
async def process_categories_command(message: types.Message):
    chat_id = message.chat.id
    if chat_id != invite:
        await message.reply("Where your invite code?")
        print("Неудачная попытка открыть категории")
    else:
        await message.reply("Доступные хабы:", reply_markup=inline_kb_full)
        print("Открыты кнопки с хабами")


@dp.callback_query_handler(lambda c: c.data == 'InfoSec')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/infosecurity/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба Информационная безопасность:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по InfoSec")
        
@dp.callback_query_handler(lambda c: c.data == 'Dev')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/programming/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба Программирование:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по Dev")

@dp.callback_query_handler(lambda c: c.data == 'PopScien')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/popular_science/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба Научно-популярное:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по PopScien")

@dp.callback_query_handler(lambda c: c.data == 'DIY')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/DIY/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба DIY:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по DIY")

@dp.callback_query_handler(lambda c: c.data == 'Gadgets')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/gadgets/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба Гаджеты:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по Gadgets")

@dp.callback_query_handler(lambda c: c.data == 'DevMic')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/controllers/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба Программирование микроконтроллеров:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по DevMic")

@dp.callback_query_handler(lambda c: c.data == 'ServAdm')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/s_admin/top/daily/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за сутки из хаба Серверное администрирование:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по ServAdm")

@dp.callback_query_handler(lambda c: c.data == 'DevOps')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/devops/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба DevOps:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по DevOps")

@dp.callback_query_handler(lambda c: c.data == 'Network')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/network_technologies/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба Сетевые технологии:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по Network")

@dp.callback_query_handler(lambda c: c.data == 'Nix')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/linux_dev/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба *nix:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по Nix")

@dp.callback_query_handler(lambda c: c.data == 'Robot')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/robot/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба Робототехника:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по Robot")

@dp.callback_query_handler(lambda c: c.data == 'SysDev')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    url = urllib.request.urlopen("https://habr.com/ru/hub/system_programming/top/weekly/")
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
    await bot.send_message(callback_query.from_user.id, 'Топ статья за неделю из хаба Системное программирование:')
    await bot.send_message(callback_query.from_user.id, res)
    print("Выдана статья по SysDev")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Hmmm...')

if __name__ == '__main__':
    executor.start_polling(dp)
