import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

#Analisa o algoritimo
df = pd.read_csv("pizzas.csv")
df.plot(kind="scatter", x="diametro", y="preco");
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x ,y)

#Configuração do site
st.title("Prever valor da Pizza - Pizzaria Cérebro Pensante")
st.write("Site teste de Machine Learning feito Por: João Pedro Kapp - Noooob")
st.write("Site desenvolvido em: Python e Jupyter Notebook")
st.divider()
diametro = st.number_input("Digite o tamanho do diametro do pizza em cm: ")
if diametro > 0:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da Pizza com diametro de {diametro}cm, custa um total de: R${preco_previsto:.2f}")
    st.write("Na compra de três pizzas de trinta centimetros ou mais, você ganha uma Pizza doce de brinde!")
    st.divider()
else:
    st.write("A Pizza não pode ter um diametrro negativo!")
