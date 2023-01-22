import requests
import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


# https://api.themoviedb.org/3/movie/19995?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&external_source=tvdb_id

def getPosterPathByID(id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&external_source=tvdb_id".format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"];

def getRecommendMoviesAndPosters(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    distance = similarity[movie_index]
    movieList = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[0:6]
    recommend_movies = []
    recommend_movies_poster = []

    for i in movieList:
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(getPosterPathByID(movies.iloc[i[0]].id))

    return recommend_movies, recommend_movies_poster


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Search a movie you like...',
    movies["title"].values)


if st.button("Recommend"):
    moviesNames, moviesPoster = getRecommendMoviesAndPosters(selected_movie_name)
    # st.write(moviesPoster)

    col0, col1, col2, col3, col4 = st.columns(5)

    with col0:
        st.image(moviesPoster[0])
        st.caption(moviesNames[0])

    with col1:
        st.image(moviesPoster[1])
        st.caption(moviesNames[1])

    with col2:
        st.image(moviesPoster[2])
        st.caption(moviesNames[2])

    with col3:
        st.image(moviesPoster[3])
        st.caption(moviesNames[3])

    with col4:
        st.image(moviesPoster[4])
        st.caption(moviesNames[4])


print()

# st.write('You selected:', option)