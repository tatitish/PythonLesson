# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k = '))
array = []

for i in range(k + 1):
    array.append(randint(0, 100))
result = []

for i in range(k,-1,-1):
    if array[i] != 0:
        if i == 0:
            result.append(f'{array[i]}')
        elif i == 1:
            result.append(f'{array[i]}*x')
        else:
            result.append(f'{array[i]}*x^{i}')

with open ('file.txt', 'w') as data:
    data.write(" + ".join(result) + " = 0") 