from os import DirEntry
import sys
import logging
from datetime import datetime
from .extract_pixiv_id import get_pixiv_id_from_filename
from .constant import all_ranges

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

id_not_found_str = "id not found"
before2018_str = "2007 - 2017"


def get_year(entry: DirEntry) -> str:
    year_from_lm = get_year_from_last_modified(entry)
    year_from_pixiv_id = try_get_year_from_pixiv_id(entry)
    if year_from_pixiv_id == id_not_found_str:
        log.info(
            f"can not find pixiv id from filename {entry.name}, use last modified year {year_from_lm}"
        )
        return year_from_lm
    else:
        log.info(f"using year {year_from_pixiv_id} from pixiv id")
        return year_from_pixiv_id


def get_year_from_last_modified(entry: DirEntry) -> str:
    stat_result = entry.stat()
    timestamp = datetime.fromtimestamp(stat_result.st_mtime)
    if timestamp.year <= 2017:
        return before2018_str
    else:
        return str(timestamp.year)


def try_get_year_from_pixiv_id(entry: DirEntry) -> str:
    pixiv_id = get_pixiv_id_from_filename(entry.name)
    if pixiv_id == -1:
        return id_not_found_str
    log.info(f"found pixiv id {pixiv_id} from filename {entry.name}")
    # the first range is special, covers 2007 - 2017
    if pixiv_id < all_ranges[0][1]:
        log.debug(f"pixiv id {pixiv_id} is before 2018")
        return before2018_str
    # then handle the rest of the ranges
    for year, id_barrier in all_ranges[1:]:
        if pixiv_id < id_barrier:
            log.debug(f"pixiv id {pixiv_id} is in {year}")
            return str(year)
    # however, if the pixiv id is larger than the last range, it is in current year
    if pixiv_id > all_ranges[-1][1]:
        log.debug(f"pixiv id {pixiv_id} is in current year")
        return datetime.now().year
    raise InvalidPixivIdError(
        f"pixiv id {pixiv_id} from filename {entry.name} is not in any range"
    )


class InvalidPixivIdError(Exception):
    pass
