import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the data set
data = pd.read_csv('dataset.csv')

# Create a dictionary to map the values ​​of 'type'
type_mapping = {
    'CASH_OUT': 1, 'PAYMENT': 2,
    'CASH_IN': 3, 'TRANSFER': 4,
    'DEBIT': 5
}

# Create a dictionary to map the values ​​of 'isFraud'
fraud_mapping = {
    0: 'Not Fraud', 1: 'Fraud'
}

# Map the values ​​of 'type' and 'isFraud'
data['type'] = data['type'].map(type_mapping)
data['isFraud'] = data['isFraud'].map(fraud_mapping)

# Create the input (x) and output (y) variables
x = data[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']].values
y = data['isFraud'].values

# Split the data set into training and testing
xtrain, xtest, ytrain, ytest = train_test_split(
    x,
    y,
    test_size=0.10,
    random_state=42
)

# Create and train the decision tree model
model = DecisionTreeClassifier()
model.fit(xtrain, ytrain)

# Calculate the accuracy of the model on the test set
accuracy = accuracy_score(ytest, model.predict(xtest))
print(f'Accuracy: {accuracy}')

# Make a prediction with new data
# PS: You can replace this data with your own personal data
features = np.array([[4, 9000.60, 9000.60, 0.0]])
print('-------------------- Printed results --------------------')
print(model.predict(features))