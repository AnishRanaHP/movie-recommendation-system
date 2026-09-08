# Movie Recommendation System

A **content-based movie recommendation system** built using Python and machine learning techniques. The system analyzes movie information such as genres, keywords, overview, cast, and crew to recommend movies that are similar to a movie selected by the user.

## Project Overview

Finding a good movie to watch can be difficult when there are thousands of options available. This project aims to solve this problem by recommending movies based on the content and characteristics of a selected movie.

The system processes movie metadata, creates a combined feature representation, and calculates similarity between movies to generate recommendations.

## Objectives

* Build a movie recommendation system using Python.
* Process and combine different movie features.
* Apply text-processing techniques to movie metadata.
* Calculate similarity between movies.
* Recommend movies similar to the user's selected movie.

## Dataset

The project uses the **TMDB 5000 Movies Dataset**, including movie information such as:

* Movie title
* Genres
* Keywords
* Overview
* Cast
* Crew
* Movie ID
* Popularity
* Ratings

The movie data is loaded using Pandas for preprocessing and analysis.

## Methodology

The recommendation system follows these main steps:

1. **Load the Dataset**
   Movie and credit datasets are imported using Pandas.

2. **Data Preprocessing**
   Relevant movie information is selected and processed to make it suitable for the recommendation model.

3. **Feature Engineering**
   Important movie features such as genres, keywords, overview, cast, and crew are combined to create a unified representation of each movie.

4. **Text Processing**
   Movie information is converted into text-based features that can be used for similarity analysis.

5. **Vectorization**
   Movie features are converted into numerical representations.

6. **Similarity Calculation**
   Similarity between movies is calculated using **Cosine Similarity**.

7. **Recommendation**
   The system identifies movies with the highest similarity scores and returns the most relevant recommendations.

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **NLTK**
* **Scikit-learn**
* **Natural Language Processing (NLP)**
* **Machine Learning**

## Project Structure

```text
Movie-Recommendation-System/
│
├── Movie-recomender-system.ipynb
├── README.md
└── Dataset/
    ├── tmdb_5000_movies.csv
    └── tmdb_5000_credits.csv
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Install required libraries

```bash
pip install pandas numpy nltk scikit-learn
```

### 3. Open the notebook

Open:

```text
Movie-recomender-system.ipynb
```

using **Jupyter Notebook** or **Google Colab**.

### 4. Run the cells

Execute the notebook cells in order and provide a movie title to generate recommendations.

## Example

**Input:**

```text
Avatar
```

**Output:**

The system returns movies that are most similar to the selected movie based on their available content and metadata.

## Future Improvements

* Create a web interface using **Streamlit**
* Add movie posters and additional movie information
* Include user ratings and watch history
* Implement collaborative filtering
* Develop a hybrid recommendation system
* Deploy the recommendation system online

## Author

**Anish Rana**

This project was developed as a practical application of **Python, NLP, and machine learning concepts** to build a real-world recommendation system.

