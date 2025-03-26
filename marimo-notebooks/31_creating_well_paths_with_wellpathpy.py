import marimo

__generated_with = "0.11.28"
app = marimo.App()


app._unparsable_cell(
    r"""
    !pip install wellpathpy
    """,
    name="_"
)


@app.cell
def _():
    import wellpathpy as wp
    import matplotlib.pyplot as plt

    import numpy as np
    np.set_printoptions(suppress=True)
    return np, plt, wp


@app.cell
def _(wp):
    md, inc, azi = wp.read_csv('Data/Volve/15_9-F-12_Survey_Data.csv')
    return azi, inc, md


@app.cell
def _(md):
    md
    return


@app.cell
def _(azi, inc, md, wp):
    dev = wp.deviation(md, inc, azi)
    return (dev,)


@app.cell
def _(dev):
    dev
    return


@app.cell
def _(dev, plt):
    fig, ax = plt.subplots(1, 2, figsize=(8,10))

    ax1 = plt.subplot2grid((1,2), (0,0))
    ax2 = plt.subplot2grid((1,2), (0,1))

    ax1.plot(dev.inc, dev.md, color = "black", marker='.', linewidth=0)
    ax1.set_ylim(dev.md[-1], 0)
    ax1.set_xlim(0, 90)
    ax1.set_xlabel('Deviation', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Measured Depth', fontweight='bold', fontsize=14)
    ax1.grid(color='lightgrey')
    ax1.set_axisbelow(True)

    ax2.plot(dev.azi, dev.md, color = "black", marker='.', linewidth=0)
    ax2.set_ylim(dev.md[-1], 0)
    ax2.set_xlim(0, 360)
    ax2.set_xlabel('Azimuth', fontweight='bold', fontsize=14)
    ax2.grid(color='lightgrey')
    ax2.set_axisbelow(True)

    plt.show()
    return ax, ax1, ax2, fig


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating Positional Logs
        Next we need to set the depth spacing we want the positional logs set to. This can be set to match your well log spacing or another spacing of your choice.
        """
    )
    return


@app.cell
def _(dev):
    depth_step = 1
    depths = list(range(0, int(dev.md[-1]) + 1, depth_step))
    return depth_step, depths


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Calculate the continuous logs using the minimum curvature method
        """
    )
    return


@app.cell
def _(depths, dev):
    pos = dev.minimum_curvature().resample(depths = depths)
    return (pos,)


@app.cell
def _(pos):
    pos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The positional data will only contain depth, Northing and Easting at the resampled depth rate. If we want to have azimuth, inclination and depth (md) at the same sample rate we have to call upon `.deviation()` on our positional data.
        """
    )
    return


@app.cell
def _(pos):
    resampled_dev = pos.deviation()
    return (resampled_dev,)


@app.cell
def _(resampled_dev):
    resampled_dev
    return


@app.cell
def _(dev, plt, resampled_dev):
    (fig_1, ax_1) = plt.subplots(1, 2, figsize=(8, 10))
    ax1_1 = plt.subplot2grid((1, 2), (0, 0))
    ax2_1 = plt.subplot2grid((1, 2), (0, 1))
    ax1_1.plot(dev.inc, dev.md, color='black', marker='.', linewidth=0)
    ax1_1.plot(resampled_dev.inc, resampled_dev.md, color='red')
    ax1_1.set_ylim(dev.md[-1], 0)
    ax1_1.set_xlim(0, 90)
    ax1_1.set_xlabel('Deviation', fontweight='bold', fontsize=14)
    ax1_1.set_ylabel('Measured Depth', fontweight='bold', fontsize=14)
    ax1_1.grid(color='lightgrey')
    ax1_1.set_axisbelow(True)
    ax2_1.plot(dev.azi, dev.md, color='black', marker='.', linewidth=0)
    ax2_1.plot(resampled_dev.azi, resampled_dev.md, color='red')
    ax2_1.set_ylim(dev.md[-1], 0)
    ax2_1.set_xlim(0, 360)
    ax2_1.set_xlabel('Azimuth', fontweight='bold', fontsize=14)
    ax2_1.grid(color='lightgrey')
    ax2_1.set_axisbelow(True)
    plt.show()
    return ax1_1, ax2_1, ax_1, fig_1


@app.cell
def _(plt, pos):
    (fig_2, ax_2) = plt.subplots(2, 2, figsize=(15, 5))
    ax1_2 = plt.subplot2grid((1, 3), (0, 0))
    ax2_2 = plt.subplot2grid((1, 3), (0, 1))
    ax3 = plt.subplot2grid((1, 3), (0, 2))
    ax1_2.plot(pos.easting, pos.northing, color='black', linewidth=2)
    ax1_2.set_xlim(-500, 400)
    ax1_2.set_ylim(-400, 100)
    ax1_2.set_xlabel('West (-) / East (+)', fontweight='bold', fontsize=14)
    ax1_2.set_ylabel('South (-) / North (+)', fontweight='bold', fontsize=14)
    ax1_2.grid(color='lightgrey')
    ax1_2.set_axisbelow(True)
    ax2_2.plot(pos.easting, pos.depth, color='black', linewidth=2)
    ax2_2.set_xlim(-500, 400)
    ax2_2.set_ylim(3500, 0)
    ax2_2.set_xlabel('West (-) / East (+)', fontweight='bold', fontsize=14)
    ax2_2.set_ylabel('Depth', fontweight='bold', fontsize=14)
    ax2_2.grid(color='lightgrey')
    ax2_2.set_axisbelow(True)
    ax3.plot(pos.northing, pos.depth, color='black', linewidth=2)
    ax3.set_xlim(-500, 400)
    ax3.set_ylim(3500, 0)
    ax3.set_xlabel('South (-) / North (+)', fontweight='bold', fontsize=14)
    ax3.set_ylabel('Depth', fontweight='bold', fontsize=14)
    ax3.grid(color='lightgrey')
    ax3.set_axisbelow(True)
    plt.tight_layout()
    plt.show()
    return ax1_2, ax2_2, ax3, ax_2, fig_2


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Calculating TVDSS
        """
    )
    return


@app.cell
def _(pos):
    pos_tvdss = pos.to_tvdss(datum_elevation=30)
    return (pos_tvdss,)


@app.cell
def _(pos_tvdss):
    pos_tvdss
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 3D Directional Plot
        """
    )
    return


@app.cell
def _(pos):
    wellhead_northing = 6478572
    wellhead_easting = 435050

    pos_wellhead = pos.to_wellhead(surface_northing=wellhead_northing,
                                   surface_easting=wellhead_easting)
    return pos_wellhead, wellhead_easting, wellhead_northing


@app.cell
def _(pos_wellhead):
    pos_wellhead.northing
    return


@app.cell
def _(pos_wellhead):
    import plotly
    import plotly.graph_objs as go
    plotly.offline.init_notebook_mode()
    wellpath = go.Scatter3d(x=pos_wellhead.easting, y=pos_wellhead.northing, z=pos_wellhead.depth, mode='markers', marker={'size': 5, 'opacity': 0.8})
    data = [wellpath]
    fig_3 = go.Figure(data=data)
    fig_3.update_layout(scene=dict(zaxis_autorange='reversed', xaxis_title='West (-) / East (+) (m)', yaxis_title='South (-) / North (+) (m)', zaxis_title='TVD (m)'), width=800, margin=dict(r=20, b=10, l=10, t=10))
    plotly.offline.iplot(fig_3)
    return data, fig_3, go, plotly, wellpath


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Integrate Survey Data with Well Data
        """
    )
    return


@app.cell
def _(pd, pos, pos_tvdss, pos_wellhead, resampled_dev):
    data_1 = {'MD': resampled_dev.md, 'AZI': resampled_dev.azi, 'INC': resampled_dev.inc, 'TVD': pos.depth, 'TVDSS': pos_tvdss.depth, 'YLOC': pos.northing, 'XLOC': pos.easting, 'NORTHING': pos_wellhead.northing, 'EASTING': pos_wellhead.easting}
    df = pd.DataFrame(data_1)
    return data_1, df


@app.cell
def _(df):
    df
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
