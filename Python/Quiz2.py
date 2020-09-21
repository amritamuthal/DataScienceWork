# Quiz2:
# Display a Breakdown of User Types

import pandas as pd

filename = 'chicago.csv'

df = pd.read_csv(filename)

user_types = df['User Type'].value_counts()

print(user_types)