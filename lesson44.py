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
    
    
    
# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
# koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
# if k == 1:
# ans.append(f'{koefs[i]}*x')
# elif k == 0:
# ans.append(f'{koefs[i]}')
# else:
# ans.append(f'{koefs[i]}*x**{k}')
# flag = randint(0, 1)
# if flag == 1:
# ans.append('+')
# elif flag == 0:
# ans.append('-')
# k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()
    
    
    
    
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# import random
# def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
# if b > 0:
# res += '+' + str(b) + '*x'
# if c > 0:
# res += '+' + str(c)
# return f'{a}*x^2' + res


# def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
# if b > 0:
# res += '+' + str(b) + '*x'
# if c > 0:
# res += '+' + str(c)
# return f'{a}*x^2' + res


# f = open('dz40.txt', 'w')
# f.write(nmnogochlen1())
# print(nmnogochlen1())
# f.close()

# f = open('dz41.txt', 'w')
# f.write(nmnogochlen2())
# print(nmnogochlen2())
# f.close()
# f = open('dz40.txt', 'r')
# list_5 = str(f.readline()).split('x')
# c1 = b1 = a1 = 0
# if len(list_5) == 3:
# c1 = list_5[2][1:]
# if len(list_5) >= 2:
# b1 = list_5[1][3:-1]
# a1 = list_5[0][:-1]
# f.close()

# f = open('dz41.txt', 'r')
# list_51 = str(f.readline()).split('x')
# c2 = b2 = a2 = 0
# if len(list_51) == 3:
# c2 = list_51[2][1:]
# if len(list_51) >= 2:
# b2 = list_51[1][3:-1]
# a2 = list_51[0][:-1]
# f.close()

# f = open('dz42.txt', 'w')
# f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# f.close()


ffile1 = open('file1.txt', 'r')
ffile2 = open('file2.txt', 'r')
ffile3 = open('file3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()
for i in range(len(file1)):
if file1[i-1] != '^':
if file1[i].isnumeric():
ffile3.write(str(int(file1[i])+int(file2[i])))
else:
ffile3.write(str(file1[i]))
else:
ffile3.write(str(file1[i]))
ffile1.close
ffile2.close
ffile3.close
