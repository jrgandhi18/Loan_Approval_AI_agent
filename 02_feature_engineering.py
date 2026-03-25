import pandas as pd

df = pd.read_csv('cleaned_loan_data.csv')

# 1. Create Total Income (Applicant + Coapplicant)
df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# 2. Split back to Train and Test (Based on Loan_Status presence)
train_final = df[df['Loan_Status'].notnull()]
test_final = df[df['Loan_Status'].isnull()]

train_final.to_csv('final_train_cleaned.csv', index=False)
test_final.to_csv('final_test_cleaned.csv', index=False)

print("✅ Step 2: Feature Engineering Done. Files ready for AI!")