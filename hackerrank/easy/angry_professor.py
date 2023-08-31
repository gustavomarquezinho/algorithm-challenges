def angry_professor(min_students: int, times: list) -> str:
    arrived = 0

    for time in times:
        if time <= 0:
            arrived += 1

    if arrived < min_students:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'min_students': 3, 'times': [-1, -3, 4, 2]}, 'YES', angry_professor)
    show_test_case(0, {'min_students': 2, 'times': [0, -1, 2, 1]}, 'NO', angry_professor)
    show_test_case(1, {'min_students': 4, 'times': [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]}, 'NO', angry_professor)
