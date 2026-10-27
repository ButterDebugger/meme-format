import subprocess

from meme_format.utils.paths import OUTPUTS_DIR
from meme_format.utils.prompts import ask_for_int, ask_for_string, pick_input_file
from meme_format.utils.text import print_header


def main():
    # Ask user for file paths
    target_gif = str(pick_input_file([".gif"], "Gif to optimize"))

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "optimized")
    new_width = ask_for_int("New width", 320)
    max_colors = ask_for_int("Max colors", 256)

    output_gif = OUTPUTS_DIR / f"{output_filename}.gif"

    # Optimize the gif
    print_header(2, "Optimizing the gif")

    # Execute the command
    filter_complex = f"scale={new_width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors={max_colors}[p];[s1][p]paletteuse=dither=bayer"

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            target_gif,
            "-filter_complex",
            filter_complex,
            output_gif,
        ],
        check=True,
    )
