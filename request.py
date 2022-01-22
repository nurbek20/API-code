import requests, json
from typing import Text
from requests.models import Response
# url = "https://oc.kg/"
# res = requests.get(url)
# print(res)   # код статуса 
# print(res.status_code) # 
# print(res.content)
# print(res.headers)
# print("Статус кода: ", res.status_code)
# print("Тип запроса: ",res.request)
# print("Тип запроса: ",res.request.method)
# print("URL сайта: ", res.url)
# print("Тип кодировки(юникод): ", res.encoding)
# print("Контент сайта: ", res.content)
# print(res.links)
# print(type(res.links))
# print(res.text)
# file_n.close() print(sum(map(int, text.split(None, 2)[:2])))

# res = requests.get(n)https://nurbek20.github.io/Wildlife/
# html1 = res.text
# file_n1 = open(f"{name}.html", "x")  https://www.google.ru/   http://www.nurcinema.kg/
# file_n1.write(html) 
# file_n1.close()

n = str(input("Вставте ссылку сайте: "))
try:
    res=requests.get(n)
    html=res.text
    name3=res.status_code
    if name3 == 404:
        print("Вы ввели неправильное название сайта. Такого пути не существует.")
    elif name3 == 200:
        name = n.split(".")[1]
        file_n = open(f"{name}.html", "x")
        file_n.write(html)
        file_n = open(f"{name}.html", "r")
        my_file=file_n.read()
        print(my_file)
        print ("количество изображений:", my_file.count('<img'))
        print ("количество кнопок:", my_file.count("<button"))
        print ("количество методов (<div):", my_file.count("<div"))
        lines = 0
        for i in open(f"{name}.html"):
            lines += 1
        print("Количества строчек: ", lines)
except FileExistsError:
    print("Такой файл уже существует")