import streamlit as st
import var13

st.image('Titanic.png')
st.header('Данные пассажиров Титаника')
st.subheader('группа ПИ-1-см, команда 5')

var = ['Вариант 13 (Юнусова)', 'Вариант 10 (Демура)', 'Вариант 20 (Степанова)']

var = st.radio("Выберите вариант : ", var)

with open("data.csv") as file:
    data = file.readlines()

if var == 'Вариант 13 (Юнусова)':
    var13.main(data)
elif var == 'Вариант 10 (Демура)':
    st.text('по состоянию на 13.06.2024 не удалось связаться со студентом')
elif var == 'Вариант 20 (Степанова)':
    st.text('по состоянию на 13.06.2024 не удалось связаться со студентом')
