def print_header(color: int, message: str):
    print(f"\x1b[48;5;{color}m {message} \x1b[0m")

def dim_text(text: str) -> str:
    return f"\x1b[2m{text}\x1b[0m"
