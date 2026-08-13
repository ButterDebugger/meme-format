import subprocess
import sys
from pathlib import Path

# Allow imports from parent directory
cwd = Path(__file__).parent
sys.path.insert(0, str(cwd.parent))

from utils.prompts import ask_for_string, pick_file
from utils.text import print_header

# Program entry point
if __name__ == "__main__":
    # Ask for the input mp4
    media_file = pick_file(str(cwd), [".mp4", ".mov"])

    # Ask for the start time and duration
    print_header(2, "Clip information")
    start_time = ask_for_string("Start time", "00:00:00")
    duration = ask_for_string("Clip duration", "")
    output_file = ask_for_string("Output file name", "output")

    # Extract clip
    print_header(2, "Extracting clip")
    if duration == "":
        subprocess.run([
            "ffmpeg", "-ss", start_time, "-i", media_file, "-c:a", "copy", f"{output_file}.mp4"
        ])
    else:
        subprocess.run([
            "ffmpeg", "-ss", start_time, "-i", media_file, "-t", duration, "-c:a", "copy", f"{output_file}.mp4"
        ])
