# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, 
# list comprehension(4 задачи из прошлых семинаров переделать с использованием этих функций)


# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
'''lst = [4, 5, 7, 83, 21, 50, 0, 5, 21]
def f(item):
    return len(list(filter(lambda x: x == item, lst))) == 1
result = list(filter(f, lst))
print(result)'''



#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
'''n = int(input('Введите число '))
numbers = [0,1]
for i in range(2, n + 1):
    numbers.append(numbers[i - 1] + numbers [i - 2])

not_numbers = list(map(lambda p: p[1] * (-1)**p[0], enumerate(numbers[1:])))
not_numbers.reverse()
print (not_numbers + numbers)'''




# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
'''lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))'''





#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''number = input('Введите число: ').split('.')
print(sum(map(int, number[1])))'''




# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
'''numbers = [2, 3, 4, 5, 6, 7, 5]
diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
print(diff)'''



