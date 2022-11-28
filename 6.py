#6.6 Задачи
#1. Последний с четными

numbers = []

while True:
    output_check = input('\n\tЗакончили? Введите "да". Если нет, нажмите "Enter"\t')
    if output_check == 'да':
        break

    numbers.append(int(input('\tВведите число: ')))

print(f'\n\tСписок: {numbers}')

if numbers:
    result = sum(numbers[::2]) * numbers[-1]
else:
    result = 0

print(f'\tРезультат: {result}')

#2. Max-min

numbers = []

while True:
    output_check = input('\n\tЗакончили? Введите "да". Если нет, нажмите "Enter"\t')
    if output_check == 'да':
        break

    numbers.append(float(input('\tВведите число: ')))

print(f'\n\tСписок: {numbers}')

if numbers:
    result = max(numbers) - min(numbers)
else:
    result = 0

print('\tРезультат: {0:.3f}'.format(result))

#3. Умная сортировка

list_numbers = []

while True:
    output_check = input('\n\tЗакончили? Введите "да". Если нет, нажмите "Enter"\t')
    if output_check == 'да':
        break

    list_numbers.append(int(input('\tВведите число: ')))

tuple_numbers = tuple(list_numbers)
print(f'\n\tКортеж: {tuple_numbers}')

result = sorted(tuple_numbers, key=lambda number: abs(number))

print(f'\tРезультат: {result}')