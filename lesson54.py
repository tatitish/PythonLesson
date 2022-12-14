# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open('origin.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст: '))
with open('origin.txt', 'r') as file:
    my_text = file.readline()

with open('rle_cod.txt', 'w', encoding='UTF-8') as file:
    file.write(coding(my_text))

print('Полученный текст для сжатия: ',my_text)
print("Результат RLE сжатия: ",coding(my_text))
print("Результат декодирования: ",decoding(coding(my_text)))

