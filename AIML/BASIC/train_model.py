import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv(r"C:\Users\sivan\Downloads\ShadowFox\AIML\BASIC\HousingData.csv")
df = df.dropna()

X = df.drop("MEDV", axis=1)
y = df["MEDV"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
