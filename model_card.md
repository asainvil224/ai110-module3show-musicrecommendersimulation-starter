# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

MelodyMatch

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The recommender recommends songs based on your preference. The recommender assumes users have clear preferences for specific genres and that their tastes align with the available song features like energy, mood, and tempo. This is primarily for classroom exploration and educational purposes.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model uses song features like genre, energy level, mood, and tempo to match against user preferences. It considers what genres the user likes, their preferred energy, mood, and tempo. To create a score, it calculates a similarity match by comparing each song's features to the user's inputs, assigning higher scores for closer matches and summing them up for a total recommendation score. From the starter logic, I modified the scoring to weight genre more heavily and added a penalty for mismatched moods to improve accuracy.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains approximately 17 songs, covering genres like pop, rock, jazz, hip-hop, classical, and electronic, with moods including upbeat, calm, energetic, melancholic, and neutral. I did add more songs to add variety to the dataset. Missing elements include artist-specific details, lyrical content, release dates, cultural influences, and user interaction history, which could enhance the model's understanding of musical taste.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear genre preferences, such as those who consistently favor rock or jazz music. The scoring accurately captures patterns where songs with matching genres and aligned moods receive higher scores, resulting in recommendations that feel intuitive. For example, when a user prefers energetic pop music, the model reliably recommends upbeat pop tracks with high energy levels, matching what you would expect. Additionally, the weighted genre emphasis combined with the mood penalty ensures that recommendations respect both primary preferences and secondary mood constraints, leading to results that align with user intuition in straightforward cases.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system struggles with users who have diverse or evolving tastes, as it does not consider features like artist popularity, lyrical themes, or contextual listening situations. Certain genres and moods may be underrepresented in the dataset, causing the model to provide limited recommendations for users with preferences outside the well-represented categories. The system can overfit to a single strong preference, such as heavily weighting genre matching, which may cause it to ignore users who value mood or tempo equally. Additionally, the scoring might unintentionally favor users whose preferences align closely with the majority of songs in the catalog, while disadvantaging those with niche or unconventional tastes that fall outside the typical feature patterns.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender with three distinct user profiles: "High-Energy Pop," "Chill Lofi," and "Deep Intense Rock." The High-Energy Pop profile prioritizes upbeat, danceable pop music with high energy and valence, the Chill Lofi profile seeks relaxing, acoustic lofi tracks with low energy, and the Deep Intense Rock profile targets intense, high-energy rock music. When examining the recommendations, I looked for whether the top five songs matched the specified genre, had appropriate energy and mood levels, and whether the explanation text accurately described why each song was recommended. What surprised me was how well the recommender distinguished between these contrasting profiles—songs for the Chill Lofi profile had significantly lower energy and tempo scores compared to the High-Energy Pop profile, demonstrating that the scoring properly captured different preference dimensions. I ran simple tests by comparing the recommendations across profiles to ensure they produced different results, and I verified that the scoring logic correctly weighted genre and mood features to generate the expected rankings for each distinct user type.



## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

To improve the model next, I would incorporate additional features such as artist popularity, release year, and instrumentation to provide richer context for recommendations. I would also implement better explanations by showing users exactly which features matched their preferences, helping them understand why a song was recommended. To improve diversity among top results, I would add a penalty mechanism that reduces scores for songs too similar to already-recommended tracks, ensuring variety in the final list. For handling more complex user tastes, I would introduce support for weighted preference profiles that allow users to specify how much they value genre versus mood versus tempo, and implement collaborative filtering techniques to learn from patterns in how users with similar tastes rate songs over time.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems are very complex and require good design. It was interesting how the recommender used certain algorithms behind the scenes to calculate the user's preference. It made think how each website I visit, it continuously keep track of my data to feed into the recommendation system.

