# all pixiv constant
# constant about ID to year
# always use the last moment of dec 31st of the year
from typing import List, Tuple

before2025: Tuple[int, int] = (2024, 125750247)
before2024: Tuple[int, int] = (2023, 114717469)
before2023: Tuple[int, int] = (2022, 104130000)
before2022: Tuple[int, int] = (2021, 95207000)
before2021: Tuple[int, int] = (2020, 86723000)
before2020: Tuple[int, int] = (2019, 78638500)
before2019: Tuple[int, int] = (2018, 72431010)
before2018: Tuple[int, int] = (2017, 66553410)

all_ranges: List[Tuple[int, int]] = [
    before2018,
    before2019,
    before2020,
    before2021,
    before2022,
    before2023,
    before2024,
    before2025,
]
