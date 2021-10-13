from utils import currency_rates

# Список для проверки многократного вывода
ask = ['AUD', 'USD', 'GBP', 'EUR', 'INR']

# Реализация многократного запроса к функции
for i in ask:
    answer = currency_rates(i)
    print(f'{i} {answer}')
