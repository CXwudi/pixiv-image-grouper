from os import DirEntry
import sys
import logging
from datetime import datetime
from pixiv_image_grouper.extract_pixiv_id import get_pixiv_id_from_filename
from pixiv_image_grouper.constant import all_ranges
from pixiv_image_grouper.logging_config import get_logger

log: logging.Logger = get_logger(__name__)

id_not_found_str: str = "id not found"
before2018_str: str = "2007 - 2017"


def get_year(entry: DirEntry[str]) -> str:
    year_from_lm: str = get_year_from_last_modified(entry)
    year_from_pixiv_id: str = try_get_year_from_pixiv_id(entry)
    if year_from_pixiv_id == id_not_found_str:
        log.info(
            "can not find pixiv id from filename %s, use last modified year %s", entry.name, year_from_lm
        )
        return year_from_lm
    else:
        log.info("using year %s from pixiv id", year_from_pixiv_id)
        return year_from_pixiv_id


def get_year_from_last_modified(entry: DirEntry[str]) -> str:
    stat_result = entry.stat()
    timestamp: datetime = datetime.fromtimestamp(stat_result.st_mtime)
    if timestamp.year <= 2017:
        return before2018_str
    else:
        return str(timestamp.year)


def try_get_year_from_pixiv_id(entry: DirEntry[str]) -> str:
    pixiv_id: int = get_pixiv_id_from_filename(entry.name)
    if pixiv_id == -1:
        return id_not_found_str
    log.info("found pixiv id %s from filename %s", pixiv_id, entry.name)
    # the first range is special, covers 2007 - 2017
    if pixiv_id < all_ranges[0][1]:
        log.debug("pixiv id %s is before 2018", pixiv_id)
        return before2018_str
    # then handle the rest of the ranges
    for year, id_barrier in all_ranges[1:]:
        if (
            pixiv_id <= id_barrier
        ):  # including the id_barrier, the id_barrier should be the last day of the year
            log.debug("pixiv id %s is in %s", pixiv_id, year)
            return str(year)
    # however, if the pixiv id is larger than the last range, it is in current year
    if pixiv_id > all_ranges[-1][1]:
        log.debug("pixiv id %s is in current year", pixiv_id)
        return str(datetime.now().year)
    raise InvalidPixivIdError(
        "pixiv id %s from filename %s is not in any range" % (pixiv_id, entry.name)
    )


class InvalidPixivIdError(Exception):
    pass
