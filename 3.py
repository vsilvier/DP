#3.6 Задачи
#1. Welcome to Python

name = 'Ilya'
surname = 'Vasilev'

print(f'\nHello {name} {surname}! You just delved into Python. Great start!\n')

#2. Python art

thickness = 5
c = 'H'

print((c * thickness).center(thickness * 3))

for i in range((thickness - 1) // 2):
    print((c * thickness + ' ' * (2 * i + 2 - thickness % 2) + c * thickness).center(thickness * 3))

for i in range(thickness):
    print(c * thickness + ' ' * thickness + c * thickness)

for i in range((thickness - 1) // 2):
    print((c * thickness + ' ' * (thickness - i * 2 - 2) + c * thickness).center(thickness * 3))

print((c * thickness).center(thickness * 3))

#3. Заголовок

text = "I am doing my homework right now. Please, don't disturb me!"

print(f'\n\t{text = }')
print(f'\t{text.title() = }')

#4. Форматированный вывод денежной суммы

amount = 100500.157

print(f'\n\t{amount = }')
print('\tРезультат = {0:,.2f}'.format(amount))