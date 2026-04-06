# CVaR Portfolio Optimization

## Overview

This project builds a portfolio optimization framework using Conditional Value-at-Risk (CVaR), a downside risk metric that focuses on expected losses in the worst tail of return scenarios. The model is compared against a standard equal-weight portfolio to evaluate whether a downside-risk-focused allocation improves portfolio behavior.

## Objective

Minimize portfolio tail risk using CVaR under long-only constraints and compare the resulting portfolio to a simple equal-weight benchmark across key performance and risk metrics.

## Methodology

The workflow follows these steps:

1. Download historical adjusted close prices for a selected ETF universe.
2. Compute daily returns from the cleaned price data.
3. Build an equal-weight benchmark portfolio.
4. Solve a CVaR minimization problem using CVXPY.
5. Compare the optimized portfolio against the benchmark.
6. Export summary metrics and visualizations.

## Asset Universe

The model uses the following ETFs:

- SPY
- QQQ
- IWM
- EFA
- AGG
- GLD

These assets were selected to represent a diversified multi-asset allocation across U.S. equities, international equities, bonds, and gold.

## Optimization Approach

The optimization is implemented with CVXPY.

The model:

- minimizes Conditional Value-at-Risk at a chosen confidence level
- enforces long-only weights
- constrains portfolio weights to sum to 1
- estimates portfolio losses across historical return scenarios

This allows the portfolio to focus on limiting expected losses in the worst part of the return distribution rather than only minimizing total variance.

## Benchmark Comparison

The optimized portfolio is compared against an equal-weight benchmark using:

- Annual Return
- Annual Volatility
- Sharpe Ratio
- Max Drawdown

This comparison helps evaluate whether the CVaR portfolio provides stronger downside protection and different allocation behavior than a naive diversification approach.

## Outputs

The model generates the following output files in the `outputs/` folder:

- `performance_summary.csv`: summary table of annual return, annual volatility, Sharpe ratio, and max drawdown
- `cumulative_returns.png`: cumulative performance comparison between the equal-weight and CVaR portfolios
- `drawdowns.png`: drawdown comparison over time
- `cvar_weights.png`: final optimized portfolio weights

## Project Structure

```text
cvar-portfolio-optimization/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
├── outputs/
└── src/
    ├── benchmark.py
    ├── data_loader.py
    ├── main.py
    ├── optimizer.py
    └── plots.py
