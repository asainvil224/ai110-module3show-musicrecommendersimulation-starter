from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

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

    def _score_song(self, user: UserProfile, song: Song) -> float:
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 1.0
        if song.mood == user.favorite_mood:
            score += 1.0
        score += 1 - abs(song.energy - user.target_energy)
        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += 1 - song.acousticness
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [(song, self._score_song(user, song)) for song in self.songs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite {user.favorite_genre} genre")
        if song.mood == user.favorite_mood:
            reasons.append(f"matches your favorite {user.favorite_mood} mood")
        energy_diff = abs(song.energy - user.target_energy)
        reasons.append(f"energy level is {1 - energy_diff:.2f} similar to your target")
        if user.likes_acoustic:
            reasons.append(f"has {song.acousticness:.2f} acousticness, which you like")
        else:
            reasons.append(f"has low acousticness ({song.acousticness:.2f}), matching your preference")
        return "This song " + ", ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numerical fields
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    feature_ranges = {
        'energy': (0, 1),
        'valence': (0, 1),
        'tempo_bpm': (60, 180),
        'danceability': (0, 1),
        'acousticness': (0, 1)
    }
    score = 0.0
    reasons = []
    if 'genre' in user_prefs and song['genre'] == user_prefs['genre']:
        score += 1.0
        reasons.append("Genre match")
    if 'mood' in user_prefs and song['mood'] == user_prefs['mood']:
        score += 1.0
        reasons.append("Mood match")
    for feat in ['energy', 'valence', 'tempo_bpm', 'danceability', 'acousticness']:
        if feat in user_prefs:
            target = user_prefs[feat]
            song_val = song[feat]
            min_val, max_val = feature_ranges[feat]
            dist = abs(song_val - target) / (max_val - min_val)
            sim = 1 - dist
            score += sim
            reasons.append(f"{feat} similarity: {sim:.2f}")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
