import requests
import simplejson as json
import asyncio
from googletrans import Translator

def translate_to_rus(text):
    translator = Translator()
    return asyncio.run(translator.translate(text, dest='ru')).text

'Aries'
list_of_signs = [
    'Aries',
    'Taurus',
    'Gemini',
    'Cancer',
    'Leo',
    'Virgo',
    'Libra',
    'Scorpio',
    'Sagittarius',
    'Capricorn',
    'Aquarius',
    'Pisces'
]

list_of_periods = [
    'daily',
    'weekly',
    'monthly'
]

def get_horoscope(sign, period):
    url = f'https://horoscope-app-api.vercel.app/api/v1/get-horoscope/{period}'
    parameters = {
        'sign': sign, 
        'day': 'TODAY'
    }
    headers = {
        'accept': 'application/json'
    }   
    response = requests.get(url, params=parameters, headers=headers)
    horoscope = response.json()['data']['horoscope_data']
    return translate_to_rus(horoscope)

print(get_horoscope(list_of_signs[0], list_of_periods[1]))