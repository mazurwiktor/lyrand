import random
import re

from typing import Dict, List, Tuple

from lang import count_syllables, does_rhyme
from track import Track


def pick_random_one(lines: List[str]) -> str:
    return lines[random.randint(0, len(lines) - 1)]


def pick_random_one_dict(d: Dict[str, List[str]]) -> Tuple[str, List[str]]:
    key = random.choice(list(d.keys()))
    return key, d[key]


def shuffle(lines: List) -> List:
    return random.sample(lines, len(lines))


def syllables(lines: List[str], num_syllables: int) -> List[str]:
    filtered = []
    for line in lines:
        if sum([count_syllables(w) for w in re.findall(r"\w+", line)]) == num_syllables:
            filtered.append(line)
    return filtered


def _without(index, l):
    return l[:index] + l[index+1:]


def rhymes(tracks: List[Track], limit=10):
    """ Given
        `tracks`, which is a list of lists of lines in track
       returns
        list of dicts, wherein key is a line from specific track, and value is a list of lines that
        come from any other track and rhyme."""

    def without(index: int, l: List) -> List:
        return l[:index] + l[index + 1:]

    matches = []
    for t, track in enumerate(tracks):
        print(f"processing track {t+1}/{len(tracks)}")
        matches_in_track = {}
        for l, line in enumerate(track.lyrics):
            line_matches = []
            for wtrack in without(t, tracks):
                rhyme_ctr = 0
                for wline in wtrack.lyrics:
                    if does_rhyme(line, wline):
                        line_matches.append(wline)
                        rhyme_ctr += 1
                    if limit and rhyme_ctr >= limit:
                        break
            if line_matches:
                matches_in_track[line] = line_matches
        if matches_in_track:
            matches.append(matches_in_track)
    return matches
