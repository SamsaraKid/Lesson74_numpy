import numpy as np
import pandas as pd

data = {'Name': ['Andrey', 'Anna', 'Nastya', 'Mila', 'Sasha', 'Zhenya', 'Dima', 'Anton', 'Ira', 'Kolya'],
        'Height': [189, 165, 170, 171, 155, 165, 182, 169, 165, 181],
        'Weight': [77, 70, 75, 64, 55, 80, 88, 75, 77, 61]}

dframe = pd.DataFrame(data)
dframe = dframe.sort_values(by='Height')
print(dframe.loc[1], dframe.loc[3], dframe.loc[5], sep='\n')
