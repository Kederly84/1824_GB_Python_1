import requests
import datetime

def currency_rates(curr_name: str) -> str:
    """"Функция с помощью строковых методов разбирает ответ от сервера
    и возвращает курс и дату"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currences ={}
    curr_name = curr_name.upper()
    r = requests.get(url, timeout=2)
    content = r.text
    date_finder = content.find('Date')
    date = datetime.datetime.strptime(content[(date_finder + 6):(date_finder + 16)], '%d.%m.%Y')
    stroke = content.split('<Valute')
    for i in stroke:
        char_idx = i.find('<CharCode>')
        char_value = i.find('Value')
        char = i[(char_idx + 10):(char_idx + 13)]
        value = i[(char_value + 6):(char_value + 13)].replace(',', '.')
        currences[char] = value
    if curr_name not in currences.keys():
        answer = None
    else:
        answer = f'{round(float(currences.get(curr_name)), 2)}, {date}'
    return answer

if __name__ == '__main__':
    print('Зачем я это сотворил')