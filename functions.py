import pandas as pd

df = pd.read_csv('sample_csa.csv',index_col=0)
df.drop(['Unnamed: 5','Unnamed: 6'],axis=1,inplace=True)
df.columns=['fname','lname','salary','eligibility']
df['eligibility'] = df['eligibility'].apply(lambda x: x.lower())
print(df)