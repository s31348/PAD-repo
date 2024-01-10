import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Importowanie wyczyszczonych danych przed skalowaniem
data = pd.read_csv('clean_data.csv')

# Tworzenie dashboardu
st.title('Dashboard PAD - s31348')

st.header('Wizualizacje')

##############################################################################################################

# 1. Wizualizacja rozkładu zmiennych numerycznych
numeric_columns = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table']
categorical_columns = ['clarity', 'color', 'cut']
dependent_variable = 'price'

st.subheader('1. Wizualizacja rozkładu zmiennych numerycznych')
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
for i, ax in enumerate(axes.flatten()):
    sns.histplot(data[numeric_columns[i]], ax=ax)
    ax.set_title(numeric_columns[i])
st.pyplot(fig)

# 2. Zależności ceny od innych zmiennych
st.subheader('2. Zależności ceny od innych zmiennych')
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
for i, ax in enumerate(axes.flatten()):
    sns.scatterplot(x=numeric_columns[i], y=dependent_variable, data=data, ax=ax)
    sns.regplot(x=numeric_columns[i], y=dependent_variable, data=data, ax=ax, scatter=False, color='red')
    ax.set_title(numeric_columns[i])
st.pyplot(fig)

# 3. Liczebność kategorii zmiennych kategorycznych
st.subheader('3. Liczebność kategorii zmiennych kategorycznych')
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for i, ax in enumerate(axes.flatten()):
    sns.countplot(x=categorical_columns[i], data=data, ax=ax)
    ax.set_title(categorical_columns[i])
st.pyplot(fig)

# 4. Wykresy cen dla poszczególnych kategorii zmiennych kategorycznych
st.subheader('4. Wykresy cen dla poszczególnych kategorii zmiennych kategorycznych')
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for i, ax in enumerate(axes.flatten()):
    df_gb = (data
             .groupby(categorical_columns[i])
             .agg({'price': 'mean'}).reset_index()
             .sort_values(by='price', ascending=False))
    sns.barplot(x=categorical_columns[i], y ='price', data=df_gb, ax=ax)
    ax.set_title(categorical_columns[i])
st.pyplot(fig)

##############################################################################################################

st.header('Analiza wybranej zmiennej + próbka danych')

selected_variable = st.selectbox('Wybierz zmienną do analizy:', [col for col in data.columns if col !='price'])

# Wizualizacja rozkładu wybranej zmiennej i zależności ceny od innych zmiennych

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.histplot(data[selected_variable], kde=True, ax=axes[0])
axes[0].set_title('Rozkład wybranej zmiennej')
sns.scatterplot(x=data[selected_variable], y=data['price'], ax=axes[1])
axes[1].set_title('Zależność ceny od innych zmiennych')
st.pyplot(fig)

# Wyświetlenie próbki danych w postaci tabeli
st.subheader('Próbka danych')
st.write(data.head())