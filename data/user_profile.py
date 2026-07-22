# Example "taste profile" following the User Taste Profile fields
# described in docs/understand_problem.md. This is a broader,
# conceptual profile (not the same as the UserProfile dataclass in
# src/recommender.py) meant as reference/sample data for that section.

TASTE_PROFILE = {
    "favorite_genres": ["hip hop", "edm"],
    "favorite_artists": ["Voltage Fox", "808 Mirage"],
    "preferred_tempo_range": (90, 130),
    "preferred_moods": ["hype", "confident"],
    "average_listening_time": 45,  # minutes per day
    "recently_played_songs": [12, 14, 18],  # Song ids from data/songs.csv
    "frequently_skipped_genres": ["jazz", "ambient"],
}
