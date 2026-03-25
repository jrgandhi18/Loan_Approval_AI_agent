import pandas as pd

# 1. Load the files
train = pd.read_csv('train_data.csv')
test = pd.read_csv('test_data.csv')

# 2. Merge for uniform cleaning
df = pd.concat([train, test], ignore_index=True)

# 3. Basic Cleaning
# Filling Categorical nulls with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)

# Filling Numerical nulls with median
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

df.to_csv('cleaned_loan_data.csv', index=False)
print("✅ Step 1: Data Cleaned and Merged!")