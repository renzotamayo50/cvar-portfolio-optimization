import pandas as pd
import yfinance as yf


def download_prices(tickers, start_date, end_date):
    """
    Download adjusted close prices for a list of tickers.
    """
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError("No price data was downloaded.")

    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"].copy()
    else:
        prices = data.copy()

    prices = prices.dropna(how="all")

    if prices.empty:
        raise ValueError("Price data is empty after cleaning.")

    return prices


def compute_returns(prices):
    """
    Compute daily percentage returns from price data.
    """
    returns = prices.pct_change().dropna(how="any")

    if returns.empty:
        raise ValueError("Return data is empty after pct_change().")

    return returns


if __name__ == "__main__":
    tickers = ["SPY", "QQQ", "IWM", "EFA", "AGG", "GLD"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    prices = download_prices(tickers, start_date, end_date)
    returns = compute_returns(prices)

    print("Prices head:")
    print(prices.head())
    print("\nReturns head:")
    print(returns.head())
    print("\nPrices shape:", prices.shape)
    print("Returns shape:", returns.shape)