import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv', parse_dates=['date'])

df_sorted = df.sort_values(by = ['state','date']) 
df_sorted['date'] = df_sorted['date'].astype(str)

df_sorted['new_deaths'] = df_sorted.groupby(['state'])['deaths'].diff().fillna(0)
df_sorted['new_cases'] = df_sorted.groupby(['state'])['cases'].diff().fillna(0)

df_sorted.fillna('', inplace=True)

df_sorted.to_csv('covid_data.csv')