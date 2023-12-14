import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the Titanic dataset
titanic = pd.read_csv('./datasets/train.csv', index_col=0)

X = titanic.iloc[:, :-1] # feature matrix

y = titanic.iloc[:, -1]   # target variable

le = LabelEncoder()

y = le.fit_transform(y)

# Drop unnecessary columns if they exist
columns_to_drop = ['Cabin', 'Ticket', 'Embarked', 'Name']
titanic = titanic.drop(labels=columns_to_drop, axis=1, errors='ignore')

# Fill null values in 'Age'
titanic['Age'] = titanic['Age'].fillna(value=(-titanic['Fare'] * 0.04301) + (-titanic['Pclass'] * 7.90311) + 48)

# Feature scaling
for col in ['Age', 'Fare', 'Parch', 'SibSp']:
    titanic[col] = ((titanic[col] - np.mean(titanic[col])) / np.std(titanic[col]))

# Convert 'Sex' to numeric
ordered_sex = {'male': 0, 'female': 1}
titanic['Sex'] = titanic['Sex'].map(ordered_sex)

# Separate dependent and independent features
y = titanic['Survived'].copy()
titanic.drop(labels=['Survived'], inplace=True, axis=1)

# Create the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = GradientBoostingClassifier(n_estimators=100)
model = clf.fit(titanic, y)
model.fit(X_train, y_train)

# Check the cross-validation score
scores = cross_val_score(model, titanic, y, cv=10)
mean_score = np.mean(scores)
print(f"Mean score: {mean_score:.3f} (+/- {np.std(scores):.3f})")

# Testing
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Drop unnecessary columns if they exist
test = test.drop(labels=columns_to_drop, axis=1, errors='ignore')

titanic['Fare'].fillna(titanic['Fare'].median(), inplace=True)

# Fill null values in 'Fare' and 'Age'
test['Fare'] = test['Fare'].fillna(value=131.757 - (42.379 * test['Pclass']))
test['Age'] = test['Age'].fillna(value=(test['Fare'] * 0.0152) + (-test['Pclass'] * 7.73788) + 46.13266)

# Feature scaling for the test set
for col in ['Age', 'Fare', 'Parch', 'SibSp']:
    test[col] = ((test[col] - np.mean(test[col])) / np.std(test[col]))

# Convert 'Sex' to numeric for the test set
test['Sex'] = test['Sex'].map(ordered_sex)

# Predict
y_pred = model.predict(test)
y_pred = model.predict(X_test)

# Store in a DataFrame
ID = pd.Series(range(892, 1310))
sol = pd.DataFrame({'PassengerId': ID, 'Survived': y_pred})

# Display accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'\n\nModel Accuracy: {accuracy * 100:.2f}%')
