from cProfile import label

from requests import get
import requests
from requests_oauthlib import OAuth2Session

# Requests библиотека

class Custom_bag(Exception):
    pass

params = {"ll": "30.325061,59.934541",
          "lang": 'ru_RU',
          "pt": "30.310311,59.934541,pm2rdm",
          "z": 14,
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/?", params=params)
    if response.status_code == 400:
        raise Custom_bag("Ошибка 400: Плохой запрос. Проверьте параметры.")
except ConnectionError:
        print("Проверьте подключение к сети.")
else:
    with open("map_new.png", "wb") as file:
        file.write(response.content)




resp = requests.get('http://api.github.com')
print(resp.json())

print(resp.headers['Date'])

# client_id = "ca8d08504efa4a81a02174759e05c409"
# client_secret = "ac072c325feb40829128d1461d00455a"
# auth_url = "https://oauth.yandex.ru/authorize"
# token_url = "https://oauth.yandex.ru/token"
# oauth = OAuth2Session(client_id=client_id)
# authorization_url, state = oauth.authorization_url(
#     auth_url,
#     access_type="offline",  # Запрашиваем токен обновления, если это нужно
#     prompt="consent",  # Опционально, чтобы всегда запрашивать согласие
# )
# print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
# code = input("Вставьте одноразовый код(111): ")
# token = oauth.fetch_token(token_url=token_url,
#                           code=code,
#                           client_secret=client_secret)
# access_token = token["access_token"]
# print(access_token)
#
# headers = {"Authorization": f"OAuth {access_token}"}
# r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
# print(r.json())

#-----------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd

# Библиотека Pandas

# Pandas — это библиотека Python, которая используется для манипуляции и анализа данных.
# Основные её компоненты:

#Series — одномерный массив, который может хранить значения любого типа данных;
#DataFrame — двумерный массив (таблица), в котором столбцами являются объекты класса Series

# s = pd.Series(data, index=index) - преобразование в массив

# Чтение данных из CSV файла с указанием разделителя
data = pd.read_csv('csv.csv', delimiter=';')

# Проверка имен столбцов
print(data.columns)

# Удаление пробелов из имен столбцов, если они есть
data.columns = data.columns.str.strip()

# Вывод первых 5 строк данных
print(data.head())

# Расчет дохода
data['revenue'] = data['Quantity'] * data['Price']
print(data)

# Фильтрация: товары с доходом больше 5
high_revenue = data[data['revenue'] > 5]
print(high_revenue)

#-----------------------------------------------------------------------------------------------

# Библиотека NumPy

#NumPy — это библиотека для научных вычислений в Python. Она обеспечивает поддержку многомерных массивов и матриц,
# а также предлагает разнообразные математические функции для их обработки

# Создание одномерного массива
a = np.array([1, 2, 3, 4, 5])

# Векторизация: умножение на 2
a_multi = a * 2
print(a_multi)

# Создание двумерного массива (матрицы)
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Транспонирование матрицы
b_transposed = b.transpose() #b.T
print(b_transposed)

# Вычисление среднего значения всех элементов массива
mean_values = np.mean(b)
print(mean_values)
# Вычисление среднего значения по каждой строке
mean_values = np.mean(b, axis=0)
print(mean_values)
# Вычисление среднего значения по столбцам
mean_values = np.mean(b, axis=1)
print(mean_values)

#-----------------------------------------------------------------------------------------

#Объединение pandas и NumPy

a = np.array([1, 2, 3, 4, 5])
s = pd.Series(a, index=["a", "b", "c", "d", "e"])
print(s)
#np.linspace(0, 1, 5) - это функция из библиотеки NumPy,
# которая генерирует 5 чисел (включая 0 и 1),
# равномерно распределенных между 0 и 1
s = pd.Series(np.linspace(0, 1, 5))
print(s)

d = {"a": 10, "b": 20, "c": 30, "g": 40}
# в качестве index будут ключи
print(pd.Series(d))
print()
print(pd.Series(d, index=["a", "b", "c", "d"]))

a = np.array([1, 2, 3, 4, 5])
s = pd.Series(a, index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s['a'])
print("Выбор нескольких элементов")
print(s[['a', 'b']])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)
print("Фильтрация")
print(s[s > 2])

s.name = "Данные"
s.index.name = "Индекс"
print(s)

students_marks = {"student": ['Александр', 'Дарья', 'Яна'], "math": [3, 5, 4], "physics": [5, 4, 5]}
# Объект класса DataFrame работает с двумерными табличными данными.
# Создать DataFrame проще всего из словаря Python
students = pd.DataFrame(students_marks)
print(students)
#У объекта класса DataFrame есть индексы по строкам (index) и столбцам (columns)
print(students.index)
print(students.columns)

# Задаем значения index
students.index = ['1', '2', '3']
print(students)

bikes_prices = pd.read_csv('Bike_Prices.csv')
# Для получения первых n строк дата-сета используется метод head(n).
# По умолчанию возвращается пять первых строк:
print(bikes_prices.head(3))
# Для получения последних n строк используется метод tail(n)
print(bikes_prices.tail(3))
#Для получения части дата-сета можно использовать срез
print(bikes_prices[10:13])
# Вывод данных KM_Driven 5 позиций бренда Honda
print(bikes_prices[bikes_prices['Brand'] == 'Honda']['KM_Driven'].head())

#-------------------------------------------------------------------------------------------------

# Библиотека Matplotlib

# Matplotlib — популярная Python-библиотека для визуализации данных.
# Она используется для создания любых видов графиков: линейных, круговых диаграмм, построчных гистограмм и других.
# Pyplot — это модуль в пакете Matplotlib, который помогает автоматически создавать оси, фигуры и другие компоненты

import matplotlib.pyplot as plt

# строим график
x = [1, 2, 3, 4, 5]
y = [20, 30, 15, 40, 25]
# plt.plot() — стандартная функция, которая строит график в соответствии со значениями, которые ей были переданы
plt.plot(x, y, color='red', marker='o', markersize= 5, linewidth=2, linestyle='dashed')
plt.xlabel('Ось Х')
plt.ylabel('Ось У')
plt.title('Первый график')
# plt.show() — функция, которая отвечает за вывод визуализированных данных на экран
plt.show()

# Диаграмма рассеяния, или scatterplot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 25, 34, 20, 10, 40, 21, 33, 19, 28]

plt.scatter(x, y)
plt.show()

# Столбчатая диаграмма bar
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
# alpha= может принимать значения от 0 до 1, где 0 — полная прозрачность, а 1 — отсутствие прозрачности
plt.bar(x, y, label='Доход', alpha=0.5)
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.xlabel('Месяц года')
plt.ylabel('Доход, в млн руб.')
plt.legend()
plt.show()

#Круговая диаграмма pie
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
# autopct показывает значение в процентах
plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()

#-----------------------------------------------------------------------------------------

#Библиотека Pillow
from PIL import Image

image = Image.open('pillow.jpg.jpg')
cropped_img = image.crop((300, 150, 700, 1000))
cropped_img.size

# image.show()
cropped_img.show()
low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
low_res_img.show()



