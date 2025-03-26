import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 6 - Displaying Formations on Log Plots
        Created by: Andy McDonald

        This short notebook illustrates how to add background shading to each of the curve tracks based on formations contained within a dictionary object.
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
    well = pd.read_csv("Data/15_9-19.csv", header=0, skiprows=[1])
    return (well,)


@app.cell
def _(np, well):
    well.replace(-999.00, np.nan, inplace=True)
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell
def _(plt, well):
    (_fig, _ax) = plt.subplots(figsize=(15, 10))
    _ax1 = plt.subplot2grid((1, 5), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 5), (0, 1), rowspan=1, colspan=1)
    _ax3 = plt.subplot2grid((1, 5), (0, 2), rowspan=1, colspan=1)
    _ax4 = plt.subplot2grid((1, 5), (0, 3), rowspan=1, colspan=1)
    _ax5 = _ax3.twiny()
    _ax10 = _ax1.twiny()
    _ax10.xaxis.set_visible(False)
    _ax11 = _ax2.twiny()
    _ax11.xaxis.set_visible(False)
    _ax12 = _ax3.twiny()
    _ax12.xaxis.set_visible(False)
    _ax13 = _ax4.twiny()
    _ax13.xaxis.set_visible(False)
    _ax1.plot('GR', 'DEPTH', data=well, color='green', linewidth=0.5)
    _ax1.set_xlabel('Gamma')
    _ax1.xaxis.label.set_color('green')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylabel('Depth (m)')
    _ax1.tick_params(axis='x', colors='green')
    _ax1.spines['top'].set_edgecolor('green')
    _ax1.title.set_color('green')
    _ax1.set_xticks([0, 50, 100, 150, 200])
    _ax2.plot('RT', 'DEPTH', data=well, color='red', linewidth=0.5)
    _ax2.set_xlabel('Resistivity')
    _ax2.set_xlim(0.2, 2000)
    _ax2.xaxis.label.set_color('red')
    _ax2.tick_params(axis='x', colors='red')
    _ax2.spines['top'].set_edgecolor('red')
    _ax2.set_xticks([0.1, 1, 10, 100, 1000])
    _ax2.semilogx()
    _ax3.plot('RHOB', 'DEPTH', data=well, color='red', linewidth=0.5)
    _ax3.set_xlabel('Density')
    _ax3.set_xlim(1.95, 2.95)
    _ax3.xaxis.label.set_color('red')
    _ax3.tick_params(axis='x', colors='red')
    _ax3.spines['top'].set_edgecolor('red')
    _ax3.set_xticks([1.95, 2.45, 2.95])
    _ax4.plot('DT', 'DEPTH', data=well, color='purple', linewidth=0.5)
    _ax4.set_xlabel('Sonic')
    _ax4.set_xlim(140, 40)
    _ax4.xaxis.label.set_color('purple')
    _ax4.tick_params(axis='x', colors='purple')
    _ax4.spines['top'].set_edgecolor('purple')
    _ax5.plot('NPHI', 'DEPTH', data=well, color='blue', linewidth=0.5)
    _ax5.set_xlabel('Neutron')
    _ax5.xaxis.label.set_color('blue')
    _ax5.set_xlim(0.45, -0.15)
    _ax5.set_ylim(4150, 3500)
    _ax5.tick_params(axis='x', colors='blue')
    _ax5.spines['top'].set_position(('axes', 1.08))
    _ax5.spines['top'].set_visible(True)
    _ax5.spines['top'].set_edgecolor('blue')
    _ax5.set_xticks([0.45, 0.15, -0.15])
    for _ax in [_ax1, _ax2, _ax3, _ax4]:
        _ax.set_ylim(4150, 3500)
        _ax.grid(which='major', color='lightgrey', linestyle='-')
        _ax.xaxis.set_ticks_position('top')
        _ax.xaxis.set_label_position('top')
        _ax.spines['top'].set_position(('axes', 1.02))
    plt.tight_layout()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Displaying shaded formation intervals on the plot

        We can use the axhspan functions for shade across each track at specified depth intervals.
        To tidy up the plot, we can remove the depth labels for each track. We require a short separation between the tracks due to overlap of the curve scales.
        """
    )
    return


@app.cell
def _(plt, well):
    formations = {'A': [3500, 3665], 'B': [3665, 3705], 'C': [3705, 3820], 'D': [3820, 3935], 'E': [3935, 4100]}
    zone_colours = ['red', 'blue', 'green', 'orange', 'purple']
    (_fig, _ax) = plt.subplots(figsize=(15, 10))
    _ax1 = plt.subplot2grid((1, 5), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 5), (0, 1), rowspan=1, colspan=1, sharey=_ax1)
    _ax3 = plt.subplot2grid((1, 5), (0, 2), rowspan=1, colspan=1, sharey=_ax1)
    _ax4 = plt.subplot2grid((1, 5), (0, 3), rowspan=1, colspan=1, sharey=_ax1)
    _ax5 = _ax3.twiny()
    _ax10 = _ax1.twiny()
    _ax10.xaxis.set_visible(False)
    _ax11 = _ax2.twiny()
    _ax11.xaxis.set_visible(False)
    _ax12 = _ax3.twiny()
    _ax12.xaxis.set_visible(False)
    _ax13 = _ax4.twiny()
    _ax13.xaxis.set_visible(False)
    _ax1.plot('GR', 'DEPTH', data=well, color='green', linewidth=0.5)
    _ax1.set_xlabel('Gamma')
    _ax1.xaxis.label.set_color('green')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylabel('Depth (m)')
    _ax1.tick_params(axis='x', colors='green')
    _ax1.spines['top'].set_edgecolor('green')
    _ax1.title.set_color('green')
    _ax1.set_xticks([0, 50, 100, 150, 200])
    _ax2.plot('RT', 'DEPTH', data=well, color='red', linewidth=0.5)
    _ax2.set_xlabel('Resistivity')
    _ax2.set_xlim(0.2, 2000)
    _ax2.xaxis.label.set_color('red')
    _ax2.tick_params(axis='x', colors='red')
    _ax2.spines['top'].set_edgecolor('red')
    _ax2.set_xticks([0.1, 1, 10, 100, 1000])
    _ax2.semilogx()
    _ax3.plot('RHOB', 'DEPTH', data=well, color='red', linewidth=0.5)
    _ax3.set_xlabel('Density')
    _ax3.set_xlim(1.95, 2.95)
    _ax3.xaxis.label.set_color('red')
    _ax3.tick_params(axis='x', colors='red')
    _ax3.spines['top'].set_edgecolor('red')
    _ax3.set_xticks([1.95, 2.45, 2.95])
    _ax4.plot('DT', 'DEPTH', data=well, color='purple', linewidth=0.5)
    _ax4.set_xlabel('Sonic')
    _ax4.set_xlim(140, 40)
    _ax4.xaxis.label.set_color('purple')
    _ax4.tick_params(axis='x', colors='purple')
    _ax4.spines['top'].set_edgecolor('purple')
    _ax5.plot('NPHI', 'DEPTH', data=well, color='blue', linewidth=0.5)
    _ax5.set_xlabel('Neutron')
    _ax5.xaxis.label.set_color('blue')
    _ax5.set_xlim(0.45, -0.15)
    _ax5.set_ylim(4150, 3500)
    _ax5.tick_params(axis='x', colors='blue')
    _ax5.spines['top'].set_position(('axes', 1.08))
    _ax5.spines['top'].set_visible(True)
    _ax5.spines['top'].set_edgecolor('blue')
    _ax5.set_xticks([0.45, 0.15, -0.15])
    for _ax in [_ax1, _ax2, _ax3, _ax4]:
        _ax.set_ylim(4150, 3500)
        _ax.grid(which='major', color='lightgrey', linestyle='-')
        _ax.xaxis.set_ticks_position('top')
        _ax.xaxis.set_label_position('top')
        _ax.spines['top'].set_position(('axes', 1.02))
        for (depth, colour) in zip(formations.values(), zone_colours):
            _ax.axhspan(depth[0], depth[1], color=colour, alpha=0.1)
    for _ax in [_ax2, _ax3, _ax4]:
        plt.setp(_ax.get_yticklabels(), visible=False)
    plt.tight_layout()
    _fig.subplots_adjust(wspace=0.15)
    return colour, depth, formations, zone_colours


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
