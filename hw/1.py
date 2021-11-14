import math


def first_task(first_katet=12, second_katet=14):
    return f"Катет_1: {first_katet}\nКатет_2: {second_katet}\nГипотенуза: {((first_katet ** 2) + (second_katet ** 2)) ** 0.5}"


def second_task(num_of_the_month=3):
    _data_about_seasons = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
    return f'За окном {_data_about_seasons[num_of_the_month // 3]}.' \
        if 0 < num_of_the_month < 13 else 'incorrect value'


def third_task(num):
    previous_power = math.floor(math.log2(num))
    return 2 ** previous_power


def fourth_task(num=9):
    res = []
    for i in range(1, 10):
        print(f'{i} * {num} = {i * num}')
        res.append(i * num)
    return res


# basic function for fifth_task
def f(x):
    y = (0.1 * (x ** 3)) - (2 / x)
    return y


def fifth_task():
    suitable = []
    for x in range(-20, 21):
        try:
            y = f(x)
            if abs(y) < 10:
                suitable.append(x)
        except Exception as e:
            print(e)
            print(x)
            print('Function might not exist in this point')

    return suitable
