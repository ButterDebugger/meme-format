from utils.text import dim_text, print_header

def pick_file(path: str, extensions: list[str], header: str = "Pick a file"):
    import os
    from pathlib import Path

    print_header(12, header)

    root_path = Path(path)
    media_files: list[str] = []

    for filename in os.listdir(root_path):
        filepath = Path(filename)

        if filepath.suffix not in extensions:
            continue

        media_files.append(filename)

        print(f"[{len(media_files)}]  {filename}")

    if len(media_files) == 0:
        print("No files found")
        exit(1)

    choice = int(input("Pick a file: "))

    return root_path / media_files[choice - 1]

def ask_for_string(prompt: str, default: str = "") -> str:
    answer = input(f"{prompt}: " if default == "" else f"{prompt} {dim_text(f"[{default}]")}: ")

    if answer == "":
        answer = default

    return answer

def ask_for_boolean(prompt: str, default: bool = False) -> bool:
    optional_text = dim_text("Y/n" if default else "y/N")

    while True:
        answer = input(f"{prompt} {optional_text}: ")

        if answer == "":
            return default
        elif answer.lower() in ["y", "yes"]:
            return True
        elif answer.lower() in ["n", "no"]:
            return False
        else:
            print("Invalid answer")

def ask_for_int(prompt: str, default: int | None = None) -> int:
    optional_text = "" if default is None else dim_text(f" [{default}]")

    while True:
        answer = input(f"{prompt}{optional_text}: ")

        # If the answer is empty
        if answer == "":
            if default is None:
                # There is no default, so ask again
                print("Invalid answer")
                continue
            else:
                # Return the default
                return default

        # Try to convert the answer to an int
        try:
            answer = int(answer)

            return answer
        except ValueError:
            print("Invalid answer")
            continue

def clear_folder(path: str, header: str = "Clearing folder"):
    import os
    from shutil import rmtree

    print_header(9, header)

    if os.path.exists(path):
        print(f"Removing {path}")
        rmtree(path, ignore_errors=True)

    os.makedirs(path)
    print(f"Created {path}")
