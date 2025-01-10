# Pixiv Image Grouper

Opinionated tool to group images from Pixiv or other sources into folders.

## Prerequisites

- Python 3.8+

## Installation

Using uv (recommended):

```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix

# Install package with development dependencies
uv pip install -e ".[dev]"

# Build executable
pyinstaller src/pixiv_image_grouper/main.py --name pixiv-image-grouper
```

## Usage

Move the executable from `dist/pixiv-image-grouper/` to the folder where you want to group the images and run it.

Then all images will be grouped into folders by their years.

Year info is extracted either from Pixiv id from the filename or the last modified date of the file.
