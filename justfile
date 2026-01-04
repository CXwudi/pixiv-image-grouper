# Run tests
test:
    uv run pytest tests

# Type check
typecheck:
    uv run ty check src/pixiv_image_grouper tests

# Lint
lint:
    uv run ruff check .

# Format
format:
    uv run ruff format .

# Build executable
build-exe:
    uv run pyinstaller src/pixiv_image_grouper/main.py --name pixiv-image-grouper --onefile
