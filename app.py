import streamlit as st
import requests

st.title("🎬 Movie Recommendation System")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendations"):
    try:
        response = requests.post("http://127.0.0.1:5000/recommend", json={"user_id": user_id})

        if response.status_code == 200:
            recommendations = response.json().get("recommendations", [])
            if not recommendations:
                st.warning("⚠️ No recommendations found!")
            else:
                st.subheader("📌 Recommended Movies")
                for movie in recommendations:
                    st.write(f"🎥 {movie['title']} ({movie['genre']}) - ⭐ {movie['rating']}")
        else:
            st.error("❌ Error fetching recommendations! API returned an error.")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error connecting to API: {e}")

