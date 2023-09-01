def designer_pdf_viewer(letters_heights: list, word: str) -> int:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    tallest_letter = 0

    for letter in word:
        letter_index = letters.find(letter.lower())

        if not 0 <= letter_index < len(letters):
            continue

        if letters_heights[letter_index] > tallest_letter:
            tallest_letter = letters_heights[letters.find(letter)]

    area = tallest_letter * len(word)
    return area


if __name__ == '__main__':
    from tests import show_test_case

    letters_heights_0 = [
        1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
    ]

    show_test_case(0, {'letters_heights': letters_heights_0, 'word': 'abc'}, 9, designer_pdf_viewer)

    letters_heights_1 = [
        6, 5, 7, 3, 6, 7, 3, 4, 4, 2, 3, 7, 1, 3, 7, 4, 6, 1, 2, 4, 3, 3, 1, 1, 3, 5
    ]

    show_test_case(1, {'letters_heights': letters_heights_1, 'word': 'zbkkfhwplj'}, 70, designer_pdf_viewer)

    letters_heights_6 = [
        1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7
    ]

    show_test_case(6, {'letters_heights': letters_heights_6, 'word': 'zaba'}, 28, designer_pdf_viewer)
