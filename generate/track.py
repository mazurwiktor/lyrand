from dataclasses import dataclass
from typing import List


@dataclass
class Track:
    artist: str
    title: str
    lyrics: List[str]
