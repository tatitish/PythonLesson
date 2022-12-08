from os.path import exists
from lesson71csv import creating
from lesson71writing import writing_scv
from lesson71writing import writing_txt


path = 'lesson71Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()