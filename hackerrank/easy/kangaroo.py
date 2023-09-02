def kangaroo(pos_1: int, vel_1: int, pos_2: int, vel_2: int) -> str:
    if (pos_1 <= pos_2 and vel_1 <= vel_2) or (pos_2 <= pos_1 and vel_2 <= vel_1):
        return 'NO'

    for _ in range(10_000):
        if pos_1 == pos_2:
            return 'YES'

        pos_1 += vel_1
        pos_2 += vel_2
    return 'NO'


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'pos_1': 0, 'vel_1': 3, 'pos_2': 4, 'vel_2': 2}, 'YES', kangaroo)
    show_test_case(1, {'pos_1': 0, 'vel_1': 2, 'pos_2': 5, 'vel_2': 3}, 'NO', kangaroo)
    show_test_case(20, {'pos_1': 2932, 'vel_1': 7030, 'pos_2': 9106, 'vel_2': 4840}, 'NO', kangaroo)
