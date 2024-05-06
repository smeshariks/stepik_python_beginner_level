import random
num = random.randint(1, 100)
print ('Добро пожаловать в числовую угадайку')

def is_valid(text):
    return text.isdigit() and int(text) >= 1 and int(text) <= 100

while True:
    while True:
        txt = input()
        if is_valid(txt):
            num1 = int(txt)
            break
        else:
            print ('А может быть все-таки введем целое число от 1 до 100?')
            
    if num1 == num:
        print ('Вы угадали, поздравляем!')
        print ('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    elif num1 > num:
        print ('Ваше число больше загаданного, попробуйте еще разок')
    elif num1 < num:
        print ('Ваше число меньше загаданного, попробуйте еще разок')