import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Creating Poro-Perm Crossplots with Seaborn

        ## Import the Required Libraries
        """
    )
    return


@app.cell
def _():
    import seaborn as sns
    import pandas as pd
    return pd, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Read the CSV Data
        """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv("Data/15_9-19A-CORE.csv", na_values=' ')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Create a Simple Scatter Plot
        """
    )
    return


@app.cell
def _(df, sns):
    sns.scatterplot(x=df['CPOR'], y=df['CKHL']);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Change the Y-Axis to Logarithmic
        """
    )
    return


@app.cell
def _(df, sns):
    _p = sns.scatterplot(x=df['CPOR'], y=df['CKHL'])
    _p.set(yscale='log')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Add a Third Variable for Colour
        """
    )
    return


@app.cell
def _(df, sns):
    _p = sns.scatterplot(x=df['CPOR'], y=df['CKHL'], hue=df['CGD'], palette='YlOrRd', s=100)
    _p.set(yscale='log')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Tidy up the Plot Labels
        """
    )
    return


@app.cell
def _(df, sns):
    _p = sns.scatterplot(x=df['CPOR'], y=df['CKHL'], hue=df['CGD'], palette='YlOrRd', s=100)
    _p.set(yscale='log')
    _p.set_ylabel('Core Permeability (mD)')
    _p.set_xlabel('Core Porosity (%)')
    return


@app.cell
def _(df, sns):
    _p = sns.scatterplot(x=df['CPOR'], y=df['CKHL'], hue=df['CGD'], palette='YlOrRd', s=100)
    _p.set(yscale='log')
    _p.set_ylabel('Core Permeability (mD)', fontsize=12, fontweight='bold')
    _p.set_xlabel('Core Porosity (%)', fontsize=12, fontweight='bold')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Change the Figure Size
        """
    )
    return


@app.cell
def _(df, sns):
    sns.set(rc={'figure.figsize': (15, 8)})
    _p = sns.scatterplot(x=df['CPOR'], y=df['CKHL'], hue=df['CGD'], palette='YlOrRd', s=100)
    _p.set(yscale='log')
    _p.set_ylabel('Core Permeability (mD)', fontsize=12, fontweight='bold')
    _p.set_xlabel('Core Porosity (%)', fontsize=12, fontweight='bold')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
