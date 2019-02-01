
import pandas as pd
import numpy as np

data = pd.read_csv("lead.csv") 
print(data.head(5))
print(data.dtypes)

from datetime import datetime

data["RESULT"]=data.RESULT.astype(float)
data["SAMPLE_DATE"]=pd.to_datetime(data['SAMPLE_DATE'])
data['SchoolName'] =  data['SchoolName'].astype(str) 

#filter rows for based on the values and the date


school_names=np.array(list(data.SchoolName))
names, indices = np.unique(school_names, return_inverse=True)
names=np.array(names)

filtered=pd.DataFrame()
for school in names:
    subset = data[data.SchoolName==school]
    subset1 = subset[subset.SAMPLE_DATE==subset.SAMPLE_DATE.max()]
    subset2 = subset1[subset1.RESULT==subset1.RESULT.max()]
    if len(subset2.ID)>1:
        subset2 = subset2.iloc[[0]]
    else:
        subset2=subset2
    filtered = filtered.append(subset2)

filtered.to_csv('filtered.csv' , index=False)

