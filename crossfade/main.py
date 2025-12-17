import os
import sys
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_string, clear_folder, pick_file
from utils.text import print_header

frames_path = str(cwd / "frames")

if __name__ == "__main__":
    # Ask user for file paths
    first_image = pick_file(str(cwd), [".png", ".jpg"], "First image")
    second_image = pick_file(str(cwd), [".png", ".jpg"], "Second image")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")

    output_gif = str(cwd / f"{output_filename}.gif")

    # Clear the frames folder
    clear_folder(frames_path, "Clearing frames folder")

    # Create the frames
    print_header(2, "Creating frames")
    os.system(f"ffmpeg -loop 1 -i \"{first_image}\" -loop 1 -i \"{second_image}\" -filter_complex \"[1:v][0:v]blend=all_expr='A*(if(gte(T,3),1,T/3))+B*(1-(if(gte(T,3),1,T/3)))'\" -t 4 \"{frames_path}/image_%d.png\"")

    # Join the frames into a gif
    print_header(2, "Joining the frames into a gif")
    os.system(f"ffmpeg -f image2 -i \"{frames_path}/image_%d.png\" \"{output_gif}\"")
