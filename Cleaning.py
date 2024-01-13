#import pandas's module
import pandas as pd

df_c = pd.read_csv("Divvy_Trips_2019_Q4_and_2020_Q1.csv") 

df_c = df_c.drop_duplicates()

df_c = df_c.fillna(value="not specified")

print(df_c)


