# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

x = [1.1, 1.2, 3.1, 5, 10.01]
max = x[0]
min = x[0]
for i in x:
    if round(x[0]%1, 4) < round((i)%1, 4):
        max = round((i)%1, 4)
    if round(x[0]%1, 4) > round((i)%1, 4):
        min = round((i)%1, 4)
    raznicha = max - min
print(raznicha)

# list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in list:
# if (i % 1) <= min:
# min = i % 1
# if ( i % 1) >= max:
# max = i % 1
# print (f"Разница между максимальным и минимальным значением дробной части равна: {(max-min)}")
