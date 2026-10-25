import streamlit as st
import joblib

model = joblib.load("models/text_model.joblib")

st.title("Clasificador de reseñas IMDB")

st.warning(
    "Este modelo fue entrenado con reseñas de películas en inglés. "
    "La predicción es una estimación basada en los datos de entrenamiento y no debe interpretarse como una verdad absoluta."
)

texto = st.text_area(
    "Escriba una reseña:"
)

if st.button("Clasificar"):

    if texto.strip():

        pred = model.predict([texto])[0]

        if pred == 1:
            st.success("Predicción: POSITIVA")
        else:
            st.error("Predicción: NEGATIVA")
