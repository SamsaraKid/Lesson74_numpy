import numpy as np
import pandas as pd

dframe = pd.read_excel('movies.xlsx')

dramas = dframe[dframe['Жанр'] == 'драма']
spilberg = dframe[dframe['Режиссер'].str.contains('Спилберг')]
maxrating = dframe[dframe['Рейтинг'] == dframe['Рейтинг'].max()]
movies2005 = dframe[dframe['Год'] >= 2005]