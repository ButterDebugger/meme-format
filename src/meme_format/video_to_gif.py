import subprocess

from meme_format.utils.paths import OUTPUTS_DIR
from meme_format.utils.prompts import ask_for_int, ask_for_string, pick_input_file
from meme_format.utils.text import print_header


def main():
    # Ask user for target video
    target_video = str(pick_input_file([".mp4", ".mov"], "Target video"))

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")
    frame_rate = ask_for_int("Frame rate", 24)

    output_gif = OUTPUTS_DIR / f"{output_filename}.gif"

    # Convert to gif
    print_header(2, "Converting to gif")

    # Execute the command
    filter_complex = f"[0:v] fps={frame_rate},split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1"

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            target_video,
            "-y",
            "-filter_complex",
            filter_complex,
            output_gif,
        ],
        check=True,
    )
