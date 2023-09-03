def the_birthday_bar(chocolate_squares: list, birth_day: int, birth_month: int) -> int:
    ways_to_divide = 0

    for i in range(len(chocolate_squares)):
        if sum(chocolate_squares[i:i + birth_month]) == birth_day:
            ways_to_divide += 1
    return ways_to_divide


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'chocolate_squares': [1, 2, 1, 3, 2], 'birth_day': 3, 'birth_month': 2}, 2, the_birthday_bar)
    show_test_case(1, {'chocolate_squares': [1, 1, 1, 1, 1, 1], 'birth_day': 3, 'birth_month': 2}, 0, the_birthday_bar)
    show_test_case(5, {'chocolate_squares': [5, 2, 2, 1, 5, 3, 2], 'birth_day': 9, 'birth_month': 3}, 2, the_birthday_bar)
