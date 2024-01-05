# Pixiv Image Grouper

Opinionated tool to group images from Pixiv or other sources into folders.

## Prerequisites

- Python 3.6+

## Installation

```bash
python3 -m venv .venvs/
.venvs/bin/python -m pip install -r requirements.txt

pyinstaller --onefile --name pixiv-image-grouper main.py
```

## Usage

Move the executable to the folder where you want to group the images and run it

Then all images will be grouped into folders by their years.

Year info is extracted either from Pixiv id from the filename or the last modified date of the file.