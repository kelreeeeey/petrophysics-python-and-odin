import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### 4 - Displaying Core Data and Deriving a Poro Perm Relationship
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Created By: Andy McDonald
        <br><br>
        The following short tutorial illustrates the process of loading in core data from a CSV file, creating poro-perm crossplots, and deriving a poro-perm relationship using numpy.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    return np, pd, plt


@app.cell
def _(pd):
    core_data = pd.read_csv("Data/15_9-19A-CORE.csv", na_values=' ')
    return (core_data,)


@app.cell
def _(core_data):
    core_data.head()
    return


@app.cell
def _(core_data):
    core_data.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can make a quick scatter plot by:
        """
    )
    return


@app.cell
def _(core_data):
    core_data.plot(kind="scatter", x="CPOR", y="CKHG")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There is one main problem with previous plot. Poro-perm data is normally presented on semilog scale, where the y-axis is logarithmic and the x-axis set to linear. We can change this by using the yscale('log') method.
        """
    )
    return


@app.cell
def _(core_data, plt):
    core_data.plot(kind="scatter", x="CPOR", y="CKHG")
    plt.yscale('log')
    plt.grid(True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can further refine the scatter plot by removing the scientific notation on the y-axis.
        """
    )
    return


@app.cell
def _(core_data, plt):
    from matplotlib.ticker import FuncFormatter
    (_fig, _ax) = plt.subplots()
    _ax.axis([0, 40, 0.01, 100000])
    _ax.plot(core_data['CPOR'], core_data['CKHG'], 'bo')
    _ax.set_yscale('log')
    _ax.grid(True)
    _ax.set_ylabel('Core Perm (mD)')
    _ax.set_xlabel('Core Porosity (%)')
    for _axis in [_ax.yaxis, _ax.xaxis]:
        _formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
        _axis.set_major_formatter(_formatter)
    return (FuncFormatter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can derive a linear regression by using the polyfit function from numpy. As we are working with a semi-log plot, we need to calculate log base 10 of the core permeability.
        """
    )
    return


@app.cell
def _(core_data, np):
    import statsmodels.api as sm

    x = core_data['CPOR']
    y = np.log10(core_data['CKHG'])

    model = sm.OLS(y, x, missing='drop')
    results = model.fit()
    return model, results, sm, x, y


@app.cell
def _(results):
    results.summary()
    return


@app.cell
def _(core_data, np):
    x_1 = np.polyfit(core_data['CPOR'], np.log10(core_data['CKHG']), 1)
    return (x_1,)


@app.cell
def _(x_1):
    x_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The result of the regression is: $10^{(0.16911398  * CPOR - 1.61346487)}$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using the code from the previous plot, we can now add a new line with our x-axis set to porosity and our y-axis set to an equation. Note that we have to use the equation above to reverse the log base 10 function used when deriving the function.
        """
    )
    return


@app.cell
def _(FuncFormatter, core_data, plt, x_1):
    (_fig, _ax) = plt.subplots()
    _ax.axis([0, 30, 0.01, 10000])
    _ax.semilogy(core_data['CPOR'], core_data['CKH'], 'bo')
    _ax.grid(True)
    _ax.set_ylabel('Core Perm (mD)')
    _ax.set_xlabel('Core Porosity (%)')
    _ax.semilogy(core_data['CPOR'], 10 ** (x_1[0] * core_data['CPOR'] + x_1[1]), 'r-')
    for _axis in [_ax.yaxis, _ax.xaxis]:
        _formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
        _axis.set_major_formatter(_formatter)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Our next step is to calculate a predicted permeability using our new equation and add it as a new column in the pandas dataframe.
        """
    )
    return


@app.cell
def _(core_data, x_1):
    core_data['PRED_PERM'] = 10 ** (x_1[0] * core_data['CPOR'] + x_1[1])
    return


@app.cell
def _(core_data):
    core_data.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can then make a quick plot of our prediction vs the original measurement. To get an idea of how well the prediction did, we can add a 1 to 1 line to aid the visualisation.
        """
    )
    return


@app.cell
def _(core_data, plt):
    (_fig, _ax) = plt.subplots()
    _ax.axis([0.01, 10000, 0.01, 10000])
    _ax.loglog(core_data['CKH'], core_data['PRED_PERM'], 'bo')
    _ax.loglog([0.01, 10000], [0.01, 10000], 'r-')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
