import pandas as pd

df3= pd.read_csv("Divvy_Trips_2019_Q4_and_202_Q1_C") 

df3['weekday'] = pd.to_datetime(df3['start_time']).dt.day_name()

df3['time_difference'] = pd.to_datetime(df3['end_time']) - pd.to_datetime(df3['start_time'])

df3.to_csv('Divvy_Trips_2019_Q4_and_202_Q1_C_v2.csv', index=False)

