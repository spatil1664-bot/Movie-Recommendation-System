import streamlit as st
import pandas as pd
import pickle

# Load data
movies = pd.read_csv("cleaned_data.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'].str.lower() == movie.lower()].index[0]

    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

# Streamlit UI
st.title("🎬 Movie Recommendation System")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("✅", movie)
