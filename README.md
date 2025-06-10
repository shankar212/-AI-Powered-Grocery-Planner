
# 🧠 AI-Powered Grocery Planner 🛒

A smart grocery planning application that automatically generates a weekly meal plan tailored to your dietary preferences, household size, and budget, and then builds a real-time shopping list using **Kroger's public API** and **Google Gemini 1.5 Flash**.

---

## 📌 Overview

This project is a full-stack AI-integrated grocery planning tool built using **Streamlit**, which combines:
- 🧠 Google **Gemini 1.5 Flash** to generate personalized 7-day meal plans.
- 🛒 **Kroger Product API** for real-time grocery inventory and pricing.
- 📄 PDF export of shopping lists.
- 🧮 Budget-aware item aggregation and cost calculation.
- **LIVE** : https://ai-powered-grocery-planner.streamlit.app/

---

## 🚀 Features

- **Dynamic Meal Planning**: AI generates a full weekly plan based on diet, household size, and budget.
- **Real-Time Inventory**: Connects with Kroger’s API to check prices and availability.
- **Custom Budget Handling**: Alerts when cost exceeds your limit and suggests adjustments.
- **Out-of-Stock Toggle**: Option to include or exclude unavailable products.
- **PDF Export**: One-click download of your shopping list.
- **Clean UI**: Built with Streamlit for interactive input and real-time updates.

---

## 🏗️ Tech Stack

| Technology     | Description                        |
|----------------|------------------------------------|
| `Streamlit`    | UI Framework for Python apps       |
| `Google Gemini`| Meal plan generation using LLM     |
| `Kroger API`   | Real-time product data             |
| `ReportLab`    | PDF generation in Python           |
| `Python`       | Core development language          |

---

## 📂 Project Structure

```
.
├── app.py                  # Streamlit frontend
├── gemini_planner.py       # Gemini 1.5 meal plan generator
├── kroger_api.py           # Product lookup using Kroger API
├── kroger_auth.py          # Auth token generator for Kroger
├── utils.py                # Shopping list & cost calculator
├── README.md               # Project documentation
```

---

## 🔑 How it Works

### 1. Meal Plan Generation
Uses the Gemini API to generate 7 days of meals and their ingredient lists based on:
- Dietary preference (e.g., Vegan)
- Household size (1–8 people)
- Budget ($10–300)

### 2. Inventory Match
For each ingredient, the app:
- Queries Kroger API for the best matching product.
- Fetches price and stock information.

### 3. Budget Analysis
- Aggregates duplicate ingredients.
- Calculates average price and total cost.
- Notifies the user if the total cost exceeds budget.

### 4. Exporting
- Allows users to export the shopping list as a downloadable PDF with pricing and stock status.

---

## 🔐 Setup & Usage

### 1. Install dependencies

```bash
pip install streamlit requests reportlab google-generativeai
```

### 2. Set up your API keys

- **Google Gemini Key**: Get from [Google AI Studio](https://makersuite.google.com/)
- **Kroger API**: Register and get credentials from [Kroger Developer Portal](https://developer.kroger.com)

Update code:

```python
# gemini_planner.py
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# kroger_auth.py
auth = ("KROGER_CLIENT_ID", "KROGER_CLIENT_SECRET")
```

### 3. Run the app

```bash
streamlit run app.py
```

---


## 📄 Example Output

![image](https://github.com/user-attachments/assets/da3a730d-9000-4b36-85dc-177fdb9159e5)
![image](https://github.com/user-attachments/assets/6f69cc80-eeae-4aaa-8503-8be4b1ada2eb)
![image](https://github.com/user-attachments/assets/17347bf2-a980-4a98-b395-bdbb84c85897)

**PDF Shopping List Preview:**

```
🧾 Grocery Shopping List
- Almond Milk — $2.49 (In stock)
- Quinoa — $3.29 (In stock)
- Kale — $1.99 (Out of stock)



...
Total Cost: $63.15
```

---

## ✍️ Add to Resume

**Project Title**: AI-Powered Grocery Planner with Gemini & Kroger API  
**Tech Stack**: Python, Streamlit, Google Gemini, REST APIs, ReportLab  
**Description**:
> Developed an intelligent grocery planning web app that generates personalized weekly meal plans and real-time shopping lists by integrating Google Gemini 1.5 Flash with Kroger’s live inventory API. Included cost analysis, PDF export, and budget alert features.

---

## 📬 Contact

> Created by **Shanker Rathod**  
> For questions or collaboration: [www.shankerr.me / https://www.linkedin.com/in/shanker-rathod-4a609421b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app]
