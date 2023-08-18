import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# st.write("""
# Mi primera aplicación interactiva
# Hola Mundo
# """)

df = pd.read_csv("UNI_CORR_500_01.txt", skiprows=4,sep="\t", names=["ID","frames", "X", "Y", "Z"])
st.write("""
# Mi primera aplicación interactiva
## Mostrar una tabla
""")

# Graficamos una tabla
st.table(df.head())

# Using "with" notation
with st.sidebar:
 # Titulo
 st.write("# Opciones")
 # slider
 div = st.slider('Número debins:', 0, 500, 25)
 st.write("Bins=", div)

st.write("""
# Mi primera aplicación interactiva
## Histograma sobre el eje X e Y
""")
# # Desplegamos un histograma con los datos del eje X
# fig, ax = plt.subplots(figsize=(10, 3))
# ax.hist(df["X"], bins=div, color= "lightcoral")
# ax.set_xlabel('Posición en metros' )
# ax.set_ylabel('Frecuencia')
# ax.set_title('Histograma posiciónes enel eje X')
# # Desplegamos el gráfico
# st.pyplot(fig)


fig, ax = plt.subplots(1, 2, figsize=(10,3))
ax[0].hist(df["X"], bins=div, color="lightcoral")
ax[0].set_xlabel('Posición en metros')
ax[0].set_ylabel('Frecuencia')
ax[0].set_title('Histograma posiciónes en eleje X')
ax[1].hist(df["Y"], bins=div, color="indianred")
ax[1].set_xlabel('Posición en metros')
ax[1].set_ylabel('Frecuencia')
ax[1].set_title('Histograma posiciónes en el eje Y')
st.pyplot(fig)




