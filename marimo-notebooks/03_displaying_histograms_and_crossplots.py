import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 3 - Displaying Histograms and Crossplots
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Created by: Andy McDonald
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The following tutorial illustrates how to display well data from a LAS file on histograms and crossplots.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Loading Well Data from CSV
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The following cells load data in from a CSV file and replace the null values (-999.25) with Not a Number (NaN) values. More detail can be found in 1. Loading and Displaying Well Data From CSV.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell
def _(pd):
    well = pd.read_csv("data/L0509WellData.csv", header=0)
    return (well,)


@app.cell
def _(np, well):
    well.replace(-999.25, np.nan, inplace=True)
    return


@app.cell
def _(well):
    well
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Displaying data on a histogram
        """
    )
    return


@app.cell
def _(plt, well):
    mean = well['GR'].mean()
    p5 = well['GR'].quantile(0.05)
    p95 = well['GR'].quantile(0.95)

    plt.figure(figsize=(6,4), dpi=300)
    well['GR'].plot(kind='hist', bins=30, color='red', alpha=0.5, edgecolor='black')
    plt.xlabel('Gamma Ray', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xlim(0,200)

    plt.axvline(mean, color='blue', label='mean')
    plt.axvline(p5, color='green', label='5th Percentile')
    plt.axvline(p95, color='purple', label='95th Percentile')

    plt.legend()
    plt.show()
    return mean, p5, p95


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Displaying a simple histogram can be done by calling the .hist function on the well dataframe and specifying the column.
        """
    )
    return


@app.cell
def _(well):
    well.hist(column="GR")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The number of bins can be controled by the bins parameter:
        """
    )
    return


@app.cell
def _(well):
    well.hist(column="GR", bins = 30)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also change the opacity of the bars by using the alpha parameter:
        """
    )
    return


@app.cell
def _(well):
    well.hist(column="GR", bins = 30, alpha = 0.5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Plotting multiple histograms on one plot
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It can be more efficient to loop over the columns (curves) within the dataframe and create a plot with multiple histograms, rather than duplicating the previous line multiple times. <br><br>

        First we need to create a list of our curve names.
        """
    )
    return


@app.cell
def _(well):
    cols_to_plot = list(well)
    return (cols_to_plot,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can remove the depth curve from our list and focus on our curves. The same line can be applied to other curves that need removing.
        """
    )
    return


@app.cell
def _(cols_to_plot):
    cols_to_plot.remove("DEPTH")
    return


@app.cell
def _(cols_to_plot, plt, well):
    rows = 3
    cols = 2
    _fig = plt.figure(figsize=(10, 10))
    for (i, feature) in enumerate(cols_to_plot):
        _ax = _fig.add_subplot(rows, cols, i + 1)
        well[feature].hist(bins=20, ax=_ax, facecolor='green', alpha=0.6)
        _ax.set_title(feature + ' Distribution')
        _ax.set_axisbelow(True)
        _ax.grid(color='whitesmoke')
    plt.tight_layout()
    plt.show()
    return cols, feature, i, rows


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Displaying data on a crossplot (Scatterplot)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As seen in the first notebook, we can display a crossplot by simply doing the following. using the c argument we can add a third curve to colour the data.
        """
    )
    return


@app.cell
def _(well):
    well.plot(kind="scatter", x="NPHI", y="RHOB", c="GR", 
              colormap="YlOrRd_r", ylim=(3,2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can take the above crossplot and create a 3D version. First we need to make sure the Jupyter notbook is setup for displaying interactive 3D plots using the following command.
        """
    )
    return


@app.cell
def _():
    # '%matplotlib inline' command supported automatically in marimo
    return


@app.cell
def _(plt, well):
    from mpl_toolkits.mplot3d import Axes3D
    _fig = plt.figure(figsize=(5, 5))
    _ax = _fig.add_subplot(111, projection='3d')
    _ax.scatter(well['NPHI'], well['RHOB'], well['GR'], alpha=0.3, c='r')
    return (Axes3D,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we want to have multiple crossplots on view, we can do this by:
        """
    )
    return


@app.cell
def _(plt, well):
    (_fig, _ax) = plt.subplots(figsize=(10, 10))
    ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)
    ax1.scatter(x='NPHI', y='RHOB', data=well, marker='s', alpha=0.2)
    ax1.set_ylim(3, 1.8)
    ax1.set_ylabel('RHOB (g/cc)')
    ax1.set_xlabel('NPHI (dec)')
    ax2.scatter(x='GR', y='RHOB', data=well, marker='p', alpha=0.2)
    ax1.set_ylim(3, 1.8)
    ax2.set_ylabel('RHOB (g/cc)')
    ax2.set_xlabel('GR (API)')
    ax3.scatter(x='DT', y='RHOB', data=well, marker='*', alpha=0.2)
    ax3.set_ylim(3, 1.8)
    ax3.set_ylabel('RHOB (g/cc)')
    ax3.set_xlabel('DT (us/ft)')
    ax4.scatter(x='GR', y='DT', data=well, marker='D', alpha=0.2)
    ax4.set_ylabel('DT (us/ft)')
    ax4.set_xlabel('GR (API)')
    plt.tight_layout()
    return ax1, ax2, ax3, ax4


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
