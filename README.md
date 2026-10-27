# Meme format

A collection of scripts that allow you to create GIFs locally on your computer.

## Requirements

- [FFmpeg](https://ffmpeg.org/download.html)
- [UV](https://docs.astral.sh/uv/)
- Python 3.12+

## Getting started

```sh
git clone https://github.com/ButterDebugger/meme-format.git
cd meme-format
uv sync
```

## Usage

Place your source files into `input_media/`, then run a script.

Results are saved to `output_media/`.

| Command               | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| `uv run crossfade`    | Crossfade between two images                                           |
| `uv run extract_clip` | Extract a section from a video into its own file                       |
| `uv run left_right`   | Create a left-right split between two images                           |
| `uv run optimize`     | Reduce the file size of a GIF (Recommended before uploading elsewhere) |
| `uv run video_to_gif` | Convert a video into a GIF                                             |
