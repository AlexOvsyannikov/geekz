def first_task(first_katet=12, second_katet=14):
    return f"Катет_1: {first_katet}\nКатет_2: {second_katet}\nГипотенуза: {((first_katet ** 2) + (second_katet ** 2)) ** 0.5}"


def second_task(num_of_the_month=3):
    _data_about_seasons = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
    return f'За окном {_data_about_seasons[num_of_the_month // 3]}.' \
        if 0 < num_of_the_month < 13 else 'incorrect value'