import logging
import os
from os import DirEntry

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def move_to_year_folder(current_dir: str, entry: DirEntry, year: str) -> None:
    log.info(f"moving file {entry.name} to folder {year}")
    # create the year folder if not exists
    year_folder: str = f"{current_dir}/{year}"
    if not os.path.exists(year_folder):
        os.mkdir(year_folder)
    # move the file to the year folder
    os.rename(entry.path, f"{year_folder}/{entry.name}")
    log.info(f"file {entry.name} moved to folder {year}")
