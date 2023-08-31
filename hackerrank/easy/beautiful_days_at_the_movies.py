def beautiful_days_at_the_movies(starting_day: int, ending_day: int, divisor: int) -> int:
    days = 0

    for day in range(starting_day, ending_day + 1):
        reversed_day = int(str(day)[::-1])

        if(day - reversed_day) % divisor == 0:
            days += 1
    return days


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'starting_day': 49860, 'ending_day': 205494, 'divisor': 155635764}, 607, beautiful_days_at_the_movies)
    show_test_case(8, {'starting_day': 20, 'ending_day': 23, 'divisor': 6}, 2, beautiful_days_at_the_movies)
    show_test_case(9, {'starting_day': 1, 'ending_day': 123456, 'divisor': 13}, 9657, beautiful_days_at_the_movies)
