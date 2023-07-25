import pandas as pd

# create a sample dataframe with a string column
df = pd.DataFrame({'date': ['2021-04-12 10:30:00', '2021-04-13 11:45:00', '2021-04-14 12:30:00']})

# convert the 'date' column from string to timestamp with a specified format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

# print the resulting dataframe
print(df)


