import numpy as np
import pandas as pd


TRADING_DAYS = 252


def equal_weight_portfolio(n_assets):
    if n_assets <= 0:
        raise ValueError("Number of assets must be positive.")
    return np.ones(n_assets) / n_assets


def portfolio_returns(returns, weights):
    return returns @ weights


def max_drawdown(return_series):
    cumulative = (1 + return_series).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative / running_max) - 1
    return drawdown.min()


def var_cvar(return_series, alpha=0.95):
    cutoff = np.percentile(return_series, (1 - alpha) * 100)
    tail_losses = return_series[return_series <= cutoff]

    var_95 = cutoff
    cvar_95 = tail_losses.mean()

    return var_95, cvar_95


def performance_summary(return_series, risk_free_rate=0.0):
    ann_return = return_series.mean() * TRADING_DAYS
    ann_vol = return_series.std() * np.sqrt(TRADING_DAYS)

    sharpe = np.nan
    if ann_vol > 0:
        sharpe = (ann_return - risk_free_rate) / ann_vol

    mdd = max_drawdown(return_series)
    var_95, cvar_95 = var_cvar(return_series, alpha=0.95)

    return pd.Series({
        "Annual Return": ann_return,
        "Annual Volatility": ann_vol,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": mdd,
        "VaR 95%": var_95,
        "CVaR 95%": cvar_95,
    })