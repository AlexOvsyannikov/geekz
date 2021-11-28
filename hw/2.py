# Homework number 6;

def first():
    number = '23142569022'
    digit = 2
    count = 0
    for i in number:
        if i == str(digit):
            count += 1
    print(f'В строке {number} цифр {digit}: {count}')


def second():
    code = '19sdf*'
    min_count = 6
    count = 0
    for i in code:
        if i != "*":
            count += 1
        else:
            break
    if count < min_count:
        print(f'Код слишком короткий\nЧисло символов до кода {count}')
    else:
        print('Все ок')


