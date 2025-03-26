import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 2. Displaying a Well Plot with Matplotlib
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
        The following tutorial illustrates displaying well data from a CSV on a custom matplotlib plot.
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
    well.replace(-999.00, np.nan, inplace=True)
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Setting up the logplot
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can quickly make a log plot using subplot2grid from matplotlib. This allows us to space out multiple plots (tracks) in an easy to understand way. <br><br>

        Each track is setup as an axis (ax for short)
        """
    )
    return


@app.cell
def _(plt, well):
    _fig = plt.subplots(figsize=(10, 10))
    _ax1 = plt.subplot2grid((1, 3), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 3), (0, 1), rowspan=1, colspan=1)
    _ax3 = plt.subplot2grid((1, 3), (0, 2), rowspan=1, colspan=1)
    _ax1.plot('GR', 'DEPTH', data=well, color='green')
    _ax1.set_title('Gamma')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylim(4850, 4600)
    _ax1.grid()
    _ax2.plot('RHOB', 'DEPTH', data=well, color='red')
    _ax2.set_title('Density')
    _ax2.set_xlim(1.95, 2.95)
    _ax2.set_ylim(4850, 4600)
    _ax2.grid()
    _ax3.plot('DT', 'DEPTH', data=well, color='purple')
    _ax3.set_title('Sonic')
    _ax3.set_xlim(140, 40)
    _ax3.set_ylim(4850, 4600)
    _ax3.grid()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Customising the Log Plot
        We can further customise the plot to look more like a familiar log plot, with the curve names and scales at the top and two curves (density & neutron) in the one track.
        """
    )
    return


@app.cell
def _(plt, well):
    (_fig, ax) = plt.subplots(figsize=(10, 10))
    _ax1 = plt.subplot2grid((1, 3), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 3), (0, 1), rowspan=1, colspan=1)
    _ax3 = plt.subplot2grid((1, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = _ax2.twiny()
    ax7 = _ax1.twiny()
    ax7.xaxis.set_visible(False)
    ax8 = _ax2.twiny()
    ax8.xaxis.set_visible(False)
    ax9 = _ax3.twiny()
    ax9.xaxis.set_visible(False)
    _ax1.plot('GR', 'DEPTH', data=well, color='green')
    _ax1.set_xlabel('Gamma')
    _ax1.xaxis.label.set_color('green')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylabel('Depth (m)')
    _ax1.tick_params(axis='x', colors='green')
    _ax1.spines['top'].set_edgecolor('green')
    _ax1.title.set_color('green')
    _ax1.set_xticks([0, 50, 100, 150, 200])
    _ax2.plot('RHOB', 'DEPTH', data=well, color='red')
    _ax2.set_xlabel('Density')
    _ax2.set_xlim(1.95, 2.95)
    _ax2.xaxis.label.set_color('red')
    _ax2.tick_params(axis='x', colors='red')
    _ax2.spines['top'].set_edgecolor('red')
    _ax2.set_xticks([1.95, 2.2, 2.45, 2.7, 2.95])
    _ax3.plot('DT', 'DEPTH', data=well, color='purple')
    _ax3.set_xlabel('Sonic')
    _ax3.set_xlim(140, 40)
    _ax3.xaxis.label.set_color('purple')
    _ax3.tick_params(axis='x', colors='purple')
    _ax3.spines['top'].set_edgecolor('purple')
    ax4.plot('NPHI', 'DEPTH', data=well, color='blue')
    ax4.set_xlabel('Neutron')
    ax4.xaxis.label.set_color('blue')
    ax4.set_xlim(0.45, -0.15)
    ax4.set_ylim(4850, 4600)
    ax4.tick_params(axis='x', colors='blue')
    ax4.spines['top'].set_position(('axes', 1.08))
    ax4.spines['top'].set_visible(True)
    ax4.spines['top'].set_edgecolor('blue')
    ax4.set_xticks([0.45, 0.3, 0.15, 0, -0.15])
    for ax in [_ax1, _ax2, _ax3]:
        ax.set_ylim(4850, 4600)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position('top')
        ax.xaxis.set_label_position('top')
        ax.spines['top'].set_position(('axes', 1.02))
    plt.tight_layout()
    return ax, ax4, ax7, ax8, ax9


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
