import subprocess

from meme_format.utils.paths import OUTPUTS_DIR, TEMP_DIR
from meme_format.utils.prompts import ask_for_string, clear_folder, pick_input_file
from meme_format.utils.text import print_header

FRAMES_DIR = TEMP_DIR / "frames"


def main():
    # Ask user for file paths
    first_image = pick_input_file([".png", ".jpg"], "First image")
    second_image = pick_input_file([".png", ".jpg"], "Second image")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")

    output_gif = OUTPUTS_DIR / f"{output_filename}.gif"

    # Clear the frames folder
    clear_folder(FRAMES_DIR, "Clearing frames folder")

    # Create the frames
    print_header(2, "Creating frames")
    subprocess.run(
        [
            "ffmpeg",
            "-loop",
            "1",
            "-i",
            first_image,
            "-loop",
            "1",
            "-i",
            second_image,
            "-filter_complex",
            "[1:v][0:v]blend=all_expr='A*(if(gte(T,3),1,T/3))+B*(1-(if(gte(T,3),1,T/3)))'",
            "-t",
            "4",
            FRAMES_DIR / "image_%d.png",
        ],
        check=True,
    )

    # Join the frames into a gif
    print_header(2, "Joining the frames into a gif")
    subprocess.run(
        [
            "ffmpeg",
            "-f",
            "image2",
            "-i",
            FRAMES_DIR / "image_%d.png",
            output_gif,
        ],
        check=True,
    )
