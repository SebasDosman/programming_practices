import panda as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix

df = pd.read_csv('12_caracteristicas.csv', sep = ',')
del df['Hoja']

X = df.drop(['class'], axis = 1).to_numpy()
Y = df['class'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

model = RandomForestClassifier(max_depth = 10, n_estimators = 200)
model.fit(X_train, y_train)

plot_confusion_matrix(model, X_test, y_test)
plt.show()

