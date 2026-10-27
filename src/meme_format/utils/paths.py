from pathlib import Path

INPUTS_DIR = Path.cwd() / "input_media"
OUTPUTS_DIR = Path.cwd() / "output_media"
TEMP_DIR = Path.cwd() / "temp"


def create_dirs(dir: Path):
    dir.mkdir(parents=True, exist_ok=True)
