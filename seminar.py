# напечатать стpoку в одну линию - C:\WINDOWS\System32\drivers\etc\nst

'''f = open('filetest.txt', 'r')
print(f.readline())
'''



# преобразовать список таким образом

# a = [4, 3, -10, 1, 7, 12]  ->  [4, -10, 12, 3, 1, 7]

'''a = [4, 3, -10, 1, 7, 12]
b = [i for i in a if i%2==0]
c = [i for i in a if i%2!=0]
print(a,'->', b+c)'''

'''a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)'''




# На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий.
# Результат вывести в одну строчку через пробел.
#
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

'''rivers = input('Введите список рек через пробел: ')
rivs = list(rivers.split())
len_riv=[]
for i in rivs:
    len_riv.append(len(i))
result = list(zip(rivs, len_riv))
result.sort(key=lambda x: x[1], reverse=True)
print(result)'''

'''s=sorted(input().split(), key=lambda x: len(x))[::-1]
print(*s)'''



# Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее.
# То есть, число пар может быть 10 и менее.
# Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.

'''inp_string=input('')
zipper = [i for i in range(11)]
result = list(zip(inp_string, zipper))
print(*result)'''

'''n = 10
lst = []
for i in zip(range(0,n+1),input('введите текст: ')):
    lst.append(i)
print(lst)'''

'''s = input()
lst = list(zip(s, range(10)))
print(lst)'''




# 5. Напишите функцию triangle(a, b, c),
# которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

'''triangle = lambda a,b,c: print('Это треугольник') if a+b>c and c+b>a and a+c>b else print('Как говорил Шарик: индийский дом')
triangle(7,6,10)'''