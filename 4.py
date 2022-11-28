#4.6 Задачи
#1. Среднее

from random import randint

a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)

print(f'\n\t({a} + {b} + {c}) / 3 = {(a + b + c) // 3}')

#2. Деление и еще раз деление

from random import randint

x = randint(0, 100)
y = randint(0, 100)

print(f'\n\t{x=}\n\t{y=}')
print(f'\tРезультат = {x // y}, {x % y}')

#3. Округление

number = 14.721

print('\n\tx = {0}'.format(number))
print('\t1. {0:.2f}'.format(number))
print('\t2. {0:.0f}'.format(number))
print('\t3. {0:=011}'.format(number))