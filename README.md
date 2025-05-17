# 🎬 Movie Recommendation System

This project is a web-based application built using **Streamlit** and **Flask**, which provides personalized movie recommendations using collaborative, content-based, and hybrid filtering techniques. It applies machine learning models including KNN, SVD, NMF, and neural networks to deliver relevant and diverse suggestions.

---

## 📌 Objectives

- Predict movies that align with user interests and watch history
- Provide real-time recommendations with high accuracy
- Enhance user satisfaction through hybrid recommendation approaches

---

## 📊 Dataset Overview

- Source: MovieLens, IMDb, Kaggle
- Features include:
  - `title`, `genre`, `duration`, `user_id`, `rating`, `release_year`
  - `director`, `actors`, `timestamp`, `popularity_score`

---

## 🔍 Techniques Used

- **Collaborative Filtering**: KNN, NMF, SVD
- **Content-Based Filtering**: TF-IDF on genres & descriptions
- **Hybrid Modeling**: Combining both for personalized predictions
- **Evaluation**: MAE, RMSE, Precision@K, Recall@K

---

## 📈 Key Visualizations

### 🎭 Top 10 Genres by Frequency
Shows genre popularity using a bar chart.

![Genres](images/genres_rating_bar.png)

### ⭐ Ratings vs. Votes (Scatter)
Highlights how higher votes usually relate to better user ratings.

![Ratings Votes](images/rating_votes_scatter.png)

---

## 🧠 Model Performance

| Metric         | Training | Testing |
|----------------|----------|---------|
| MAE            | 0.095    | 0.125   |
| RMSE           | 0.208    | 0.328   |
| R² Score       | 0.997    | 0.991   |

✅ *Model generalizes well without overfitting.*

---

## 🚀 Tech Stack

- Python, Pandas, NumPy
- Flask (API) + Streamlit (UI)
- Scikit-learn, Surprise
- SQLite/PostgreSQL (optional)

---

## 🧰 How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app/streamlit_ui.py
