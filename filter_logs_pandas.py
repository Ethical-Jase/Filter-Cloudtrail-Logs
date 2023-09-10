import pandas as pd
import json

# crate a list to add dataframes to
awsc_list = list()

# list of files
files_list = ['test.json', 'test2.json']

# read the files
for file in files_list:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    
    # normalize the file and append it to the list of dataframe
    awsc_list.append(pd.json_normalize(data, 'Records', sep='_'))
    
# concat the files into a single dataframe
awsc = pd.concat(awsc_list).reset_index(drop=True)

# display top 5 rows
awsc.head()

# displays specific columns
awsc[['eventTime', 'awsRegion', 'eventName', 'userIdentity_userName']]

# allows mixed formats to be used
awsc['eventTime'] = pd.to_datetime(awsc['eventTime'],dayfirst=True, format='mixed')

#displays types e.g objects
awsc.dtypes

# sets time and date to current
from datetime import datetime
now  = datetime.now()

# sorts date range greater than and less than
dateMask = (awsc['eventTime'] > '2014-03-06 17:00:00') & (awsc['eventTime'] < '2014-03-06 20:00:00')
df=awsc.loc[dateMask]
df.head(10)

# sorts for specific ip address and display top 10 rows 
ipmask = (awsc['sourceIPAddress']=='205.251.233.176') 
dfip=awsc.loc[ipmask]
dfip.head(10)

# will display rows 1 and 2
awsc.iloc[1:3]

# sorts assending
awsc.sort_values('eventTime', ascending = True)

# sorts decending
awsc.sort_values('eventTime', ascending = False)

# looks for specific ip address
awsc['sourceIPAddress'] == ('72.21.198.64')

# looks for srting containing "api"
awsc['userAgent'].str.contains('api')

# displays all ip address and a count of each 
awsc.groupby('sourceIPAddress').count()

# displays eventName and eventTime columns and a count of each
awsc.groupby(['eventName', 'eventTime']).count()

# will return an interger of total number of different eventTimes found
awsc['eventTime'].nunique()

# will return each a list of each different result found in eventTime column
awsc['eventTime'].unique()

