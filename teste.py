# Importar librarys
import streamlit as st
import pandas as pd
from numpy.random import randint
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import  numpy as np
import plotly.express as px
import plotly.graph_objects as go


# Radio
chute = st.radio(
    "por que essa função se chama radio?",
    ('Opção 1: porque o rádio é um osso muito bonito',
     'Opção 2: é uma homenagem à Marie Curie',
     'Opção 3: as opções lembram botões de rádio')
)
if chute == 'Opção 3: as opções lembram botões de rádio':
    st.write('Correto!')
else:
    st.write("Incorreto, tente novamente.")
#input de números
input_num = st.number_input(
       'Escreva um número entre 0 e 10',
       min_value = 0,
       max_value = 10,
       value = 0,
       step = 1
)
st.write('O número inputado foi: ', input_num)
#input de texto
input_txt = st.text_input(
      'Escreva uma palavra com até 5 letras',
      value = 'juiz',
      max_chars = 5
)
st.write('A palavra inputada foi: ', input_txt)
#dataset de iris do sklearn
df = px.data.iris()
#lista de possíveis especies
lista_especie = ('setosa','versicolor','virginica')
#caixa de seleção à esquerda
var_especie = st.sidebar.selectbox(
    'Escolha a espécie a ser visualizada',
    lista_especie
)
#dicionários de cores a serem visualizadas no gráficos
dict_flor={
 lista_especie[0]:'blue',
 lista_especie[1]:'red',
 lista_especie[2]:'green'
}
#gráfico 3D gerado a partir do plotly
fig = go.Figure(
       data=go.Scatter3d(
          x=df['sepal_length'],
          y=df['sepal_width'],
          z=df['petal_width'],
          mode='markers',
          marker=dict(
            size=4,
            color=np.where(
               df['species'] == var_especie,
               dict_flor[var_especie],
               'lightgray'
            )
          )
       )
)
st.plotly_chart(fig)

#precisa escrever o texto? Beleza
st.write('hola!')
#quer mostrar a tabela? Não tem problema
st.write(df)
#aguenta gráficos? Tranquilo
st.write(fig)
#e muito mais...