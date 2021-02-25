import pandas as pd 

df = pd.read_excel("workingPoor(1).xlsx",index_col=0)
d = [7,47,10,38,34,1,39,3,29,6,25,18,26,48,21,8,28,40,45,51]
req =  list(map(lambda x : x - 1,d))
d  = pd.DataFrame(df.iloc[req,0:1])
d.to_csv("data.csv")

