import requests
#  'https://api.openweathermap.org/data/2.5/weather?q="Osh"&units=metric&appid=48f56f7b62a5c368126ca352e69f0fac'
# city_name = "dubai"
city_name = input("Введите называния города: ")
API_key = '48f56f7b62a5c368126ca352e69f0fac'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
response = requests.get(API_url)
# print(response)
json_date = response.json()
# print(type(json_date))
# temp = json_date['clouds']
# print(temp)
# print(json_date['weather'])
# print(json_date['main']['temp'])
# print(json_date['main']['feels_like'])
# print("Температура города: ", json_date['main']['temp'], "градус")
# print("Ощущается как: ",json_date['main']['feels_like'], "градус")
# print("Минималный температура: ", json_date['main']['temp_min'],"градус")
# print("Максималный температура: ", json_date['main']['temp_max'],"градус")
status_sky=json_date['weather'] [0] ['main']
dic={"clear": "чистое небо","snow":"снежное", "rain":"дождь", "wind":"ветер", "clouds":"облака", "foggy":"туман"}
if status_sky.lower() in dic:
     
    print(f"""
Государство:             {json_date['sys']['country']}
Описания:                {dic[status_sky.lower()]}
Температура города:      {json_date['main']['temp']}    градус
Ощущается как:           {json_date['main']['feels_like']}    градус
Минималный температура:  {json_date['main']['temp_min']}    градус
Максималный температура: {json_date['main']['temp_max']}    градус
Давления:                {json_date['main']['pressure']}
Влажность:               {json_date['main']['humidity']}  
Облачность:              {json_date['clouds']['all']} %
""")
else:
    print(f"""
Государство:             {json_date['sys']['country']}
Описания:                {status_sky}
Температура города:      {json_date['main']['temp']}    градус
Ощущается как:           {json_date['main']['feels_like']}    градус
Минималный температура:  {json_date['main']['temp_min']}    градус
Максималный температура: {json_date['main']['temp_max']}    градус
Давления:                {json_date['main']['pressure']}
Влажность:               {json_date['main']['humidity']}  
Облачность:              {json_date['clouds']['all']} %
""")