import os
import subprocess

from meme_format.utils.paths import OUTPUTS_DIR, TEMP_DIR
from meme_format.utils.prompts import ask_for_string, clear_folder, pick_input_file
from meme_format.utils.text import print_header

INPUT_FRAMES_DIR = TEMP_DIR / "input_frames"
OUTPUT_FRAMES_DIR = TEMP_DIR / "output_frames"


def main():
    # Ask user for file paths
    target_gif = pick_input_file([".gif"], "Left gif")
    right_image = pick_input_file([".png", ".jpg"], "Right image")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")

    output_gif = OUTPUTS_DIR / f"{output_filename}.gif"

    # Remove existing folders
    clear_folder(INPUT_FRAMES_DIR, "Clearing input frames folder")
    clear_folder(OUTPUT_FRAMES_DIR, "Clearing output frames folder")

    # Split the gif into individual frames
    print_header(2, "Splitting gif into individual frames")
    os.system(f'ffmpeg -i "{target_gif}" "{INPUT_FRAMES_DIR}/frame_%d.png"')

    # Join each frame with the image to the right
    print_header(2, "Joining each frame with the image to the right")

    processes: list[subprocess.Popen[bytes]] = []
    for filename in os.listdir(INPUT_FRAMES_DIR):
        print_header(3, f"Joining {filename}")

        process = subprocess.Popen(
            f'ffmpeg -i "{INPUT_FRAMES_DIR}/{filename}" -i "{right_image}" -filter_complex hstack -y "{OUTPUT_FRAMES_DIR}/{filename}"'
        )
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.wait()

    # Join the frames into a gif
    print_header(2, "Joining the frames into a gif")
    os.system(f'ffmpeg -f image2 -i "{OUTPUT_FRAMES_DIR}/frame_%d.png" "{output_gif}"')
