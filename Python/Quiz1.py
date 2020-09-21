# Quiz1:
# Compute the Most Popular Start Hour

import pandas as pd

filename = 'chicago.csv'

df = pd.read_csv(filename)

df['Start Time'] = pd.to_datetime(df['Start Time'])

df['hour'] = df['Start Time'].dt.hour

popular_hour = df['hour'].mode()[0]

print('Most Popular Start Hour:', popular_hour)
