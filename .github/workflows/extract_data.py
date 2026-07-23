#import pandas library
import pandas as pd

#create dictionary
data ={

    "id": [1,2,3],
    "name ": ["a","b","c"],
    "age":[10,20,30]
}

#convert to tabular format 
df = pd.DataFrame(data)

#show data
print(df)