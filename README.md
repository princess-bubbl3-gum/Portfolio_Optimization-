
# 📈 Portfolio Optimization in Python


## 🔧 Objective
This project builds a foundational **Mean-Variance Portfolio Optimization Model** using real financial data from S&P 500 companies. The goal is to minimize portfolio risk for a target return or maximize the Sharpe Ratio — a core principle of modern quantitative finance.

## 🚀 Why It Matters
- Portfolio optimization is widely used in **hedge funds, asset management**, and **fintech platforms** to **balance return and risk**.
- Understanding and implementing these models is a **high-demand skill** in data-driven finance, quant roles, and analytics.

---

## 🧠 What I Did

✅ Built a mean-variance optimized portfolio using:

- 📉 Log Returns & Annualized Metrics  
- 🧮 Covariance Matrix and Efficient Frontier  
- 📊 Volatility-Minimizing & Sharpe Ratio-Maximizing Portfolios  
- 🔁 Constraints: Full Investment, Return Target, Bounds  
- 🛠️ `scipy.optimize.minimize` with custom objective functions  
- 🖼️ Visualizations with **annotations and efficient frontier** highlighting  


## 📸 Visual Preview

*(Optional — add an image of your Efficient Frontier chart)*  

yaml
Copy
Edit
> Tip: Store images in an `/assets` folder and use relative links.

---

## 📁 Data Source

All financial data used in this project was sourced from [Yahoo Finance](https://finance.yahoo.com/) using the `yfinance` Python library. Tickers include major companies across tech, energy, and finance sectors for a diversified portfolio analysis.

---

## 📁 Repo Structure

```bash
├── portfolio_optimization.ipynb    # Main Jupyter notebook with code and visualizations
├── requirements.txt                # Python dependencies
├── data/                           # Historical price or return data (if included)
├── assets/                         # Plots or figures
