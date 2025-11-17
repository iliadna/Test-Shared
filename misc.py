def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def square_dict(n: int) -> dict[int, int]:
    return {i: i * i for i in range(1, n + 1)}


def repeat_string(s: str, times: int) -> str:
    return s * times
