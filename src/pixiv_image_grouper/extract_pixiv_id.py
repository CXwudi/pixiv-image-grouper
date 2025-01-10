import re
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

normal_match = re.compile(r"(\d{6,10})_p\d{1,3}")
pid_variant_match = re.compile(r"pid-(\d{6,10})")
pixiv_prefix_variant_match = re.compile(r"pixiv(\d{6,10})")

all_matchers = [normal_match, pid_variant_match, pixiv_prefix_variant_match]


def get_pixiv_id_from_filename(filename: str):
    for matcher in all_matchers:
        log.debug(f"trying matcher {matcher} on filename {filename}")
        match_result = matcher.search(filename)
        if match_result:
            return int(match_result.group(1))
    return -1
