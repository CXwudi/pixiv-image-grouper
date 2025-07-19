import os
import logging

from pixiv_image_grouper.check_image import is_image
from pixiv_image_grouper.get_year import get_year
from pixiv_image_grouper.file_handling import move_to_year_folder
from pixiv_image_grouper.logging_config import setup_logging, get_logger

log: logging.Logger = get_logger(__name__)


def main() -> None:
    setup_logging()
    # get the current directory
    current_dir: str = os.getcwd()
    log.info("working on current directory %s", current_dir)

    # walk the image files in the current directory
    with os.scandir(current_dir) as it:
        for entry in it:
            if not entry.name.startswith(".") and entry.is_file() and is_image(entry):
                log.info("processing file %s", entry.name)
                year: str = get_year(entry)
                move_to_year_folder(current_dir, entry, year)

        it.close()
    log.info("(*^▽^*) all done!")


main()
