import pytest
from typing import List, Tuple
from pixiv_image_grouper.extract_pixiv_id import get_pixiv_id_from_filename

test_cases: List[Tuple[str, int]] = [
    ("12345678_p0.jpg", 12345678),
    ("pixiv26749967_0.jpg", 26749967),
    ("pid-38184560.jpg", 38184560),
    ("not_a_pixiv_id.jpg", -1),
]


@pytest.mark.parametrize("filename,expected", test_cases)
def test_pixiv_id_extraction(filename: str, expected: int) -> None:
    result: int = get_pixiv_id_from_filename(filename)
    assert result == expected
