from typing import Callable


def show_test_case(case: int, inputs: dict, expected_output, func: Callable):
    print(f"---- Test case {case} ----")
    print(f'Your output: {func(**inputs)}')
    print(f'Expected output: {expected_output}\n')
