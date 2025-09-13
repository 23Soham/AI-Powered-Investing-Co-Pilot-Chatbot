# 📘 AI-Powered-Investing-Co-Pilot-Chatbot

> ⚠️ **Disclaimer**  
> This is a **study project** and an **AI co-pilot**. It is **not financial advice**.  
> Please do **not** trade using these suggestions. The goal is to showcase how **AI + financial data** can be combined to create **explainable insights**.

![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Pinecone](https://img.shields.io/badge/Vector%20DB-Pinecone-5C2D91)
![LLM](https://img.shields.io/badge/LLM-Gemini%201.5-4285F4)
![License](https://img.shields.io/badge/License-MIT-black)

---

## 📌 Overview
This project is an **AI-powered investing assistant** that blends **timeless investment principles** with **modern AI workflows**.  
Inspired by Peter Lynch’s philosophy, it combines **Retrieval-Augmented Generation (RAG)** with **live stock fundamentals** to deliver **explainable, beginner-friendly insights**.

**What it does**
- 💬 Chats like a **mentor-style assistant** (plain-English answers)
- 📊 Explains stock metrics (ROE, Debt/Equity, Growth, Margins, FCF)
- 🗺️ Visualizes portfolios (dashboards, value-vs-quality clustering, radar charts)
- ✅ Provides **Long / Hold / Short** calls with the **reason why**
- 🧭 Teaches **beginner tips** (color-coded: Green = Good, Yellow = Caution, Red = Avoid)

---

## 🎯 Problem Statement
Investors are overwhelmed by dashboards and noisy metrics, but lack **clear, principle-driven guidance**.  
Beginners especially struggle to connect numbers like **ROE** or **Debt/Equity** to real decisions.

---

## 💡 Solution
An **Investing Co-Pilot** that pairs **quantitative fundamentals** with **qualitative wisdom**, so users see:
1) *What the numbers say* and 2) *How to interpret them through investing principles*.

**Feature highlights**
- **Conversational Q&A:** “What is ROE?”, “When should I sell?” → **plain-English** answers  
- **Dashboards:** clean metric cards with **tooltips** for each fundamental  
- **Clustering:** **Value × Quality** map to spot outliers fast  
- **Recommendations:** color-coded **Long / Hold / Short** with rationale  
- **Education layer:** beginner tips woven into the UI

---

## ⚙️ Architecture

**Frontend**
- **Streamlit** — interactive chat & dashboards

**Backend**
- **FastAPI** — orchestrates prompts, retrieval, and data aggregation

**Intelligence Layer**
- **LLM:** **Gemini 1.5** (Google AI Studio)
- **Embeddings:** `paraphrase-MiniLM-L6-v2`
- **Vector DB:** **Pinecone** (stores ~**3,000** curated Q&A pairs with metadata)

**Data Sources**
- 📈 **Live stock fundamentals** (ROE, Debt/Equity, Margins, Growth, FCF) curated from **Yahoo Finance**
- 📚 **Peter Lynch Knowledge Base:** books (*One Up on Wall Street*, *Beating the Street*, *Learn to Earn*), speech/interview transcripts, and curated educational articles  
  → normalized into Q&A pairs for **RAG** retrieval


---

## 🖼️ Screenshots
Place screenshots in `docs/screens/` and reference as below.

1. **Chatbot (mentorship Q&A)**  

    <img width="1300" height="600" alt="Screenshot 2025-09-12 at 12 48 08 AM" src="https://github.com/user-attachments/assets/b42f1d72-4410-444f-8f4a-bb80c33a2227" />

   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 01 45 AM" src="https://github.com/user-attachments/assets/f317f87c-4855-4b21-99c2-63a22b816fc5" />



1. **Financial Dashboard (metrics + tooltips)**  
   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 04 44 AM" src="https://github.com/user-attachments/assets/d680aa02-5c4a-4e1a-ad25-c556ef051de1" />

<img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 07 12 AM" src="https://github.com/user-attachments/assets/f29a8053-3ebc-4cef-924d-ff2586f505a1" />


2. **Portfolio Summary (averages)**  
<img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 07 55 AM" src="https://github.com/user-attachments/assets/6aef673d-d609-4c16-9abf-827401e35401" />

3. **Value–Quality Clustering**  
   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 08 21 AM" src="https://github.com/user-attachments/assets/b8e5fadf-b514-4c74-8b73-388ed2ae6312" />


4. **Radar Comparison (2–3 tickers)**  
   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 12 48 AM" src="https://github.com/user-attachments/assets/b43e050a-1e45-4af2-8128-d63ed62598eb" />


5. **Recommendations (Long / Hold / Short + why)**  
   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 13 14 AM" src="https://github.com/user-attachments/assets/dc090770-29f2-4104-93aa-fdeb21e023cc" />


6. **Beginner Tips (color-coded)**  
   <img width="1300" height="600" alt="Screenshot 2025-09-12 at 1 13 46 AM" src="https://github.com/user-attachments/assets/829b9d1c-bea7-4f2e-bc48-d4628f8e7222" />


---

## 🚀 Getting Started

### 🔧 Prerequisites
- **Python** 3.9+  
- Accounts/API keys for:
  - **Google AI Studio** (Gemini 1.5)
  - **Pinecone**
  - **Yahoo Finance** (if you proxy/cache; otherwise `yfinance` library)

### 📦 Installation
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
