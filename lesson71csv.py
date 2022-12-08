def creating ():
    file = 'lesson71Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Описание\n')
        