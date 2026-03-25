# 🏦 AI-Powered autonomous Loan Approval Agent

> Leveraging Large Language Models (LLMs) to automate and intelligently streamline the credit assessment process. This is an end-to-end data product with real-time inference capability.

---

## 📖 Executive Summary
Traditional loan approval processes are often manual, slow, and rule-based. This project engineers a solution by introducing an **AI Agent** powered by **Groq Cloud's Llama 3.1** model. It acts as an autonomous **Credit Risk Officer**, analyzing applicant data to provide a final decision (Approved/Rejected) accompanied by a structured, logical reasoning—all within sub-second latency.

---

## 🛠️ Integrated Technology Stack & Engineering
This project demonstrates the seamless integration of **Data Engineering**, **Machine Learning Inference**, and **Rapid Application Development**.

| Domain | Technolgoy | Role & Engineering Application |
| :--- | :--- | :--- |
| **Data Engineering** | **Python (Pandas, NumPy)** | Data Ingestion, Merge Strategies, Null Imputation, and Feature Transformation. |
| **Generative AI** | **Groq SDK (Llama 3.1 Model)** | **Prompt Engineering** and **Zero-Shot Learning** for classification with reasoning. |
| **Deployment** | **Streamlit** | Built a responsive **Single-Page Application (SPA)** for real-time model interaction. |
| **DevOps** | **Python-Dotenv, Git, .gitignore** | Managing sensitive configuration (`.env` files) and maintaining a clean source control. |

---

## 📂 System Architecture & Data Flow
The system follows a modular pipeline design, ensuring scalability and maintainability.

```mermaid
graph TD
    A[train_data.csv / test_data.csv] -->|ETL| B(01_eda_DataCleaning.py)
    B -->|Cleaned DataFrame| C(02_feature_engineering.py)
    C -->|Creates Total_Income & Log Transf.| D(final_test_cleaned.csv)
    
    %% Real-time Predictor Flow
    subgraph "Real-time Inference (Streamlit)"
        E(User Manual Input) -->|JSON Data| G(05_streamlit_ui.py)
        G -->|API Request| H(Groq Cloud API)
        H -->|AI Decision + Reasoning| G
    end
    
    %% Batch Processing Flow
    subgraph "Batch Processing"
        D --> F(03_groq_ai_agent.py)
        F -->|Prompt Engineering| H
        H -->|Processed Results| I(ai_loan_decisions.csv)
    end
