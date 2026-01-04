# Pixiv Image Grouper

Opinionated tool to group images from Pixiv or other sources into folders.

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just) (for development)

## Installation

```bash
# Install dependencies
uv sync

# Build executable
just build-exe
```

## Development

```bash
just test       # Run tests
just typecheck  # Type check with ty
just lint       # Lint with ruff
just format     # Format with ruff
```

## Usage

Move the executable from `dist/pixiv-image-grouper/` to the folder where you want to group the images and run it.

Then all images will be grouped into folders by their years.

Year info is extracted either from Pixiv id from the filename or the last modified date of the file.
