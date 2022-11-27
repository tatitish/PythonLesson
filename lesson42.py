# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



num = int(input('Введите число: '))
my_list = []
d = 2
while num > 1:
    if num % d == 0:
        my_list.append(d)
        num = num/d
    else:
        d += 1
print(my_list)