import os
import sys
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_int, ask_for_string, pick_file
from utils.text import print_header

if __name__ == "__main__":
    # Ask user for target video
    target_video = pick_file(str(cwd), [".mp4", ".mov"], "Target video")

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")
    frame_rate = ask_for_int("Frame rate", 24)

    output_gif = str(cwd / f"{output_filename}.gif")
    output_palette = str(cwd / "palette.png")

    # Convert to gif
    print_header(2, "Converting to gif")
    os.system(f"ffmpeg -i \"{target_video}\" -y -r {frame_rate} -filter_complex \"[0:v] split [a][b];[a] palettegen [p];[b][p] paletteuse=dither=none\" \"{output_gif}\"")
