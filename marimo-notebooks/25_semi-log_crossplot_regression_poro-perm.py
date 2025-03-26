import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Import the Libraries and Data
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    return np, pd, plt, sns


@app.cell
def _(pd):
    df = pd.read_csv("Data/15_9-19A-CORE.csv", na_values=' ', usecols=['DEPTH', 'CPOR', 'CKHL', 'CGD'])
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    #Drop nans
    df.dropna(inplace=True)
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Visualise our Data
        """
    )
    return


@app.cell
def _(df, plt):
    _p = plt.scatter(x=df['CPOR'], y=df['CKHL'], c=df['CGD'], cmap='YlOrRd', s=50)
    plt.semilogy()
    plt.ylabel('Core Permeability (mD)', fontsize=12, fontweight='bold')
    plt.xlabel('Core Porosity (%)', fontsize=12, fontweight='bold')
    plt.colorbar(_p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Build a Linear Regression Model
        """
    )
    return


@app.cell
def _():
    from sklearn.linear_model import LinearRegression
    return (LinearRegression,)


@app.cell
def _(df, np):
    x = df['CPOR'].values
    y = np.log10(df['CKHL'].values)
    return x, y


@app.cell
def _(y):
    y.shape
    return


@app.cell
def _(x, y):
    x_1 = x.reshape(-1, 1)
    y_1 = y.reshape(-1, 1)
    return x_1, y_1


@app.cell
def _(LinearRegression):
    model = LinearRegression()
    return (model,)


@app.cell
def _(model, x_1, y_1):
    model.fit(x_1, y_1)
    return


@app.cell
def _(model, x_1, y_1):
    r2 = model.score(x_1, y_1)
    r2
    return (r2,)


@app.cell
def _(model):
    model.intercept_
    return


@app.cell
def _(model):
    model.coef_
    return


@app.cell
def _(model):
    regression_eq = f'10**({model.coef_[0][0]:.4f} * CPOR + ({model.intercept_[0]:.4f}))'
    print(regression_eq)
    return (regression_eq,)


@app.cell
def _(model, np):
    x_plot_vals = np.arange(0, 50)
    y_pred = model.predict(x_plot_vals.reshape(-1,1))
    return x_plot_vals, y_pred


@app.cell
def _(y_pred):
    y_pred_log = 10**y_pred
    return (y_pred_log,)


@app.cell
def _(pd, x_plot_vals, y_pred_log):
    results_df = pd.DataFrame({'por_vals': x_plot_vals, 'perm_vals': y_pred_log.flatten()})
    results_df
    return (results_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plot the Results
        """
    )
    return


@app.cell
def _(df, plt, results_df):
    _p = plt.scatter(x=df['CPOR'], y=df['CKHL'], c=df['CGD'], cmap='YlOrRd', s=50)
    plt.plot(results_df['por_vals'], results_df['perm_vals'], color='black')
    plt.semilogy()
    plt.ylabel('Core Permeability (mD)', fontsize=12, fontweight='bold')
    plt.xlabel('Core Porosity (%)', fontsize=12, fontweight='bold')
    plt.colorbar(_p)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
