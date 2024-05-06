import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def get_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password
    
num = int(input('Введите количество паролей:'))
length = int(input('Какова будет длина пароля?:'))
need_digits = input('Нужны ли цифры?:')
need_capital = input('Включать ли прописные буквы?:')
need_lower = input('Включать ли строчные буквы?:')
need_punct = input('Включать ли спец. символы?:')
ignore_bad_symb = input('Исключать ли неоднозначные символы?:')

chars = ""
if need_digits.lower() == 'да':
    chars += digits
if need_capital.lower() == 'да':
    chars += lowercase_letters
if need_lower.lower() == 'да':
    chars += uppercase_letters
if need_punct.lower() == 'да':
    chars += punctuation
if ignore_bad_symb == 'да':
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')

for _ in range(num):
    password = get_password(length, chars)
    print(password)
