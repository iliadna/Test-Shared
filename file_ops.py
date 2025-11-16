def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content)


def append_line(path: str, line: str) -> None:
    with open(path, "a") as f:
        f.write(line + "\n")
