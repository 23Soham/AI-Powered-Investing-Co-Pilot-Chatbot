# AI-Powered-Investing-Co-Pilot-Chatbot

# 📘 AI-Powered Investing Co-Pilot

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

> _Tip:_ Add an architecture diagram image at `docs/architecture.png` and reference it here:
>
> ![Architecture](docs/architecture.png)

---

## 🖼️ Screenshots
Place screenshots in `docs/screens/` and reference as below.

1. **Chatbot (mentorship Q&A)**  
   ![Chatbot](docs/screens/chat.png)

2. **Financial Dashboard (metrics + tooltips)**  
   ![Dashboard](docs/screens/dashboard.png)

3. **Portfolio Summary (averages)**  
   ![Summary](docs/screens/summary.png)

4. **Value–Quality Clustering**  
   ![Clustering](docs/screens/clusters.png)

5. **Radar Comparison (2–3 tickers)**  
   ![Radar](docs/screens/radar.png)

6. **Recommendations (Long / Hold / Short + why)**  
   ![Recs](docs/screens/recs.png)

7. **Beginner Tips (color-coded)**  
   ![Tips](docs/screens/tips.png)

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
