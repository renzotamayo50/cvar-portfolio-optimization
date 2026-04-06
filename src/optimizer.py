import cvxpy as cp
import numpy as np
import pandas as pd


def optimize_cvar(returns, beta=0.95):
    """
    Minimize portfolio CVaR at confidence level beta.
    Long-only portfolio.
    """

    if returns.empty:
        raise ValueError("Returns DataFrame is empty.")

    r = returns.values
    n_scenarios, n_assets = r.shape

    w = cp.Variable(n_assets)
    alpha = cp.Variable()
    u = cp.Variable(n_scenarios)

    portfolio_losses = -r @ w

    cvar = alpha + (1 / ((1 - beta) * n_scenarios)) * cp.sum(u)

    constraints = [
        cp.sum(w) == 1,
        w >= 0,
        u >= 0,
        u >= portfolio_losses - alpha,
    ]

    problem = cp.Problem(cp.Minimize(cvar), constraints)
    problem.solve()

    if w.value is None:
        raise ValueError("Optimization failed. No solution found.")

    weights = pd.Series(w.value, index=returns.columns, name="Weight")

    return {
        "weights": weights,
        "status": problem.status,
        "objective": problem.value,
        "var_threshold": alpha.value,
    }


if __name__ == "__main__":
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    sample_returns = pd.DataFrame(
        np.random.normal(0.0005, 0.01, size=(500, 4)),
        columns=["SPY", "QQQ", "AGG", "GLD"]
    )

    result = optimize_cvar(sample_returns, beta=0.95)

    print("Status:", result["status"])
    print("Objective:", result["objective"])
    print("VaR threshold:", result["var_threshold"])
    print("\nWeights:")
    print(result["weights"])
    print("\nWeight sum:", result["weights"].sum())