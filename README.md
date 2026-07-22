# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders


Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders like Spotify's or Netflix's typically blend two ideas: **collaborative filtering**, which recommends things based on what similar *users* liked, and **content-based filtering**, which recommends things based on how similar an *item* is to what a user already prefers. Collaborative filtering can surface surprising discoveries but needs lots of user history to work and struggles with brand-new users or songs (the "cold start" problem). This project only implements the content-based half: instead of learning from other listeners, it compares each song's own attributes directly against one user's stated taste profile. That tradeoff means every recommendation is easy to explain (traceable to specific feature matches) and works even with a single user and a tiny catalog, but it also means the system will keep recommending "more of the same" and can never suggest something outside a user's declared preferences.

This version prioritizes **similarity over magnitude** — a song is not scored higher just because it has more energy or a faster tempo, only because its values sit *closer* to what the user asked for. Categorical traits (genre, mood) are scored as a match or non-match, while numeric traits (energy, tempo, valence, danceability, acousticness) are scored by how small the difference is between the song's value and the user's target value. All feature scores are combined into one overall score per song, and the catalog is ranked from closest match to furthest.

**Song** features used in scoring:
- `genre` (categorical match)
- `mood` (categorical match)
- `energy` (numeric closeness)
- `tempo_bpm` (numeric closeness, normalized before comparing since it has a much larger range than the other 0–1 features)
- `valence` (numeric closeness)
- `danceability` (numeric closeness)
- `acousticness` (numeric closeness)

**UserProfile** information used as the comparison target:
- `favorite_genre` — matched against each song's `genre`
- `favorite_mood` — matched against each song's `mood`
- `target_energy` — the preferred energy level a song's `energy` is compared to
- `likes_acoustic` — a preference signal used alongside `acousticness` closeness

The `Recommender` scores every song against these targets, combines the per-feature similarity scores into a single overall score, sorts songs from highest to lowest, and returns the top `k` as the recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Ran with the starter profile from `src/main.py` (`{"genre": "pop", "mood": "happy", "energy": 0.8}`) against the current `data/songs.csv` catalog:

```
Top recommendations:

Sunrise City - Score: 4.48
Because: genre match (+2.0), mood match (+1.5), energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy similarity (+0.87)

Rooftop Lights - Score: 2.46
Because: mood match (+1.5), energy similarity (+0.96)

Concrete Kingdom - Score: 0.98
Because: energy similarity (+0.98)

Corner Store Legend - Score: 0.95
Because: energy similarity (+0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



