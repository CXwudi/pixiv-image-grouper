import unittest

from .extract_pixiv_id import get_pixiv_id_from_filename

input_results = [
    ("12345678_p0.jpg", 12345678),
    ("pixiv26749967_0.jpg", 26749967),
    ("pid-38184560.jpg", 38184560),
    ("not_a_pixiv_id.jpg", -1),
]


class TestExtractPixivId(unittest.TestCase):
    def test_match(self):
        for input_result in input_results:
            result = get_pixiv_id_from_filename(input_result[0])
            print(result)
            self.assertEqual(result, input_result[1])


if __name__ == "__main__":
    unittest.main()
