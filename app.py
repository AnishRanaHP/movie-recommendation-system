import streamlit as st
import pickle
import requests


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)


st.sidebar.title("🎬 Movie Recommender")
st.sidebar.markdown("---")
st.sidebar.header("📌 About the Application")
st.sidebar.write(
    """
    This application is a Movie Recommendation System 
    that helps users discover movies similar to their 
    favorite movies.

    The system uses a content-based recommendation 
    approach and analyzes movie information such as 
    genres, keywords, overview, cast, and crew.

    Machine learning and NLP techniques are used to 
    calculate the similarity between movies and generate 
    relevant recommendations.
    """
)
st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ Technologies")
st.sidebar.write(
    """
    • Python  
    • Pandas & NumPy  
    • NLTK  
    • Scikit-learn  
    • NLP  
    • Cosine Similarity
    """
)
st.sidebar.markdown("---")
st.sidebar.caption("🎥 Built as a Machine Learning Project")




def recommend(movie,n):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:n+1]
    recommended_movie=[]
    for i in movies_list:
        recommended_movie.append(df.iloc[i[0]].title)
    return recommended_movie


df=pickle.load(open('movies.pkl','rb'))


similarity=pickle.load(open('similarity','rb'))
st.title('Movie Recommender System')

select_movie_name=st.selectbox(
    'Enter the movie you want to recommend',
    (df['title'].values)
)

top_n = st.slider(
    "Number of Recommendations",
    1,
    10,
    5
)


if st.button("🎬 Recommend"):

    name = recommend(select_movie_name, top_n)

    st.success(f"Top {top_n} Movie Recommendations!")

    for i, movie in enumerate(name, 1):
        st.write(f"**{i}. {movie}**")


st.markdown("""
<style>

h1 {
    color: orange;
    text-align: center;
}

h2, h3 {
    color: orange;
}


.stButton > button {
    background-color: red;
    color: white;
    border-radius: 8px;
    border: 1px solid black;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #B20710;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.caption(
    "A sleek dark-themed interface designed for a smooth and engaging movie discovery experience."
)





