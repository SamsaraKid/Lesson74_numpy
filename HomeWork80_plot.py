import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
from colour import Color


dframe = pd.read_csv('sales_data.csv')  # считываем данные

dframe_shopquan = dframe[['Магазин', 'Количество']].copy()  # создаём новую таблицу только с магазином и количеством продаж
shopsum = dframe_shopquan.groupby(dframe_shopquan.Магазин).sum()  # находим сумму продаж по каждому магазину
fig = px.pie(shopsum, names=shopsum.index, values=shopsum.Количество, title='Количество продаж по магазинам')
fig.show()


fig = go.Figure()  # создаём фигуру
fig.update_layout(title="График продаж")  # именуем график
for n, s in enumerate(dframe.Магазин.unique()):  # проходим по всем магазинам
    dframe_shop = dframe[dframe['Магазин'] == s]  # для каждого магазина новая таблица
    dframe_shop_sum = dframe_shop.groupby('Фрукт').sum()  # находим количество проданных фруктов
    fig.add_trace(go.Bar(x=dframe_shop_sum.index, y=dframe_shop_sum.Количество, name=s))
fig.show()


red = Color("red")
colors = list(red.range_to(Color("blue"), len(dframe.Фрукт.unique())))  # подготавливаем цвета для графиков, количество цветов = количеству фруктов
fig = make_subplots(rows=2, cols=2, subplot_titles=dframe.Магазин.unique())  # делаем подграфики для каждого магазина, в заголовке название магазина
fig.update_layout(title="График цен")  # именуем график
r = 2
c = 2
pos = [(x+1, y+1) for x in range(r) for y in range(c)]  # массив позиций графиков
for n, s in enumerate(dframe.Магазин.unique()):  # проходим по всем магазинам
    dframe_shop = dframe[dframe['Магазин'] == s]  # для каждого магазина новая таблица
    for m, f in enumerate(dframe_shop.Фрукт.unique()):  # проходим по всем фруктам
        dframe_fru = dframe_shop[dframe_shop['Фрукт'] == f]  # для каждого фрукта новая таблица
        fig.add_trace(go.Scatter(x=dframe_fru.Дата, y=dframe_fru.Цена, name=f, line={'color': str(colors[m])},
                                 showlegend=True if n == 0 else False),
                      row=pos[n][0], col=pos[n][1])
fig.show()


