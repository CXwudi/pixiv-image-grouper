from os import DirEntry
import sys
import logging
from PIL import Image
from pixiv_image_grouper.logging_config import get_logger

log: logging.Logger = get_logger(__name__)


def is_image(file: DirEntry[str]) -> bool:
    try:
        with Image.open(file.path) as im:
            log.debug("file %s is an image with format %s", file, im.format)
        return True
    except IOError:
        log.error(
            "file %s is not an image, or can not open the file, %s", file, sys.exc_info()[0]
        )
        return False
