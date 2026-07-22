# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Legato 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

The recommender predicts which songs in the catalog a user will like best by scoring each one on how closely its genre, mood, and audio features match the user's stated taste profile, then suggesting the top-ranked matches.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Each song earns points for matching the user's favorite genre and mood, plus extra points the closer its energy, tempo, valence, danceability, and acousticness are to what the user prefers, and the songs with the most points are recommended first.
---

## 4. Data  

Describe the dataset the model uses.  

The dataset is a small, hand-crafted catalog each labeled with genre (pop, rock, lofi, hip hop, trap, rap, edm, and more), mood, and five numeric audio features (energy, tempo, valence, danceability, acousticness).
---

## 5. Strengths  

Where does your system seem to work well  

It works best when a user's profile closely matches an existing song's genre, mood, and numeric feel—like the pop/happy or edm/euphoric tests, where the correct song reliably scored highest with clear reasons.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

It needs more fine tuning and larger data set to learn from and can be tricked easily.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Works fine as expected for proof of concept.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Next steps would be to make feature weights configurable (or learned) instead of fixed, add diversity so top-k isn't all near-duplicates, and expand the catalog with more genres/moods to reduce overfitting to a tiny dataset.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Learned a lot about defining a problem and discovering context and then designing a system before implementation and then evaluating and how it all works together.  
