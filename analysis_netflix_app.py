import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv("data/netflix_titles.csv")

st.sidebar.title("Menu")

st.title("Analysis Netflix")
st.write("Netflix é uma das plataformas de streaming de mídia e vídeo mais populares. Este conjunto de dados tabulares consiste em listas de todos os filmes e séries disponíveis na Netflix, juntamente com detalhes como elenco, diretores, classificações, ano de lançamento, duração, etc.")
st.dataframe(df)
st.bar_chart(data=df[["show_id", "type"]].groupby(by="type")["show_id"].count())
st.bar_chart(data=df[["show_id", "release_year"]].groupby(by="release_year")["show_id"].count())
st.bar_chart(data=df[["show_id", "country"]].groupby(by="country")["show_id"].count().sort_values(ascending=False)[:10])