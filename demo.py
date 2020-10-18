import pandas as pd
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))