#5.6 Задачи
#1. Fizz Buzz

number = int(input('\n\tx = '))

print('\tРезультат: ', end='')

if number >= 0:
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(str(number))

#2. Оценка числа

number = int(input('\n\tx = '))

print('\tРезультат: ', end='')

if number >= 0:
    if number % 2 == 1:
        print('Плохо')
    elif (number >= 2) and (number <= 5):
        print('Неплохо')
    elif (number >= 6) and (number <= 20):
        print('Так себе')
    else:
        print('Отлично')

#3. Последовательность

number = int(input('\n\tx = '))

print('\tРезультат: ', end='')

if (number > 0) and (number < 10):
    for i in range(number):
        print(i + 1, end='')

#4. Секретное сообщение

text = input('\n\n\tТекст =  ')

print('\tРезультат: ', end='')

for i in text:
    if i.isupper():
        print(i, end='')