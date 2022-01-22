import requests
from googletrans import Translator
translator = Translator()
name = int(input("""Выберите язык чтобы узнат прогноз погода на вашем языке
Русский-язык 1:
Кыргыз-тили 2:
English-languege 3:
日本語  4: 
Français 5:
:6 اللغة العربية
Türk Dili 7: """))
translator = Translator()
# t = translator.translate("Введите называния города: ", dest='').text
city_name = input("Введите называния города: ")
# translator.translate(city_name, dest='en').text
API_key = '48f56f7b62a5c368126ca352e69f0fac'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
translator = Translator()
res = requests.get(API_url)
json_data = res.json()
if name == 1:
    res = requests.get(API_url)
    json_data = res.json()
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='ru').text)
elif name == 2:
     print(translator.translate(f"""
     температура ,{json_data['main']['temp']}
     мин температура', {json_data['main']['temp_min']}
     Ощущается как',{json_data['main']['feels_like']}
     Погода: {json_data['weather'][0]['main']}""", dest='ky').text)
elif name == 3:
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='en').text)
elif name == 4:
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='ja').text)
elif name == 5:
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='fr').text)
elif name == 6:
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='ar').text)
elif name == 7:
    print(translator.translate(f"""
    температура ,{json_data['main']['temp']}
    мин температура', {json_data['main']['temp_min']}
    Ощущается как',{json_data['main']['feels_like']}
    Погода: {json_data['weather'][0]['main']}""", dest='tr').text)
else:
    print("Неверная команда!!!!")


# from googletrans.gtoken import TokenAcquirer
# acquirer = TokenAcquirer()
# text = 'test'
# tk = acquirer.do(text)
# tk
# 950629.577246
# langs = translator.detect(['한국어', '日本語', 'English', 'le français'])
# for lang in langs:
# ...    print(lang.lang, lang.confidence)
# ko 1
# ja 0.92929292
# en 0.96954316
# fr 0.043500196
# >>> from googletrans import Translator
# >>> translator = Translator()
# >>> translator.detect('이 문장은 한글로 쓰여졌습니다.')
# <Detected lang=ko confidence=0.27041003>
# >>> translator.detect('この文章は日本語で書かれました。')
# <Detected lang=ja confidence=0.64889508>
# >>> translator.detect('This sentence is written in English.')
# <Detected lang=en confidence=0.22348526>
# >>> translator.detect('Tiu frazo estas skribita en Esperanto.')
# <Detected lang=eo confidence=0.10538048>
# >>> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
# >>> for translation in translations:
# ...    print(translation.origin, ' -> ', translation.text)
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개
# >>> from googletrans import Translator
# >>> translator = Translator()
# >>> translator.translate('안녕하세요.')
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# >>> translator.translate('안녕하세요.', dest='ja')
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# >>> translator.translate('veritas lux mea', src='la')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
# >>> translator.detect('이 문장은 한글로 쓰여졌습니다.')
# # <Detected lang=ko confidence=0.27041003>
# >>> translator.detect('この文章は日本語で書かれました。')
# # <Detected lang=ja confidence=0.64889508>
# >>> translator.detect('This sentence is written in English.')
# # <Detected lang=en confidence=0.22348526>
# >>> translator.detect('Tiu frazo estas skribita en Esperanto.')
# # <Detected lang=eo confidence=0.10538048>
# >> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
# >>> for translation in translations:
# ...    print(translation.origin, ' -> ', translation.text)
# # The quick brown fox  ->  빠른 갈색 여우
# # jumps over  ->  이상 점프
# # the lazy dog  ->  게으른 개
# >>> from googletrans import Translator
# >>> translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
# >>> from googletrans import Translator
# >>> translator = Translator()
# >>> translator.translate('안녕하세요.')
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

# >>> translator.translate('안녕하세요.', dest='ja')
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

# >>> translator.translate('veritas lux mea', src='la')
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>