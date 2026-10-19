
import pandas as pd
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, roc_auc_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

print("Step 0: All libraries imported successfully!")

# 1. Create sample data
np.random.seed(42)
n = 1000

df = pd.DataFrame({
    'Age': np.random.randint(20, 70, n),
    'Income': np.random.randint(30000, 120000, n),
    'LoanAmount': np.random.randint(5000, 40000, n),
    'CreditScore': np.random.randint(550, 850, n),
    'EmploymentYears': np.random.randint(0, 30, n),
    'ExistingLoans': np.random.randint(0, 5, n),
    'MonthlyDebt': np.random.randint(200, 3000, n),
    'LoanTerm': np.random.choice([12, 36, 60], n),
    'PreviousDefault': np.random.choice(['Yes', 'No'], n),
    'HomeOwnership': np.random.choice(['Rent', 'Own', 'Mortgage'], n),
    'Default': np.random.choice([0, 1], n, p=[0.8, 0.2])
})

print("\nStep 1: Sample data created successfully!")
print("Dataset shape:", df.shape)
print(df.head())

# 2. Separate inputs and answer
X = df.drop('Default', axis=1)
y = df['Default']

print("\nStep 2: Features and target separated!")
print("Features shape:", X.shape)
print("Target shape:", y.shape)

# 3. Prepare numerical and categorical columns
num_cols = [
    'Age', 'Income', 'LoanAmount', 'CreditScore',
    'EmploymentYears', 'ExistingLoans', 'MonthlyDebt', 'LoanTerm'
]
cat_cols = ['PreviousDefault', 'HomeOwnership']

print("\nStep 3: Numerical and categorical columns identified!")
print("Numerical columns:", num_cols)
print("Categorical columns:", cat_cols)

# 4. Scale numbers and convert text into numbers
preprocessor = ColumnTransformer([
    ('numbers', StandardScaler(), num_cols),
    ('categories', OneHotEncoder(
        drop='first', handle_unknown='ignore'
    ), cat_cols)
])

print("\nStep 4: Preprocessing pipeline created successfully!")

# 5. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nStep 5: Data split completed!")
print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training targets:", y_train.shape)
print("Testing targets:", y_test.shape)

# 6. Prepare the data
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

print("\nStep 6: Data preprocessing completed!")
print("Transformed training data shape:", X_train.shape)
print("Transformed testing data shape:", X_test.shape)

# 7. Create the neural network
model = Sequential([
    Dense(64, activation='relu',
          input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

print("\nStep 7: Neural network created successfully!")
model.summary()

# 8. Configure the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
)

print("\nStep 8: Model compiled successfully!")
print("Optimizer: Adam")
print("Loss function: Binary Crossentropy")
print("Metrics: Accuracy and AUC")

# 9. Stop training when improvement stalls
stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

print("\nStep 9: Early stopping callback created!")
print("Training will stop if validation loss does not improve for 5 epochs.")

# 10. Train the model
print("\nStep 10: Starting model training...")

history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=[stop],
    verbose=1
)

print("\nStep 10: Model training completed!")
print("Epochs actually completed:", len(history.history['loss']))

# 11. Test the model
print("\nStep 11: Testing the model...")

probabilities = model.predict(X_test, verbose=0).ravel()
predictions = (probabilities >= 0.5).astype(int)

print("Predictions generated successfully!")
print("First 10 probabilities:", probabilities[:10])
print("First 10 predicted classes:", predictions[:10])

# Calculate performance
accuracy = accuracy_score(y_test, predictions)
auc = roc_auc_score(y_test, probabilities)

print("\nStep 12: Model evaluation completed!")
print(f"Test Accuracy: {accuracy:.4f}")
print(f"Test AUC-ROC: {auc:.4f}")

print("\nAll steps completed successfully!")
