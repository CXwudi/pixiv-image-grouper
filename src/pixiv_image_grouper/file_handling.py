import logging
import os
from os import DirEntry
from pixiv_image_grouper.logging_config import get_logger

log: logging.Logger = get_logger(__name__)


def move_to_year_folder(current_dir: str, entry: DirEntry, year: str) -> None:
    log.info("moving file %s to folder %s", entry.name, year)
    # create the year folder if not exists
    year_folder: str = f"{current_dir}/{year}"
    if not os.path.exists(year_folder):
        os.mkdir(year_folder)
    # move the file to the year folder
    os.rename(entry.path, f"{year_folder}/{entry.name}")
    log.info("file %s moved to folder %s", entry.name, year)
