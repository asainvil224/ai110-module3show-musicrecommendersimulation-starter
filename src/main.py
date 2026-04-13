"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


# Define distinct user preference profiles
USER_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "valence": 0.85,
        "tempo_bpm": 125,
        "danceability": 0.85,
        "acousticness": 0.1
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "valence": 0.6,
        "tempo_bpm": 80,
        "danceability": 0.5,
        "acousticness": 0.8
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "valence": 0.5,
        "tempo_bpm": 140,
        "danceability": 0.65,
        "acousticness": 0.1
    }
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Test each user profile
    for profile_name, user_prefs in USER_PROFILES.items():
        print(f"\n{'='*60}")
        print(f"Profile: {profile_name}")
        print(f"{'='*60}\n")
        
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"Top recommendations for {profile_name}:\n")
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")
            print()



if __name__ == "__main__":
    main()
