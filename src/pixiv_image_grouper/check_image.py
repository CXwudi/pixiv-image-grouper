from os import DirEntry
import sys
import logging
from PIL import Image

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def is_image(file: DirEntry) -> bool:
    try:
        with Image.open(file.path) as im:
            log.debug(f"file {file} is an image with format {im.format}")
        return True
    except IOError:
        log.error(
            f"file {file} is not an image, or can not open the file, {sys.exc_info()[0]}"
        )
        return False
