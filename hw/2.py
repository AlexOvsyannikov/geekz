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


def third():
    number_1 = '213134'
    number_2 = '333322'
    number_3 = '312356'

    all_nums = [number_1, number_2, number_3]
    sums = []
    for num in all_nums:
        sum_for_one = 0
        for digit in num:
            sum_for_one += int(digit)
        sums.append(sum_for_one)

    print(f'Сумма цифр первого числа: {sums[0]}\nСумма цифр второго числа: {sums[1]}\n'
          f'Сумма цифр третьего числа: {sums[2]}\nМаксимальная сумма цифр: {max(sums)}')



