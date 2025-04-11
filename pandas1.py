import pandas as pd

# s=pd.Series([10,20,30], index=['a','b','c'])
# print(s)

data={
    'name':['a','b','c'],
    'age':[1,2,3],
    'city':['x','y','z']
}
df = pd.DataFrame(data,index=[1,2,3])
# print(df)
# print("================")
# print(df.head())
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print("================")
# print(df['age'])
# print(df[['name','city']])
# print(df[df['age']>2])

# df['age']+=1
# df['city']='usa'
# df.rename(columns={'age':'years'},inplace=True)
# df.drop('city',axis=1)
# print(df)

