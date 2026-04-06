from pathlib import Path

import pandas as pd

from src.data_loader import download_prices, compute_returns
from src.benchmark import (
    equal_weight_portfolio,
    portfolio_returns,
    performance_summary,
)
from optimizer import optimize_cvar
from plots import plot_cumulative_returns, plot_drawdowns, plot_weights


def main():
    tickers = ["SPY", "QQQ", "IWM", "EFA", "AGG", "GLD"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    output_dir = Path("../.venv/outputs")
    output_dir.mkdir(exist_ok=True)

    prices = download_prices(tickers, start_date, end_date)
    returns = compute_returns(prices)

    eq_weights = equal_weight_portfolio(len(tickers))
    eq_port_returns = portfolio_returns(returns, eq_weights)
    eq_summary = performance_summary(eq_port_returns)

    cvar_result = optimize_cvar(returns, beta=0.95)
    cvar_weights = cvar_result["weights"]
    cvar_port_returns = portfolio_returns(returns, cvar_weights.values)
    cvar_summary = performance_summary(cvar_port_returns)

    print("\nEqual Weight Portfolio")
    print(eq_summary)

    print("\nCVaR Optimized Portfolio")
    print(cvar_summary)

    print("\nCVaR Weights")
    print(cvar_weights)
    print("\nOptimization Status:", cvar_result["status"])
    print("Objective Value:", cvar_result["objective"])

    summary_table = pd.DataFrame({
        "Equal Weight": eq_summary,
        "CVaR Optimized": cvar_summary,
    })
    summary_table.to_csv(output_dir / "performance_summary.csv")

    plot_cumulative_returns(
        eq_port_returns,
        cvar_port_returns,
        output_dir / "cumulative_returns.png"
    )
    plot_drawdowns(
        eq_port_returns,
        cvar_port_returns,
        output_dir / "drawdowns.png"
    )
    plot_weights(
        cvar_weights,
        output_dir / "cvar_weights.png"
    )

    print("\nSaved files:")
    print(output_dir / "performance_summary.csv")
    print(output_dir / "cumulative_returns.png")
    print(output_dir / "drawdowns.png")
    print(output_dir / "cvar_weights.png")


if __name__ == "__main__":
    main()