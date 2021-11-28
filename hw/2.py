# Homework number 6;

def first():
    number = '23142569022'
    digit = 2
    count = 0
    for i in number:
        if i == str(digit):
            count += 1
    print(f'В строке {number} цифр {digit}: {count}')

