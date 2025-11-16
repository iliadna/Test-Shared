def filter_positive(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n > 0]


def sum_list(numbers: list[int]) -> int:
    return sum(numbers)


def normalize(numbers: list[float]) -> list[float]:
    total = sum(numbers)
    return [n / total for n in numbers] if total else numbers
