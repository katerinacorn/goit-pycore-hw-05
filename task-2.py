import re
from typing import Generator, Callable

NUMBER_PATTERN = r"(?<=\s)(\d+\.\d+|\d+)(?=\s)"  # Matches numbers with optional decimal point, surrounded by spaces
EPSILON = 1e-6


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator function that extracts all real numbers from the input text.
    Numbers are expected to be separated by spaces.

    :param text: Input string containing numbers separated by spaces.
    :yield: Each found number as a float.
    """
    for match in re.finditer(NUMBER_PATTERN, text):
        yield float(match.group(0))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculate the total sum of all numbers extracted by the provided generator function.

    :param text: Input text containing numbers.
    :param func: Generator function that yields numbers from the text.
    :return: Sum of all extracted numbers.
    """
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 "
        "і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


# =============================
# ========== TESTS ============
# =============================

SALARY = 12.5
BONUS = 200.0
PREMIUM = 13.37
test_text = f"Зарплата: {SALARY} бонус: {BONUS} і премія {PREMIUM} наприкінці місяця."

expected_numbers = [SALARY, BONUS, PREMIUM]
generated_numbers = list(generator_numbers(test_text))

assert (
    generated_numbers == expected_numbers
), f"Expected {expected_numbers}, got {generated_numbers}"

expected_total = sum(expected_numbers)
actual_total = sum_profit(test_text, generator_numbers)
assert (
    abs(actual_total - expected_total) < EPSILON
), f"Expected {expected_total}, got {actual_total}"

print("All tests passed.")
