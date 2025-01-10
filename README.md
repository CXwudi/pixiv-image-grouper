# Pixiv Image Grouper

Opinionated tool to group images from Pixiv or other sources into folders.

## Prerequisites

- uv

## Installation

```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix

# Install package with development dependencies
uv pip install -e ".[dev]"

# Build executable
hatch run build-exe
```

## Testing

```bash
# Run unit tests
hatch run test
```

## Usage

Move the executable from `dist/pixiv-image-grouper/` to the folder where you want to group the images and run it.

Then all images will be grouped into folders by their years.

Year info is extracted either from Pixiv id from the filename or the last modified date of the file.
