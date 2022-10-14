import streamlit as st
import pandas as pd
import pickle as pk
import requests

def recommend(movie):
    ind=movies[movies.title_x==selected_movie].index[0]
    similarity=similiartity_matrix[ind]
    x=sorted(list(enumerate(similarity)),reverse=True,key=lambda x:x[1])[1:6]
    starting_url='https://image.tmdb.org/t/p/original'
    l=[]
    for i in x:
        movie_id=movies.iloc[i[0]].movie_id
        title=movies.iloc[i[0]].title_x
        end_url=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=59ee842fadafaf3662e17c8b66870be9&language=en-US').json()['poster_path']
        if end_url:
            poster_url=starting_url+end_url
        else:
            poster_url='https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg'
        l.append((title,poster_url))
    return l

st.title('Movie Recommendation System')

movies=pd.DataFrame(pk.load(open('movies.pkl','rb')))
similiartity_matrix=pk.load(open('similiarity_matrix.pkl','rb'))

movies_list=movies['title_x']

selected_movie = st.selectbox(
    'Select a Movie for recommendation',
    movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.text(recommendations[0][0])
        st.image(recommendations[0][1])
    with col2:
        st.text(recommendations[1][0])
        st.image(recommendations[1][1])
    with col3:
        st.text(recommendations[2][0])
        st.image(recommendations[2][1])
    with col4:
        st.text(recommendations[3][0])
        st.image(recommendations[3][1])
    with col5:
        st.text(recommendations[4][0])
        st.image(recommendations[4][1])