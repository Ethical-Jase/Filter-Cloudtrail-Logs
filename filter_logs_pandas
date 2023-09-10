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

awsc.head()

awsc[['eventTime', 'awsRegion', 'eventName', 'userIdentity_userName']]

awsc['eventTime'] = pd.to_datetime(awsc['eventTime'],dayfirst=True, format='mixed')

from datetime import datetime
now  = datetime.now()

dateMask = (awsc['eventTime'] > '2014-03-06 17:00:00') & (awsc['eventTime'] < '2014-03-06 20:00:00')
df=awsc.loc[dateMask]
df.head(10)

ipmask = (awsc['sourceIPAddress']=='205.251.233.176') 
dfip=awsc.loc[ipmask]
dfip.head(10)

awsc.iloc[1:3]

awsc.sort_values('eventTime', ascending = True)

awsc.sort_values('eventTime', ascending = False)

awsc['sourceIPAddress'] == ('72.21.198.64')

awsc['userAgent'].str.contains('api')

awsc.groupby('sourceIPAddress').count()

awsc.groupby(['eventName', 'eventTime']).count()

awsc['eventTime'].nunique()

awsc['eventTime'].unique()
