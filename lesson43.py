# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

# numbers = list(map(int, input("Введите числа через пробел:\n").split()))
# print(numbers)
# new_numbers = []

# for i in numbers:
# if i not in new_numbers:
# new_numbers.append(i)
# print(new_numbers)

# def elements(nums):
# nums = [int(i) for i in nums.split()]
# return list(set(nums))
# numbers = '1 1 2 2 3 455 66 66 2 1'
# print(elements(numbers))


# a= [1,2,2,2,2,3,1,4]
# print(set(a))

# b = [1, 1, 2, 3, 3, 4, 5]
# a = []
# for i in b:
# if b.count(i) == 1:
# a.append(i)

# print(a)
