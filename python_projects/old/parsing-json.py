# coding=utf-8
from datetime import datetime
from io import open
import requests
import json
import os

API_TODOS = 'https://jsonplaceholder.typicode.com/todos'
API_USERS = 'https://jsonplaceholder.typicode.com/users'

FOLDER_NAME = 'tasks'

MAX_TITLE_LENGTH = 50

FOLDER_DATEFORMAT = '%Y-%m-%dT%H:%M'
FILE_DATEFORMAT = '%d.%m.%Y %H:%M'

script_folder = os.path.dirname(os.path.realpath(__file__))


def fetch_json_from(url):
    return requests.get(url).json()


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def get_date(format):
    return datetime.now().strftime(format)


def truncate_with_dots(str, length):
    return (str[:length - 3] + '...') if len(str) > length - 3 else str


users = fetch_json_from(API_USERS)
todos = fetch_json_from(API_TODOS)
create_folder(FOLDER_NAME)


for user in users:
    id = user['id']
    name = user['name']
    email = user['email']
    username = user['username']
    company = user['company']['name']
    date = get_date(FILE_DATEFORMAT)
    date_existfile = get_date(FOLDER_DATEFORMAT)                              # формат даты\времени для переименования существующих отчетов
    filename = os.path.join(script_folder, FOLDER_NAME, username) + '.txt'
    renamed_filename = os.path.join(script_folder, FOLDER_NAME, username)     # то же что и filename, но без .txt (выходной файл получался "Antonette.txt_2019-09-06T17:22.txt")

    completedTasks = ''
    uncompletedTasks = ''

    content = name + ' <' + email + '> ' + date + '\n'
    content += company + '\n\n'
    content += 'Завершенные задачи:\n'

    for todo in todos:
        user_id = todo['userId']
        completed = todo['completed']
        title = truncate_with_dots(todo['title'], MAX_TITLE_LENGTH)   # обрезаем строку до 50 символов

        if user_id == id and completed:          # сравнивание id в user и todos для Выполненых задач
            completedTasks += title + '\n'      # и запись в троку при выполненном условии

        if user_id == id and not completed:      # сравнивание id в user и todos для Оставшихся задач
            uncompletedTasks += title + '\n'    # и запись в троку при выполненном условии

    content += completedTasks
    content += '\nОставшиеся задачи:\n'
    content += uncompletedTasks


    try:
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as file:         # запись новых файлов, которых еще нет в папке
                file.write(content)
        else:
            try:
                os.rename(filename, renamed_filename + '_' + date_existfile + '.txt')   # переименование существующих файлов
            except:
                print('Error: Rename error.')
            with open(filename, 'w', encoding='utf-8') as file:         # и запись актуального отчета
                file.write(content)
    except OSError:
        print('Error: Failed to record.')
