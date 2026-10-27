import subprocess

from meme_format.utils.paths import OUTPUTS_DIR
from meme_format.utils.prompts import ask_for_string, pick_input_file
from meme_format.utils.text import print_header


def main():
    # Ask for the input mp4
    media_file = pick_input_file([".mp4", ".mov"])

    # Ask for the start time and duration
    print_header(2, "Clip information")
    start_time = ask_for_string("Start time", "00:00:00")
    duration = ask_for_string("Clip duration", "")
    output_filename = ask_for_string("Output file name", "output")

    output_file = OUTPUTS_DIR / (output_filename + media_file.suffix)

    # Extract clip
    print_header(2, "Extracting clip")
    if duration == "":
        subprocess.run(
            [
                "ffmpeg",
                "-ss",
                start_time,
                "-i",
                media_file,
                "-c:a",
                "copy",
                output_file,
            ],
            check=True,
        )
    else:
        subprocess.run(
            [
                "ffmpeg",
                "-ss",
                start_time,
                "-i",
                media_file,
                "-t",
                duration,
                "-c:a",
                "copy",
                output_file,
            ],
            check=True,
        )
