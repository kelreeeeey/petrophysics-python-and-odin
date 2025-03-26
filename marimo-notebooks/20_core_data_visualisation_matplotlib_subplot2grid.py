import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Importing Libraries and Data
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    import lasio
    return lasio, pd, plt


@app.cell
def _(pd):
    df = pd.read_csv('Data/15_9-19A-CORE.csv')
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating the Figure With Subplots
        """
    )
    return


@app.cell
def _(df, plt):
    (_fig, _ax) = plt.subplots(figsize=(10, 10))
    _ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), rowspan=3)
    _ax2 = plt.subplot2grid(shape=(3, 3), loc=(0, 1), rowspan=3)
    _ax3 = plt.subplot2grid(shape=(3, 3), loc=(0, 2))
    _ax4 = plt.subplot2grid(shape=(3, 3), loc=(1, 2))
    _ax5 = plt.subplot2grid(shape=(3, 3), loc=(2, 2))
    _ax1.scatter(df['CPOR'], df['DEPTH'], marker='.', c='red')
    _ax1.set_xlim(0, 50)
    _ax1.set_ylim(4010, 3825)
    _ax1.set_title('Core Porosity')
    _ax1.grid()
    _ax2.scatter(df['CKHG'], df['DEPTH'], marker='.', c='blue')
    _ax2.set_xlim(0.01, 10000)
    _ax2.semilogx()
    _ax2.set_ylim(4010, 3825)
    _ax2.set_title('Core Permeability')
    _ax2.grid()
    _ax3.scatter(df['CPOR'], df['CKHG'], marker='.', alpha=0.5)
    _ax3.semilogy()
    _ax3.set_xlim(0.01, 10000)
    _ax3.set_xlim(0, 50)
    _ax3.set_title('Poro-Perm Scatter Plot')
    _ax3.set_xlabel('Core Porosity (%)')
    _ax3.set_ylabel('Core Permeability (mD)')
    _ax3.grid()
    _ax4.hist(df['CPOR'], bins=30, edgecolor='black', color='red', alpha=0.6)
    _ax4.set_xlabel('Core Porosity')
    _ax5.hist(df['CGD'], bins=30, edgecolor='black', color='blue', alpha=0.6)
    _ax5.set_xlabel('Core Grain Density')
    plt.tight_layout()
    plt.savefig('CoreDataDashBoard.png', dpi=300)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Adding Interpreted Data as Line Plots
        """
    )
    return


@app.cell
def _(lasio):
    cpi = lasio.read('Data/15_9-19_A_CPI.las').df()
    cpi['PHIF']=cpi['PHIF']*100
    cpi.columns
    return (cpi,)


@app.cell
def _(cpi, df, plt):
    (_fig, _ax) = plt.subplots(figsize=(10, 10))
    _ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), rowspan=3)
    _ax2 = plt.subplot2grid(shape=(3, 3), loc=(0, 1), rowspan=3)
    _ax3 = plt.subplot2grid(shape=(3, 3), loc=(0, 2), rowspan=1)
    _ax4 = plt.subplot2grid(shape=(3, 3), loc=(1, 2), rowspan=1)
    _ax5 = plt.subplot2grid(shape=(3, 3), loc=(2, 2), rowspan=1)
    _ax1.scatter(df['CPOR'], df['DEPTH'], marker='.', c='red')
    _ax1.plot(cpi['PHIF'], cpi.index, c='black', lw=0.5)
    _ax1.set_xlim(0, 50)
    _ax1.set_ylim(4010, 3825)
    _ax1.set_title('Core Porosity')
    _ax1.grid()
    _ax2.scatter(df['CKHG'], df['DEPTH'], marker='.')
    _ax2.plot(cpi['KLOGH'], cpi.index, c='black', lw=0.5)
    _ax2.set_xlim(0.01, 100000)
    _ax2.set_ylim(4010, 3825)
    _ax2.semilogx()
    _ax2.set_title('Core Permeability')
    _ax2.grid()
    _ax3.scatter(df['CPOR'], df['CKHG'], marker='.', alpha=0.5)
    _ax3.semilogy()
    _ax3.set_ylim(0.01, 100000)
    _ax3.set_xlim(0, 50)
    _ax3.set_title('Poro-Perm Crossplot')
    _ax3.set_xlabel('Core Porosity (%)')
    _ax3.set_ylabel('Core Permeability (mD)')
    _ax3.grid()
    _ax4.hist(df['CPOR'], bins=30, edgecolor='black', color='red')
    _ax4.set_xlabel('Core Porosity')
    _ax5.hist(df['CGD'], bins=30, edgecolor='black', color='green')
    _ax5.set_xlabel('Core Grain Density')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
