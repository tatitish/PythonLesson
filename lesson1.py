def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumber(num):
    if 6 <= num <= 7:
        print('Этот день выходной')
  
    elif 0 < num < 6:
        print('Этот день не выходной')
  
    else:
        print('Число вне пределов 7 дней')
        
num = InputNumbers("Введи цифру, обозначающую день недели: ")
checkNumber(num)