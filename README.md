# **Welcome to Bicycle-Share analysis in Python!**

This is my first project as part of the last step of the _**Google Analytics Certificate**_ 

## Scenario
In **2016**, _Cyclistic_ launched a successful bike-share offering. Since then, the program has grown
to a fleet of **5,824 bicycles** that are geotracked and locked into a network of 692 stations
across **Chicago**. The bikes can be unlocked from one station and returned to any other station
in the system anytime.

The basic approach was the flexibility of its pricing plans: single-ride passes, full-day passes, and annual memberships:

* Customers who purchase single-ride or full-day passes are referred to as casual riders.
* Customers who purchase annual memberships are Cyclistic members.

**Cyclistic’s finance analysts have concluded that annual members are much more profitable than casual riders.**

## Marketing goals
1. How do annual members and casual riders use _Cyclistic_ bikes differently?
2. What are the possible action in order to convert casual rider to annual memberships type?

## Step-by-step Analysis 

We'll analyze quarter 2019 Q4 and 2020 Q1 data frame (6 months dataset) and we'll present the possible resolutions for the marketing dep.

1. Download the public data from -> [Datasets](https://divvy-tripdata.s3.amazonaws.com/index.html)

2. Verify how is the data organized (columns structure and wideness)? 

3. Are there issues with bias or credibility in this data? 

4. Does your data ROCCC (Reliable, Original, Comprehensive, Current, Cited)?

**After these preliminary phases we can go through the _Data overview process_:**

5.Overview your data:

``` 
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4.csv") 

print(df1)
```

This will give you and overview of your data:

![image](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/8f0b404a-97af-43ed-a310-e762cce2773f)

repeat for the second dataframe
``` 
import pandas as pd

df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

print(df2)
```
we can notice that we have different name convetion for similar data that we'll have to rename so we can merge the two dataframe:
![image](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/cb05e292-bf98-4403-b9bf-e8ebed549a48)

6. Check data type of each column

``` 
import pandas as pd

df = pd.read_csv("Divvy_Trips_2019_Q4.csv")
 
data_type= df.dtypes

print(data_type)
```

**After these overview phases we can go through the _Data manipulation and cleaning process_:**

Before cleaning it's essential to merge the two data-frames verifying that the column names is unique in both file:
```
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

print("Columns in df1:", df1.columns)
print("Columns in df2:", df2.columns)
```
we can notice that we have different columns names for data of the same category:
![image](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/ccc0292e-ccd8-4668-832e-1e6d852d775f)

Rename columns names of the second data-frame and replace value in df1 for user type in order to have standardized naming convention between the two dataset and save as a new files:
```
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

column_name_mapping = {
    'ride_id': 'trip_id',
    'started_at': 'start_time',
    'ended_at': 'end_time',
    'start_station_name': 'from_station_name',
    'start_station_id': 'from_station_id',
    'end_station_id': 'to_station_id',
    'end_station_name': 'to_station_name',
    'member_casual': 'usertype',
    }

df2.rename(columns=column_name_mapping, inplace=True)

print("Columns in df2:", df2.columns)

column_to_modify = 'usertype'
value_mapping = {'Subscriber': 'member', 'Customer': 'casual'}


df1['usertype'] = df1['usertype'].replace(value_mapping)

column_to_convert = 'trip_id'

df1[column_to_convert] = df1[column_to_convert].astype('object')

df1.to_csv('Divvy_Trips_2019_Q4_renamed.csv', index=False)
df2.to_csv('Divvy_Trips_2020_Q1_renamed.csv', index=False)
```
File will be saved with a new name "oldnamefile_renamed"

7.Concat the two file in a unique dataset

import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4_renamed.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1_renamed.csv") 

column_to_convert = 'trip_id'

df1[column_to_convert] = df1[column_to_convert].astype('object')

concatenated_df = pd.concat([df1, df2], axis=0)

concatenated_df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1', index=False)

7. Remove any duplicates in the dataset and replace n/a values with "not specified" and then save.

``` 
import pandas as pd

df = pd.read_csv("Divvy_Trips_2019_Q4_and_2020_Q1.csv") 

df = df.drop_duplicates()

df = df.fillna(value="not specified")

print(df)

df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1_v1', index=False)
```

8. Creation of new columns such as "ride length" and "weekday" for our following analysis:
```
import pandas as pd

df= pd.read_csv("Divvy_Trips_2019_Q4_and_2020_Q1_C") 

df['weekday'] = pd.to_datetime(df['start_time']).dt.day_name()

df['time_difference'] = pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time'])

df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1_C_v2.csv', index=False)
```

Now we have all the data we need to start to analyse and create our dashboards that we will tell our story about the dataset in order to address marketing requests.

After have been analyzed data we find out that casual riders are most likely using more bicycle in the weekends and the average ride time is almost 4 times longer than the member one.


![Dashboard_Cyclist](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/e8adf448-faa8-4eae-9d7c-1d285ae4ea92)
**INSIGHTS:**
1. It seems casual riders use bicycle for leisure purpose and members as an alternative transports for daily activities (work,school...);
2. 13.68 % of the total rides is made from casual customers that could be retained as members and increase total revenues;
3. Average Age is lower for casual riders 36 vs 41 Years old for member one.

**SOLUTIONS:**
1. Increasing the percentage of members is possible through a well structured loyalty program;
2. Proposed assigning unique rider ID numbers for in-depth analysis and ensure compliance with GDPR principles in data handling;
3. Create a campaign to target younger clients to increase total revenue.
