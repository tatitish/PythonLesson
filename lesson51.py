# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Неабв слеабдует огорабвчаться по пуаабстякам'
find_txt = "абв"
lst = [i for i in my_text.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')