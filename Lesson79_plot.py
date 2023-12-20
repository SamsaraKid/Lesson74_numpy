import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go

'''
line - линии
scatter - точки
area - области
bar - бар-график
pie - пирог
'''


# dx = np.arange(0, 18.9, 0.05)  # [1, 2, 3, 4]
# dy = [1, 4, 9, 16]
# dy = np.power(dx, 2)
# dy = np.sin(dx)
# fig = px.line(x=dx, y=dy, title='Plot')
# fig.show()

# from plotly.graph_objs import Scatter, Layout
# plotly.offline.plot({ "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])], "layout": Layout(title="hello world") })

# dt = np.arange(0, 10*np.pi, 0.00005)
# dx = 24.8*(np.cos(dt) + (np.cos(6.2*dt)/6.2))
# dy = 24.8*(np.sin(dt) + (np.sin(6.2*dt)/6.2))
# fig = px.line(x=dx, y=dy, title='Plot')
# fig.show()

# dt = np.arange(0, 2 * np.pi, 0.0005)
# dx = 16 * np.power(np.sin(dt), 3)
# dy = 13 * np.cos(dt) - 5 * np.cos(2 * dt) - 2 * np.cos(3 * dt) - np.cos(4 * dt)
# df = pd.DataFrame({'x': dx, 'y': dy})
# fig = px.area(df, x='x', y='y', title='Plot')
# fig.show()

# dframe = px.data.carshare()
# # fig = px.bar(dframe, x='peak_hour', y='car_hours')
# dsum = dframe.groupby(dframe.peak_hour).sum()
# fig = px.bar(dsum, y='car_hours', x=dsum.index, color='car_hours',
#         color_continuous_scale=['red', 'orange', 'green', 'blue', 'violet'])
# fig.show()

# dframe = pd.read_excel('students_mean.xlsx')
# fig = px.bar(dframe, x=dframe.Имя, y=dframe.Средний)
# fig.show()

# du = np.arange(-2*np.pi, 2*np.pi, 0.0005)
# dv = np.arange(-1*np.pi, np.pi, 0.00025)
# dx = (np.cos(du)) * (np.cos(dv)) + 3 * (np.cos(du)) * (1.5 + np.sin(1.5 * du / 2))
# dy = (np.sin(du)) * (np.cos(dv)) + 3 * (np.sin(du)) * (1.5 + np.sin(1.5 * du / 2))
# dz = np.sin(dv) + 2*np.cos(1.5*du)
# fig = px.scatter_3d(x=dx, y=dy, z=dz)
# fig.show()

# dframe = px.data.election()
# dsum = dframe.groupby(dframe.winner).count()
# fig = px.pie(dsum, names=dsum.index, values=dsum.result)
# fig.show()


# data2 = [100000, 120000, 150000, 80000, 200000, 250000, 180000, 300000, 280000, 320000, 350000, 400000,
#         180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000,
#         150000, 300000, 250000, 280000, 320000, 350000, 380000, 400000, 420000, 440000, 470000, 500000,
#         200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000, 420000,
#         150000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000]
# ser2 = pd.Series(data2, name='name',
#                  index=pd.date_range(start='2019-01-01',
#                                      periods=len(data2), freq='M'))
# fig = px.line(ser2, x=ser2.index, y=ser2.name)
# fig.show()

dx = np.arange(1, 100)
dy1 = np.random.randint(1, 10, size=100)
dy2 = np.random.randint(20, 50, size=100)
dy3 = np.random.randint(60, 100, size=100)
fig = go.Figure()  # пустой график
graf1 = go.Scatter(x=dx, y=dy1, name='graf1', mode='markers')  # создаётся линия
graf2 = go.Scatter(x=dx, y=dy2, name='graf2', mode='markers+lines')
graf3 = go.Scatter(x=dx, y=dy3, name='graf3', mode='lines')
fig.add_trace(graf1)  # линия добавляется на график
fig.add_trace(graf2)
fig.add_trace(graf3)
#  подписи графика
fig.update_layout(title='График')
fig.update_xaxes(title='точки')
fig.update_yaxes(title='от 1 до 100')
fig.show()
