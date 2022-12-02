# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример: - для k= 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

k = int(input('Задайте число: '))
x = [0]*(k * 2 + 1)
x[k + 1] = 1
for i in range(k + 2, k * 2 + 1):
    x[i] = x[i-1]+ x[i-2]
for j in range(k, -1, -1):
    x[j] = x[j+2] - x[j+1]
print(x)

# def fibonacciPos(n):
# a, b = 1, 1
# for i in range(n):
# yield a
# a, b = b, a + b

# dataPos = list(fibonacciPos(k))
# print(f'Для введенного вами числа {k} список чисел Фибоначи: {dataPos}')

# def fibonacciNeg(n):
# a, b = 1, -1
# for i in range(n):
# yield a
# a, b = b, a - b
