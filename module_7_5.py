import os
import time
from os.path import dirname


# os.makedirs=('directory/directory_2')
# print(os.getcwd())
# os.chdir('directory')
# print(os.getcwd())
# os.chdir('directory_2')
# print(os.getcwd())

# for dirpath, dirnames, filenames in os.walk('.'):
#     for dirname in dirnames:
#         print('Dir:', os.path.join(dirpath, dirname))
#     for filename in filenames:
#         print('File:', os.path.join(dirpath, filename))

def info(directory):
    for root, dirs, files in os.walk(directory):
      for file in files:
          filepath = os.path.join(root, file)
          filename = file
          filetime = os.path.getatime(filepath)
          formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
          filesize = os.path.getsize(filepath)
          parent_dir = os.path.dirname(filepath)
          print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
                f' Родительская директория: {parent_dir}')
info('.')

