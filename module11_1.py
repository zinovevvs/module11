"""
import requests

image_url = 'https://www.pngegg.com/ru/png-xbsrv'
response = requests.get(image_url)

if response.status_code == 200:
    with open('downloaded_image.png', 'wb') as file:
        file.write(response.content)
    print("Изображение успешно загружено и сохранено как downloaded_image.png")
else:
    print(f"Ошибка при загрузке изображения: {response.status_code}")
"""

"""
import pandas as pd

df = pd.read_csv('/Users/zinovevvs/Desktop/Книга1.csv')
print(df.head())


mean_value = df['value'].mean()
print(f"Среднее значение: {mean_value}")

grouped = df.groupby('category')['value'].sum()
print(grouped)
"""

"""
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]


plt.bar(categories, values)


plt.title('Пример барного графика')
plt.xlabel('Категории')
plt.ylabel('Значения')


plt.show()
"""
1)Библиотека requests позволяет взаимодействовать с API информационных систем не только с веб-сервисами, позволяет отслеживать состояние веб-сервиса.
2)pandas возволяет работать с широким с спиком дата-сетов и структурировать под удобный вид периентирую данные в файле и адаптируя их для дальнейшего анализа
3)matplotlib позволяет создавать двумерные и трехмерные диаграмма, есть возможность анимировать изображения. Библиотека является некоторым аналогом программы для моделирования технических вычислений. 


