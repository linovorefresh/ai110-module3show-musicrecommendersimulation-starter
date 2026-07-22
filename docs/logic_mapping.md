# Logic Mapping
## Designing the Recommendation Scoring Rules

## Purpose

A content-based recommender should not reward songs simply because they have **higher** or **lower** values.

Instead, it should reward songs whose attributes are **closest to the user's preferred values**.

For example:

- If a user prefers Energy = 0.80
- A song with Energy = 0.79 should score higher than one with Energy = 0.30.

The objective is **similarity**, not magnitude.

---

# Core Principle

Every numerical feature follows the same idea.

```
Smaller Difference
        ↓
Higher Similarity
        ↓
Higher Recommendation Score
```

The recommendation engine compares each song's value against the user's preferred value.

---

# Step 1 — User Preference

Each user has a preferred value for every numerical feature.

Example Taste Profile

| Feature | Preferred Value |
|----------|----------------:|
| Energy | 0.80 |
| Tempo | 120 BPM |
| Valence | 0.75 |
| Danceability | 0.82 |
| Acousticness | 0.20 |

These values become the target for comparison.

---

# Step 2 — Measure the Difference

For each feature:

Difference = absolute distance between

Song Value

and

User Preference

Example

Preferred Energy

0.80

Song A

0.78

Difference

0.02

Song B

0.55

Difference

0.25

Song C

0.92

Difference

0.12

Smaller difference means the song is more similar.

---

# Step 3 — Convert Difference into Similarity

Raw differences are difficult to compare.

Instead, convert them into a similarity score between

0 and 1.

```
Perfect Match
Difference = 0
Similarity = 1.00
```

As the difference grows,

the similarity decreases toward zero.

Example

| Difference | Similarity |
|------------|-----------:|
| 0.00 | 1.00 |
| 0.05 | 0.95 |
| 0.10 | 0.90 |
| 0.30 | 0.70 |
| 0.60 | 0.40 |

The exact mathematical formula can be chosen later.

The important idea is:

> Smaller distance always produces a larger similarity score.

---

# Logic for Each Numerical Feature

## Energy

Question:

Does the song have a similar energy level?

Example

User Preference

0.80

Song

0.77

Very Similar

High Score

---

## Tempo (BPM)

Question

Is the song played at a similar speed?

Example

Preferred Tempo

120 BPM

Song A

118 BPM

Excellent Match

Song B

70 BPM

Poor Match

Since tempo has a much larger numeric range than other features, it should eventually be normalized before comparison.

---

## Valence

Question

Does the emotional positivity match?

Example

Preferred

0.75

Song

0.73

Very Similar

---

## Danceability

Question

Does the rhythmic feel match?

Example

Preferred

0.82

Song

0.79

Good Match

---

## Acousticness

Question

Does the song have a similar acoustic character?

Example

Preferred

0.20

Song

0.18

Very Similar

---

# Handling Categorical Features

Categorical values cannot be compared using numerical distance.

Instead, compare them by equality.

## Genre

Example

Preferred

Pop

Song Genre

Pop

Score

Full Match

Song Genre

Rock

Score

No Match

---

## Mood

Example

Preferred Mood

Chill

Song Mood

Chill

Full Match

Song Mood

Happy

No Match

---

# Combining All Feature Scores

Each feature produces its own similarity score.

Example

| Feature | Similarity |
|----------|-----------:|
| Genre | 1.00 |
| Mood | 1.00 |
| Energy | 0.94 |
| Tempo | 0.96 |
| Valence | 0.91 |
| Danceability | 0.88 |
| Acousticness | 0.97 |

These individual scores are then combined into a single recommendation score.

Conceptually:

```
Overall Recommendation Score

=

Average of all feature similarity scores
```

Later, the project may assign different weights so some features influence the final score more than others.

---

# Recommended Feature Importance

For the first simulator, treat every feature equally.

| Feature | Importance |
|----------|-----------:|
| Genre | High |
| Mood | High |
| Energy | High |
| Tempo | High |
| Valence | High |
| Danceability | High |
| Acousticness | High |

Once the basic system works, feature weights can be introduced.

Example

Genre might contribute more than Tempo.

Mood might contribute more than Acousticness.

Weighted scoring is considered an enhancement rather than part of the initial implementation.

---

# Algorithm Recipe

For every song in the dataset:

1. Read the user's preferred feature values.
2. Compare each numerical feature with the song's value.
3. Measure how close the values are.
4. Convert closeness into a similarity score.
5. Compare categorical features (Genre and Mood) for matches.
6. Combine all similarity scores into one overall recommendation score.
7. Rank songs from highest score to lowest score.
8. Recommend the highest-ranked songs.

---

# Design Philosophy

This simulator is intentionally simple and educational.

Rather than using advanced machine learning, it demonstrates the central idea behind content-based recommendation:

- Compare the characteristics of a song with a user's taste profile.
- Reward songs that are **closest** to the user's preferences.
- Rank songs by overall similarity.

The recommendation engine is therefore based on **similarity**, not popularity, randomness, or whether a feature value is simply higher or lower.