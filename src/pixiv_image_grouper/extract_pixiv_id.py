import re
import logging
from typing import List, Pattern, Optional

log: logging.Logger = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

normal_match: Pattern[str] = re.compile(r"(\d{6,10})_p\d{1,3}")
pid_variant_match: Pattern[str] = re.compile(r"pid-(\d{6,10})")
pixiv_prefix_variant_match: Pattern[str] = re.compile(r"pixiv(\d{6,10})")

all_matchers: List[Pattern[str]] = [normal_match, pid_variant_match, pixiv_prefix_variant_match]


def get_pixiv_id_from_filename(filename: str) -> int:
    for matcher in all_matchers:
        log.debug(f"trying matcher {matcher} on filename {filename}")
        match_result: Optional[re.Match[str]] = matcher.search(filename)
        if match_result:
            return int(match_result.group(1))
    return -1
