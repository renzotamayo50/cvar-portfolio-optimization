import matplotlib.pyplot as plt
import pandas as pd


def plot_cumulative_returns(equal_weight_returns, cvar_returns, save_path):
    eq_cum = (1 + equal_weight_returns).cumprod()
    cvar_cum = (1 + cvar_returns).cumprod()

    plt.figure(figsize=(10, 6))
    plt.plot(eq_cum, label="Equal Weight")
    plt.plot(cvar_cum, label="CVaR Optimized")
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_drawdowns(equal_weight_returns, cvar_returns, save_path):
    eq_cum = (1 + equal_weight_returns).cumprod()
    cvar_cum = (1 + cvar_returns).cumprod()

    eq_dd = eq_cum / eq_cum.cummax() - 1
    cvar_dd = cvar_cum / cvar_cum.cummax() - 1

    plt.figure(figsize=(10, 6))
    plt.plot(eq_dd, label="Equal Weight")
    plt.plot(cvar_dd, label="CVaR Optimized")
    plt.title("Drawdowns")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_weights(weights, save_path):
    plt.figure(figsize=(10, 6))
    weights.sort_values(ascending=False).plot(kind="bar")
    plt.title("CVaR Optimized Portfolio Weights")
    plt.xlabel("Asset")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()