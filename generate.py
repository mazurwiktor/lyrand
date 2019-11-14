from typing import List

import filters


def newline2list(raw_str: str) -> List[str]:
    return list(filter(None, raw_str.split("\n")))


def line_per_track(tracks: List[str]) -> List[str]:
    """Takes only one, randomly chosen line from each track."""
    tracks = filters.shuffle(tracks)
    return [filters.pick_random_one(newline2list(track)) for track in tracks]


def line_per_track_syllables(tracks: List[str], syllables: int) -> List[str]:
    """Filters lines that have given number of syllables, and takes randomly chosen
    one from each track."""
    matching = []
    for track in tracks:
        matching_in_track = filters.syllables(newline2list(track), syllables)
        if matching_in_track:
            matching.append(filters.pick_random_one(matching_in_track))
    matching = filters.shuffle(matching)
    return matching
