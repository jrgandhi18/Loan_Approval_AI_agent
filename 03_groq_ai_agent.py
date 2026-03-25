import pandas as pd
import time
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the specific .env file
# Agar ye file folder ke bahar nahi hai, toh ye kaam karna chahiye
load_dotenv("api_key_groq.env") 

# Check if key is actually loaded
api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    print("❌ ERROR: Key nahi mili! Check karo:")
    print("1. Kya 'api_key_groq.env' file isi folder mein hai?")
    print("2. Kya file ke andar 'GROQ_API_KEY=your_key' likha hai?")
    exit() # Stop the script if no key
else:
    print("✅ Key Successfully Loaded!")

client = Groq(api_key=api_key)

def get_groq_loan_report(row):
    prompt = f"""
    Analyze this loan application and give a decision:
    - Total Income: {row['Total_Income']}
    - Loan Amount: {row['LoanAmount']}
    - Credit History: {row['Credit_History']}
    - Education: {row['Education']}
    
    Decision format: [Approved/Rejected] - Reason in 1 sentence.
    """
    try:
        completion = client.chat.completions.create(
            # MODEL NAME UPDATED HERE
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# 2. Load the data
test_df = pd.read_csv('final_test_cleaned.csv')

# 3. Testing only TOP 3
print(f"🧐 Testing top 3 records...\n")
print("-" * 50)

for i in range(3):
    row = test_df.iloc[i]
    loan_id = row['Loan_ID']
    print(f"🔍 Analyzing Loan ID: {loan_id}...")
    decision = get_groq_loan_report(row)
    print(f"🤖 AI Response: {decision}")
    print("-" * 50)
    time.sleep(1)

print("\n✅ Terminal test complete!")



'''
✅ Terminal test complete!
PS C:\Codeplayground\DATASCIENCE\Loan_Approval_AI_agent> python .\03_groq_ai_agent.py
✅ Key Successfully Loaded!
🧐 Testing top 3 records...

--------------------------------------------------
🔍 Analyzing Loan ID: LP001015...
🤖 AI Response: [Approved] - The applicant's total income ($5720.0) is sufficient to repay the loan amount ($110.0) easily, and their credit history (1.0) suggests they have some experience with loans.
--------------------------------------------------
🔍 Analyzing Loan ID: LP001022...
🤖 AI Response: Rejected - The loan amount of 126.0 is relatively small compared to the total income, but the low credit history of 1.0 suggests a limited ability to repay loans.
--------------------------------------------------
🔍 Analyzing Loan ID: LP001031...
🤖 AI Response: [Approved] - The applicant's relatively low loan amount and stable income, combined with a good education level, outweigh the limited credit history, making them a moderate risk.
--------------------------------------------------

✅ Terminal test complete!
PS C:\Codeplayground\DATASCIENCE\Loan_Approval_AI_agent> 


'''