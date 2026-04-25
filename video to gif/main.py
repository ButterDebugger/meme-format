import subprocess
import sys
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_int, ask_for_string, pick_file
from utils.text import print_header

if __name__ == "__main__":
    # Ask user for target video
    target_video = str(pick_file(str(cwd), [".mp4", ".mov"], "Target video"))

    # Ask user for output options
    print_header(2, "Output options")
    output_filename = ask_for_string("Output file name", "output")
    frame_rate = ask_for_int("Frame rate", 24)

    output_gif = str(cwd / f"{output_filename}.gif")
    output_palette = str(cwd / "palette.png")

    # Convert to gif
    print_header(2, "Converting to gif")

    # Build the command
    filter_complex = f"[0:v] fps={frame_rate},split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1"
    command = [
        "ffmpeg",
        "-i", target_video,
        "-y",
        "-filter_complex", filter_complex,
        output_gif
    ]

    # Execute the command
    subprocess.run(command, check=True)
