import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("diabetes.csv")

#print(len(dataset))
#print(dataset.head)

zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']

for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0, np.NAN)
    mean = dataset[column].mean(skipna=True)
    dataset[column] = dataset[column].replace(np.NAN, mean)


X = dataset.iloc[:, 0:8] #Input column
y = dataset.iloc[:, 8] #Output column
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean') #euclidean is mathematical formula which calculates the distances between each points of data
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
#print(y_pred)

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f1_score(y_test, y_pred))
