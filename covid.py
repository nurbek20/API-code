import requests
# from googletrans import Translator   https://covid-api.mmediagroup.fr/v1/history?country=china&status=Confirmed
# url = f'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
# country1 = input("Введите называния города: ").title()
# url1 = f'https://covid-api.mmediagroup.fr/v1/cases?country={country1}'
# country2 = input("Введите называния страна: ").title()
# url2 = f'https://covid-api.mmediagroup.fr/v1/cases?country={country2}'
# apy='https://github.com/M-Media-Group/country-json/blob/master/src/countries-master.json'
# res1 = requests.get(url2)
# json1_d = res1.json()
# print(type(res))
country = int(input("""Введите называния страны 1: 
Введите называния города 2:"""))
if country == 1:
    country2 = input("Введите называния страна: ").title()
    url1 = f'https://covid-api.mmediagroup.fr/v1/cases?country={country2}'
    res = requests.get(url1)
    json_d = res.json()
    print(f"""
подтверждено            {json_d['All']['confirmed']}
восстановлено           {json_d['All']['recovered']}
смертей                 {json_d['All']['deaths']}
страна                  {json_d['All']['country']}
население               {json_d['All']['population']}
кв.км_площадь           {json_d['All']['sq_km_area']}
жизнь_продолжительность {json_d['All']['life_expectancy']}
высота в метрах         {json_d['All']['elevation_in_meters']}
континент               {json_d['All']['continent']}
аббревиатура            {json_d['All']['abbreviation']}
местоположение          {json_d['All']['location']}
исо                     {json_d['All']['iso']}
столица                 {json_d['All']['capital_city']}
""")
# elif country == 2:
#     country1 = input("Введите называния города: ").title()
#     url2 = f'https://covid-api.mmediagroup.fr/v1/cases?country={country1}'
#     res1 = requests.get(url2)
#     json1_d = res1.json()
#     print(f"""
# "лат": "40.1824",   {['All'],json1_d,['lat']}

#     """)
country = input("Введите называния страна: ").title()
url = f'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
res = requests.get(url)
print("подтверждено"  res.json()['All']['confirmed'])
print("восстановлено" res.json()['All']['recovered'])
print("смертей "    res.json()['All']['deaths'])
print("страна  "  res.json()['All']['country'])
print("население " res.json()['All']['population'])
city = input("Пишите назывантя города: ")
if city in res.json():
    print("Подтверждено: ", res.json()[city]['confirmed'])
    print("Умерли: ", res.json()[city]['deaths'])