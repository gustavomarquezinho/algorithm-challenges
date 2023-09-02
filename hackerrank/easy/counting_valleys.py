def counting_valleys(steps: int, path: str) -> int:
    SEA_LEVEL = 0
    position = SEA_LEVEL

    reached_below_sea_level = False
    valleys = 0

    for step in range(steps):
        if path[step] == 'U':
            position += 1
        else:
            position -= 1

        if position == (SEA_LEVEL - 1) and not reached_below_sea_level:
            reached_below_sea_level = True
            valleys += 1

        elif position == SEA_LEVEL and reached_below_sea_level:
            reached_below_sea_level = False
    return valleys


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'steps': 8, 'path': 'UDDDUDUU'}, 1, counting_valleys)
    show_test_case(1, {'steps': 12, 'path': 'DDUUDDUDUUUD'}, 2, counting_valleys)
    show_test_case(2, {'steps': 10, 'path': 'UDUUUDUDDD'}, 0, counting_valleys)
