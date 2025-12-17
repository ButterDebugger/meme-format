import os
import sys
import subprocess
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_string, clear_folder, pick_file
from utils.text import print_header

input_frames_path = str(cwd / "input_frames")
output_frames_path = str(cwd / "output_frames")

if __name__ == "__main__":
    # Ask user for file paths
    target_gif = pick_file(str(cwd), [".gif"], "Left gif")
    right_image = pick_file(str(cwd), [".png", ".jpg"], "Right image")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")

    output_gif = str(cwd / f"{output_filename}.gif")

    # Remove existing folders
    clear_folder(input_frames_path, "Clearing input frames folder")
    clear_folder(output_frames_path, "Clearing output frames folder")

    # Split the gif into individual frames
    print_header(2, "Splitting gif into individual frames")
    os.system(f"ffmpeg -i \"{target_gif}\" \"{input_frames_path}/frame_%d.png\"")

    # Join each frame with the image to the right
    print_header(2, "Joining each frame with the image to the right")

    processes: list[subprocess.Popen[bytes]] = []
    for filename in os.listdir(input_frames_path):
        print_header(3, f"Joining {filename}")

        process = subprocess.Popen(f"ffmpeg -i \"{input_frames_path}/{filename}\" -i \"{right_image}\" -filter_complex hstack -y \"{output_frames_path}/{filename}\"")
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.wait()

    # Join the frames into a gif
    print_header(2, "Joining the frames into a gif")
    os.system(f"ffmpeg -f image2 -i \"{output_frames_path}/frame_%d.png\" \"{output_gif}\"")
