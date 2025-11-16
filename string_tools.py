def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)


def to_snake_case(text: str) -> str:
    return text.replace(" ", "_").lower()
