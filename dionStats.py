import pandas as pd 
df = pd.read_csv("ua.sql.csv")
df['da'] = pd.to_datetime(df['clock_out'],format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df['clock_in'],format='%Y-%m-%d %H:%M:%S')
print(df['da'].dt.days)
#
#df.to_csv("testa.csv",index=False);