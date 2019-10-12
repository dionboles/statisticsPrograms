import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
x = []
y = []
for i in open("parse.txt").readlines():
    x.append(int(str(i).split(" ")[0]))
    y.append(float(str(i).split(" ")[1]))
obj = {
    "x" : x,
    "y" : y
}
dataset = pd.pandas.DataFrame(obj)

dataset.to_csv("test.csv",index=False);
print(dataset)
X = dataset.iloc[:, 0].values.reshape(-1, 1)
Y = dataset.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()
print(np.corrcoef(x,y))