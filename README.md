
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

---

## 📁 Data Source

All financial data used in this project was sourced from [Yahoo Finance](https://finance.yahoo.com/) using the `yfinance` Python library. Tickers include major companies across tech, energy, and finance sectors for a diversified portfolio analysis.

---

## 📁 Repo Structure

│
├── 📄 README.md                # Project overview, visuals, and how-to
├── 📄 requirements.txt         # List of Python dependencies (e.g., numpy, pandas, yfinance)
├── 📄 .gitignore               # Files to ignore in Git (e.g., .ipynb_checkpoints/)
│
├── 📁 data/                    # Raw and/or cleaned datasets
│   └── historical_prices.csv   # (Optional) Local copy of Yahoo Finance data
│
├── 📁 notebooks/               # Jupyter notebooks for experiments, EDA, and core analysis
│   └── mean_variance_optimization.ipynb
│
├── 📁 scripts/                 # Python scripts (for modular, reusable code)
│   ├── optimizer.py            # Functions for Sharpe Ratio, risk, returns, etc.
│   └── utils.py                # Helper functions (e.g., for plotting or data handling)
│
├── 📁 images/                  # Plots and visuals for README or presentation
│   ├── efficient_frontier.png
│   └── sharpe_ratio_plot.png
│
└── 📁 results/                 # Output files, plots, logs, or final portfolios
    └── optimized_portfolio.json
