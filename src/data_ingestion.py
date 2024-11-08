import pandas as pd
import os
import numpy as np

df=pd.read_csv('/home/kshitiz/CampusX-MLOPS/dvc-demo/Ecommerce Customers.csv')
df.iloc[:, 3:]
df=df[df['Length of Membership']>1]
df.drop(columns=['Avg. Session Length'],inplace=True)
df.to_csv(os.path.join('data','customer.csv'))
