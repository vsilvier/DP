#7. Задачи
#1. Анализ текста. Популярность.

import re

text = input('\n\tВведите текст: ')
lower_text = text.lower()
split_text = re.split('[ ,.!?;:()\[\]"\'`\-_|/]+', lower_text)

words = {}
letters = {}

for word in split_text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

print('\n\tСлова: {0}'.format(words))
print(f'\tБуквы: {letters}')

#2. Римские цифры

number = int(input('\n\tВведите число: '))

dictionary = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

decreasing = number
roman = ''
while decreasing:
    for key, value in dictionary.items():
        if key <= decreasing:
            roman += value
            decreasing -= key
            break

print(f'\tРезультат: {roman}')

#3. Ленивый спекулянт

import sys

banks_rates = {
    'Тинькофф Банк': 60.05,
    'Альфа Банк': 60.01,
    'Сбербанк': 66.45,
    'Газпромбанк': 63.98,
    'ВТБ': 64.80,
}

min_rate = sys.float_info.max
for bank, rate in banks_rates.items():
    if rate < min_rate:
        min_rate = rate
        min_bank = bank

print(f'\n\tРейтинг: {banks_rates}')
print(f'\tРезультат: {min_bank} -> {min_rate:,.2f}.')

#4. Вверх дном

name = {
    'Васильев И.Г.': '88888',
    'Князев А.С.': '77777',
    'Соколов Е.М.': '66666',
}

phone = dict(zip(name.values(), name.keys()))

print(f'\n\tСловарь: {name}')
print(f'\tРезультат: {phone}')

#5. Структурируем данные

dates = ['2022-11-15', '2022-11-16', '2022-11-17']
rates = [60.33, 60.44, 60.55]

dates_rates = dict(zip(dates, rates))

print(f'\n\tДаты: {dates}')
print(f'\tКурсы: {rates}')
print(f'\tРезультат: {dates_rates}')