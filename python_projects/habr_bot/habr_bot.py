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
from datetime import datetime
import h_url

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
invite = ##########

button_help = KeyboardButton('/help')
button_categories = KeyboardButton('/categories')

def soup(url):
    soup = BeautifulSoup(url, features="lxml")
    for link in soup.find_all('a', href=True):
        if '/blog/' in link['href'] or '/post/' in link['href']:
            if not link['href'].endswith('blog/') and not link['href'].endswith('comments/'):
                res = "https://habr.com" + link['href']
                return res

def log(line):
    log = open('log.txt', 'a')
    log.write(line)
    log.close()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    chat_id = message.chat.id
    name = message.chat.first_name
    print(chat_id)
    if chat_id != invite:
        await message.reply("Where your invite code?")
        log("Неудачная попытка запуска бота юзером " + name + " | Время: " + str(datetime.now()) + '\n')
    else:
        await message.reply("Бот для чтения статей с habr.com\n/help - для помощи.", reply_markup=markup)
        log("Удачный запуск бота, открыта клавиатура юзером " + name + " | Время: " + str(datetime.now()) + '\n')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    chat_id = message.chat.id
    name = message.chat.first_name
    if chat_id != invite:
        await message.reply("Where your invite code?")
        log("Неудачная попытка обратиться к помощи юзером " + name + " | Время: " + str(datetime.now()) + '\n')
    else:
        await message.reply("Бот для чтения статей с habr.com.\nПо запросу из категорий будет показана популярная за день\неделю\месяц статья.\n\n┌\help──────────────────⊸\n│\n├  Бот отвечает на команды:\n│       ├ /start - запуск, перезапуск бота\n│       ├ /help - вывод этого сообщения\n│       ├ /categories - просмотр категорий")
        log("Удачное обращение к помощи юзером " + name + " | Время: " + str(datetime.now()) + '\n')

markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button_help).add(button_categories)

b_infosec = InlineKeyboardButton('Информационная безопасность',       callback_data='InfoSec')
b_dev = InlineKeyboardButton('Программирование',                      callback_data='Dev')
b_popscien = InlineKeyboardButton('Научно-популярное',                callback_data='PopScien')
b_diy = InlineKeyboardButton('DIY',                                   callback_data='DIY')
b_gadgets = InlineKeyboardButton('Гаджеты',                           callback_data='Gadgets')
b_devmic = InlineKeyboardButton('Программирование микроконтроллеров', callback_data='DevMic')
b_servadm = InlineKeyboardButton('Серверное администрирование',       callback_data='ServAdm')
b_devops = InlineKeyboardButton('DevOps',                             callback_data='DevOps')
b_net = InlineKeyboardButton('Сетевые технологии',                    callback_data='Network')
b_nix = InlineKeyboardButton('*nix',                                  callback_data='Nix')
b_robotics = InlineKeyboardButton('Робототехника',                    callback_data='Robot')
b_sysdev = InlineKeyboardButton('Системное программирование',         callback_data='SysDev')

inline_kb_full = InlineKeyboardMarkup(row_width=1).add(b_devmic, b_infosec, b_servadm, b_sysdev)
inline_kb_full.add(b_net, b_robotics)
inline_kb_full.row(b_dev, b_popscien)
inline_kb_full.row(b_gadgets, b_devops)
inline_kb_full.row(b_diy, b_nix)

@dp.message_handler(commands=['categories'])
async def process_categories_command(message: types.Message):
    chat_id = message.chat.id
    name = message.chat.first_name
    if chat_id != invite:
        await message.reply("Where your invite code?")
        log("Неудачная попытка открыть категории юзером " + name + " | Время: " + str(datetime.now()) + '\n')
    else:
        await message.reply("Доступные хабы:", reply_markup=inline_kb_full)
        log("Открыты кнопки с хабами юзером " + name + " | Время: " + str(datetime.now()) + '\n')


@dp.callback_query_handler(lambda c: c.data == 'InfoSec')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_infosec)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по InfoSec" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)
        
@dp.callback_query_handler(lambda c: c.data == 'Dev')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_dev)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по Dev" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'PopScien')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_popscien)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по PopScien" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'DIY')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_diy)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по DIY" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'Gadgets')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_gadgets)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по Gadgets" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'DevMic')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_devmic)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по DevMic" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'ServAdm')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_servadm)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по ServAdm" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'DevOps')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_devops)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по DevOps" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'Network')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_network)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по Network" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'Nix')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_nix)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по Nix" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'Robot')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_robot)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по Robot" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == 'SysDev')
async def process_callback_button(callback_query: types.CallbackQuery):
    url = urllib.request.urlopen(h_url.url_sysdev)
    res = soup(url)
    await bot.send_message(callback_query.from_user.id, res)
    log("Выдана статья по SysDev" + " | Время: " + str(datetime.now()) + '\n')
    await bot.answer_callback_query(callback_query.id)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Hmmm...')

if __name__ == '__main__':
    executor.start_polling(dp)
