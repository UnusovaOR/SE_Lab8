import matplotlib.pyplot as plt
import streamlit as st


def get_count(lines, age):
    c = 0
    q = 0
    s = 0
    for line in lines:
        lst = line.rstrip().split(',')
        if lst[1] == '0' and lst[6] != '' and float(lst[6]) < age:
            if lst[12][:-1] == 'C':
                c = c + 1
            elif lst[12][:-1] == 'Q':
                q = q + 1
            elif lst[12][:-1] == 'S':
                s = s + 1
    return c, q, s


def main(file_lines):
    st.write('Для подсчета количества погибших детей по каждому пункту '
             'посадки, укажите максимальный возраст: ')
    max_age = st.slider('максимальный возраст', 1, 18)
    c, q, s = get_count(file_lines, max_age)
    embarked = ['Шербур', 'Квинстаун', 'Саутгемптон']
    count = [c, q, s]
    data = {'пункт посадки': embarked, 'количество': count}
    st.dataframe(data)
    fig = plt.figure(figsize=(8, 3))
    bar_colors = ['red', 'green', 'blue']
    plt.bar(embarked, count, color=bar_colors)
    plt.xlabel('пункт посадки')
    plt.ylabel('количество')
    plt.title(f'количество погибших детей в возрасте до {max_age} лет')
    st.pyplot(fig)
