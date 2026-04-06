from pathlib import Path

import pandas as pd

from src.data_loader import download_prices, compute_returns
from src.benchmark import equal_weight_portfolio, portfolio_returns
from src.optimizer import optimize_cvar
from src.plots import plot_cumulative_returns, plot_drawdowns, plot_weights

BASE_DIR = Path(__file__).resolve().parent.parent


def main():
    tickers = ["SPY", "QQQ", "IWM", "EFA", "AGG", "GLD"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    output_dir = BASE_DIR / "outputs"
    output_dir.mkdir(exist_ok=True)

    prices = download_prices(tickers, start_date, end_date)
    returns = compute_returns(prices)

    eq_weights = equal_weight_portfolio(len(tickers))
    eq_port_returns = portfolio_returns(returns, eq_weights)

    result = optimize_cvar(returns)

    cvar_weights_series = result["weights"]
    status = result["status"]
    objective_value = result["objective"]

    cvar_port_returns = portfolio_returns(returns, cvar_weights_series.values)

    print("\nCVaR Weights")
    print(cvar_weights_series)

    print(f"\nOptimization Status: {status}")
    print(f"Objective Value: {objective_value}")
    print(f"VaR Threshold: {result['var_threshold']}")

    eq_cum = (1 + eq_port_returns).cumprod()
    cvar_cum = (1 + cvar_port_returns).cumprod()

    summary = pd.DataFrame(
        {
            "Metric": [
                "Annual Return",
                "Annual Volatility",
                "Sharpe Ratio",
                "Max Drawdown",
            ],
            "Equal Weight": [
                eq_port_returns.mean() * 252,
                eq_port_returns.std() * (252**0.5),
                (eq_port_returns.mean() / eq_port_returns.std()) * (252**0.5),
                (eq_cum / eq_cum.cummax() - 1).min(),
            ],
            "CVaR Portfolio": [
                cvar_port_returns.mean() * 252,
                cvar_port_returns.std() * (252**0.5),
                (cvar_port_returns.mean() / cvar_port_returns.std()) * (252**0.5),
                (cvar_cum / cvar_cum.cummax() - 1).min(),
            ],
        }
    )

    summary_path = output_dir / "performance_summary.csv"
    summary.to_csv(summary_path, index=False)

    plot_cumulative_returns(
        eq_port_returns,
        cvar_port_returns,
        output_dir / "cumulative_returns.png",
    )

    plot_drawdowns(
        eq_port_returns,
        cvar_port_returns,
        output_dir / "drawdowns.png",
    )

    plot_weights(
        cvar_weights_series,
        output_dir / "cvar_weights.png",
    )

    print("\nSaved files:")
    print(output_dir / "performance_summary.csv")
    print(output_dir / "cumulative_returns.png")
    print(output_dir / "drawdowns.png")
    print(output_dir / "cvar_weights.png")


if __name__ == "__main__":
    main()