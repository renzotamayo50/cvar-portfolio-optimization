# CVaR Portfolio Optimization

## Overview
This project builds a portfolio optimization framework using Conditional Value-at-Risk (CVaR), a downside risk metric that focuses on expected losses in the worst tail of return scenarios. The model is compared against a standard equal-weight portfolio.

## Objective
Minimize portfolio tail risk using CVaR under long-only constraints and compare the resulting portfolio to a benchmark equal-weight allocation.

## Tools
- Python
- PyCharm
- yfinance
- pandas
- numpy
- matplotlib
- CVXPY

## Methodology
1. Download historical ETF prices with yfinance
2. Compute daily returns
3. Build an equal-weight benchmark portfolio
4. Optimize portfolio weights by minimizing CVaR
5. Evaluate both portfolios using:
   - Annual Return
   - Annual Volatility
   - Sharpe Ratio
   - Max Drawdown
   - VaR 95%
   - CVaR 95%

## Portfolio Universe
- SPY
- QQQ
- IWM
- EFA
- AGG
- GLD

## Outputs
- performance_summary.csv
- cumulative_returns.png
- drawdowns.png
- cvar_weights.png

## How to Run
```bash
python3 src/main.py