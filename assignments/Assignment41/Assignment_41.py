# Wine Case Study

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

Border = "-" * 40

##################################################
# Step 1 : Load the Dataset
##################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Data = load_wine()

X = Data.data
Y = Data.target

print("Wine DataSet Loaded Successfully.....")
print("Number of Features is: ", X.shape[1])
print("Number of Records: ", X.shape[0])
print("Classes are: ", Data.target_names)

print(Border)


##################################################
# Step 2 : Clean Prepare and Manipulate the Dataset
##################################################

print(Border)
print("# Step 2 : Clean Prepare and Manipulate the Dataset")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("\nData Preparation Completed....")
print("Training Data: ", X_train.shape)
print("Testing Data: ", X_test.shape)

# To calculate distance between the points

sobj = StandardScaler()

X_train = sobj.fit_transform(X_train)
X_test = sobj.transform(X_test)

print(Border)

##################################################
# Step 3 : Train the Data
##################################################

print(Border)
print("Step 3 : Train the Data")
print(Border)

model = KNeighborsClassifier(n_neighbors=5)
model = model.fit(X_train , Y_train)
print("Model Training Done Successfully....")

print(Border)

##################################################
# Step 4 : Test the Data
##################################################

print(Border)
print(" Step 4 : Test the Data")
print(Border)

result = model.predict(X_test)

print("\nActual Output: ", Y_test)
print("\nPredicted Output: ", result)

print(Border)

##################################################
# Step 5: Accuracy Calculation
##################################################

print(Border)
print("Step 5: Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test , result)
print("\n Accuracy of the Machine Learning Model is: ")
print(accuracy * 100)

print(Border)






