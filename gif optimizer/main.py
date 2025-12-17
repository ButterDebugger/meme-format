import os
import sys
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_int, ask_for_string, pick_file
from utils.text import print_header

frames_path = str(cwd / "frames")

if __name__ == "__main__":
    # Ask user for file paths
    target_gif = pick_file(str(cwd), [".gif"], "Gif to optimize")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "optimized")
    new_width = ask_for_int("New width", 320)
    max_colors = ask_for_int("Max colors", 256)

    output_gif = str(cwd / f"{output_filename}.gif")

    # Optimize the gif
    print_header(2, "Optimizing the gif")
    os.system(f"ffmpeg -y -i \"{target_gif}\" -filter_complex \"scale={new_width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors={max_colors}[p];[s1][p]paletteuse=dither=bayer\" \"{output_gif}\"")
