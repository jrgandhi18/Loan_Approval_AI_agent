import pandas as pd
import time
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the specific .env file
load_dotenv("api_key_groq.env") 
api_key = os.getenv("GROQ_API_KEY")
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
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# 2. Load the data
test_df = pd.read_csv('final_test_cleaned.csv')

# 3. Processing TOP 10 and saving to CSV
results = []
num_to_process = 10  # Starting ke 10 records

print(f"🚀 Starting process for top {num_to_process} applicants...")
print("-" * 50)

for i in range(num_to_process):
    row = test_df.iloc[i]
    loan_id = row['Loan_ID']
    
    print(f"🔄 Processing {i+1}/{num_to_process}: Loan ID {loan_id}...")
    
    decision = get_groq_loan_report(row)
    
    results.append({
        "Loan_ID": loan_id,
        "AI_Analysis": decision
    })
    
    # Rate limit se bachne ke liye chota gap
    time.sleep(0.5)

# 4. Create DataFrame and Save
output_df = pd.DataFrame(results)
output_df.to_csv('ai_loan_decisions.csv', index=False)

print("-" * 50)
print(f"✅ Done! Top {num_to_process} records saved in 'ai_loan_decisions.csv'")