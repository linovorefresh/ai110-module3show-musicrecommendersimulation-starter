import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a songs CSV into a list of dicts with numeric fields converted to int/float."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

# Point values for each scoring signal, chosen so genre (the strongest,
# most explicit taste signal) outweighs mood, which in turn outweighs any
# single numeric audio feature. Numeric features are scored on a sliding
# scale up to this max rather than all-or-nothing, since closeness matters.
GENRE_MATCH_POINTS = 2.0
MOOD_MATCH_POINTS = 1.5
NUMERIC_FEATURE_MAX_POINTS = 1.0

# tempo_bpm lives on a ~60-200 scale while the other numeric features are
# already 0-1, so its raw difference is divided by this range before being
# treated as a 0-1 similarity like the rest.
TEMPO_NORMALIZATION_RANGE = 100.0

NUMERIC_FEATURES = ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences, returning (total score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    if "genre" in user_prefs and user_prefs["genre"] == song.get("genre"):
        score += GENRE_MATCH_POINTS
        reasons.append(f"genre match (+{GENRE_MATCH_POINTS:.1f})")

    if "mood" in user_prefs and user_prefs["mood"] == song.get("mood"):
        score += MOOD_MATCH_POINTS
        reasons.append(f"mood match (+{MOOD_MATCH_POINTS:.1f})")

    for feature in NUMERIC_FEATURES:
        if feature not in user_prefs or feature not in song:
            continue
        diff = abs(float(song[feature]) - float(user_prefs[feature]))
        if feature == "tempo_bpm":
            diff = diff / TEMPO_NORMALIZATION_RANGE
        similarity = max(0.0, 1.0 - diff)
        points = similarity * NUMERIC_FEATURE_MAX_POINTS
        score += points
        reasons.append(f"{feature} similarity (+{points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, ranked highest to lowest."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong matches"
        scored.append((song, score, explanation))

    scored.sort(key=lambda entry: entry[1], reverse=True)
    return scored[:k]
