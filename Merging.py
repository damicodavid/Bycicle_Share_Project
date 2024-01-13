#import pandas's module
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4_renamed.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1_renamed.csv") 

column_to_convert = 'trip_id'

df1[column_to_convert] = df1[column_to_convert].astype('object')

merged_df = pd.merge(df1, df2, how='inner', on="trip_id","start_time","end_time","bikeid","tripduration","station_id","from_station_name","to_station_id","to_station_name","usertype","gender","birthyear")  

#rename as you prefer ('')
merged_df.to_csv('filename.csv', index=False)