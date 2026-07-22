# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CodePath (AI110, Module 3) classroom assignment: a small, educational **content-based music recommender simulation**. The goal is not production ML but demonstrating, in plain Python, how song attributes + a user taste profile turn into ranked recommendations with a human-readable explanation. Most of the actual logic is currently unimplemented `TODO` stubs — see `src/recommender.py`.

## Commands

```bash
pip install -r requirements.txt   # deps: pandas, pytest, streamlit

pytest                             # run all tests
pytest tests/test_recommender.py -k test_recommend_returns_songs_sorted_by_score  # single test

python -m src.main                 # run the CLI demo (per README)
```

Note: `src/main.py` itself imports with `from recommender import load_songs, recommend_songs` (no `src.` prefix), which only resolves if run as `cd src && python main.py`. If `python -m src.main` fails with an import error, that inconsistency is the cause — fix the import in `main.py` (`from src.recommender import ...`) rather than changing how it's invoked, to stay consistent with the tests' import style.

## Architecture

The recommendation logic exists in **two parallel, redundant forms** in `src/recommender.py` — both need to be implemented, and they should agree conceptually since they encode the same scoring rules:

1. **OOP path** (used by `tests/test_recommender.py`): `Song` and `UserProfile` dataclasses, plus a `Recommender` class with `recommend(user, k)` and `explain_recommendation(user, song)`.
2. **Functional path** (used by `src/main.py`): `load_songs(csv_path)` reads `data/songs.csv` into dicts, `score_song(user_prefs, song)` returns `(score, reasons)`, and `recommend_songs(user_prefs, songs, k)` returns a ranked list of `(song_dict, score, explanation)`.

Both are currently placeholders returning empty/unsorted data — implementing the scoring algorithm is the core task of this assignment.

### Scoring algorithm (see `docs/logic_mapping.md` for full detail)

The design is **similarity-based, not magnitude-based**: a song scores higher the *closer* its attributes are to the user's preferred values, not simply for being higher or lower.

- Numeric features (`energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`): compute `abs(song_value - user_preference)`, then convert that difference into a similarity score in `[0, 1]` (smaller difference → higher similarity — exact formula is left to the implementer, e.g. `1 - normalized_diff`).
- Categorical features (`genre`, `mood`): score by equality (full match vs. no match), compared against `UserProfile.favorite_genre` / `favorite_mood`.
- Combine per-feature scores (the starter recipe averages them equally; weighting is called out as a later enhancement, not part of the initial implementation).
- Rank all songs by overall score, descending, and return the top `k`.
- `tempo_bpm` has a much larger numeric range than the other (already 0–1 normalized) features and should be normalized before comparing.

`docs/understand_problem.md` is background reading (collaborative vs. content-based filtering) rather than an implementation spec — useful for the reflection/model-card writeup, not for code structure.

### Data

`data/songs.csv` — small fixed catalog (10 songs) with columns matching the `Song` dataclass fields exactly: `id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness`.

### Deliverables beyond code

This assignment also expects narrative writeups, not just working code:
- `README.md` — fill in system description, sample output, experiments, limitations (currently template placeholders).
- `model_card.md` — fill in intended use, data, strengths/limitations/bias, evaluation, reflection (currently template placeholders).
- `ai_interactions.md` — only relevant if attempting stretch features (agentic workflow, design pattern); leave blank otherwise.
