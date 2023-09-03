def birthday_cake_candles_0(candles_heights: list) -> int:
    return candles_heights.count(max(candles_heights))

def birthday_cake_candles_1(candles_heights: list) -> int:
    max_candle_height = 0
    taller_candies_count = 0

    for index, height in enumerate(candles_heights):
        if index == 0:
            max_candle_height = height
        elif height > max_candle_height:
            max_candle_height = height

    for height in candles_heights:
        if height == max_candle_height:
            taller_candies_count += 1
    return taller_candies_count


if __name__ == '__main__':
    from tests import show_test_case

    show_test_case(0, {'candles_heights': [3, 2, 1, 3]}, 2, birthday_cake_candles_0)
    show_test_case(1, {'candles_heights': [18, 90, 90, 13, 90, 75, 90, 8, 90, 43]}, 5, birthday_cake_candles_0)
    show_test_case(2, {'candles_heights': [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]}, 4, birthday_cake_candles_0)
