import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")
df.plot(kind="scatter", x="diametro", y="preco");
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x ,y)

st.title("Prever valor da Pizza - Pizzaria Machine Learning")
st.divider()
diametro = st.number_input("Digite o tamanho do diametro do pizza em cm: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da Pizza com diametro de {diametro}cm, custa um total de: R${preco_previsto:.2f}")
    st.write("Na compra de duas pizzas ganha uma Pizza doce de brinde!")
    st.divider()
    st.write("")