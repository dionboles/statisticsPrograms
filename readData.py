import pandas as pd 


df = pd.read_csv("data3.csv")

num = {
	"Personal" : 0,
	"Work" : 0,
	"Course" : 0
}
m = {
	"Personal" : 0,
	"Work" : 0,
	"Course" : 0
}
f = {
	"Personal" : 0,
	"Work" : 0,
	"Course" : 0
}
index = 0;
df['Reason'].array

for i in df['Reason'].array:
	if i in num:
		if(df['Gender'].array[index] == "M"):
			m[i] = m[i]+1
		else:
			f[i] = f[i]+1
		
		
	index = index+1
#	if( i == num['Personal']){
#		num['Personal'] = num['Personal']+1
#	}
#
print("male")
print(m)
print("female")
print(f)