# prompt: RECOMMENDATION SYSTEM
# Create a simple recommendation system that suggests items to
# users based on their preferences. You can use techniques like
# collaborative filtering or content-based filtering to recommend
# movies, books, or products to users.

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example Dataset (You can replace this with your own data)
data = {
    "User": ["User1", "User2", "User3", "User4", "User5"],
    "Movie_A": [5, 4, 3, np.nan, 2],
    "Movie_B": [4, np.nan, 2, 1, 5],
    "Movie_C": [1, 3, np.nan, 4, 4],
    "Movie_D": [np.nan, 2, 5, 3, 3],
    "Movie_E": [2, 1, 4, np.nan, 5],
}

# Load data into a DataFrame
df = pd.DataFrame(data)
df.set_index("User", inplace=True)

# Fill NaN values with 0 (you can use other strategies like mean imputation)
df_filled = df.fillna(0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(df_filled)
user_similarity_df = pd.DataFrame(user_similarity, index=df.index, columns=df.index)

def recommend_movies(user, num_recommendations=2):
    # Get the similarity scores for the target user
    similarity_scores = user_similarity_df[user].drop(user)  # Exclude the user themself

    # Sort users by similarity score in descending order
    sorted_similarity_scores = similarity_scores.sort_values(ascending=False)

    # Get the top similar users
    top_similar_users = sorted_similarity_scores.index[:3]  # Consider the top 3 similar users


    recommendations = {}
    for movie in df.columns:
        # Calculate a weighted average of ratings from similar users for the movie
        movie_ratings = df.loc[top_similar_users, movie]
        weighted_sum = np.sum(movie_ratings * sorted_similarity_scores.loc[top_similar_users])
        if weighted_sum > 0:  # Check to prevent division by zero
            recommendations[movie] = weighted_sum/np.sum(sorted_similarity_scores.loc[top_similar_users])
        else:
            recommendations[movie] = 0

    # Sort the recommendations in descending order
    sorted_recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))
    # Return the top N recommendations
    return list(sorted_recommendations.keys())[:num_recommendations]

# Example usage: Recommend movies for User1
user = "User1"
recommended_movies = recommend_movies(user)
