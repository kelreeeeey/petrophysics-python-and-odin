import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Loading and Displaying Well Log Data from LAS
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **Created by:** Andy McDonald  
  
        This notebook illustrates how to load data in from a LAS file and carry out a basic QC of the data before plotting it on a log plot.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading and Checking Data
        The first step is to import the required libraries: pandas, matplotlib and LASIO.  
        lasio is a library that has been developed to handle and work with LAS files. More info on the library can be found at: https://lasio.readthedocs.io/en/latest/
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import lasio
    return lasio, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To load our file in, we can use the read() method from LASIO like so:
        """
    )
    return


@app.cell
def _(lasio):
    las = lasio.read("Data/15-9-19_SR_COMP.LAS")
    return (las,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now that our file has been loaded, we can start investigating it's contents.  
        To find information out about where the file originated from, such as the well name, location and what the depth range of the file covers, we can create a simple for loop to go over each header item. Using Python's f-string we can join the items together.
        """
    )
    return


@app.cell
def _(las):
    for item in las.well:
        print(f"{item.descr} ({item.mnemonic}): {item.value}")
    return (item,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we just want to extract the Well Name, we can simply call it by:
        """
    )
    return


@app.cell
def _(las):
    las.well.WELL.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To quickly see what curves are present within the las file we can loop through `las.curves`
        """
    )
    return


@app.cell
def _(las):
    for _curve in las.curves:
        print(_curve.mnemonic)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To see what curves are present within the las file, we can repeat the process with the CurveItem object and call upon the `unit` and `descr` functions to get info on the units and the curve's description.
        The enumerate function allows us to keep a count of the number of curves that are present within the file. As enumerate returns a 0 on the first loop, we need to 1 to it if we want to include the depth curve.
        """
    )
    return


@app.cell
def _(las):
    for (count, _curve) in enumerate(las.curves):
        print(f'Curve: {_curve.mnemonic}, Units: {_curve.unit}, Description: {_curve.descr}')
    print(f'There are a total of: {count + 1} curves present within this file')
    return (count,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating a Pandas Dataframe
        Data loaded in using LASIO can be converted to a pandas dataframe using the .df() function. This allows us to easily plot data and pass it into one of the many machine learning algorithms.
        """
    )
    return


@app.cell
def _(las):
    well = las.df()
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `.head()` function generates a table view of the header and the first 5 rows within the dataframe.
        """
    )
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To find out more information about data, we can call upon the `.info()` and `.describe()` functions.  
    
        The `.info()` function provides information about the data types and how many non-null values are present within each curve.  
        The `.describe()` function, provides statistical information about each curve and can be a useful QC for each curve.
        """
    )
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell
def _(well):
    well.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Visualising Data Extent
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Instead of the summary provided by the pandas describe() function, we can create a visualisation using matplotlib. Firstly, we need to work out where we have nulls (nan values). We can do this by creating a second dataframe and calling .notnull() on our well dataframe.  
  
        As this returns a boolean (True or False) for each depth, we need to multiply by 1 to convert the values from True and False to 1 and 0 respectively.
        """
    )
    return


@app.cell
def _(well):
    well_nan = well.notnull() * 1
    return (well_nan,)


@app.cell
def _(well_nan):
    well_nan.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can now create a summary plot of the missing data
        """
    )
    return


@app.cell
def _(plt, well_nan):
    _fig = plt.subplots(figsize=(7, 10))
    _ax1 = plt.subplot2grid((1, 7), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 7), (0, 1), rowspan=1, colspan=1)
    _ax3 = plt.subplot2grid((1, 7), (0, 2), rowspan=1, colspan=1)
    _ax4 = plt.subplot2grid((1, 7), (0, 3), rowspan=1, colspan=1)
    _ax5 = plt.subplot2grid((1, 7), (0, 4), rowspan=1, colspan=1)
    _ax6 = plt.subplot2grid((1, 7), (0, 5), rowspan=1, colspan=1)
    _ax7 = plt.subplot2grid((1, 7), (0, 6), rowspan=1, colspan=1)
    columns = well_nan.columns
    axes = [_ax1, _ax2, _ax3, _ax4, _ax5, _ax6, _ax7]
    for (i, _ax) in enumerate(axes):
        _ax.plot(well_nan.iloc[:, i], well_nan.index, lw=0)
        _ax.set_ylim(5000, 0)
        _ax.set_xlim(0, 1)
        _ax.set_title(columns[i])
        _ax.set_facecolor('whitesmoke')
        _ax.fill_betweenx(well_nan.index, 0, well_nan.iloc[:, i], facecolor='red')
        if i > 0:
            plt.setp(_ax.get_yticklabels(), visible=False)
        plt.setp(_ax.get_xticklabels(), visible=False)
    _ax1.set_ylabel('Depth', fontsize=14)
    plt.subplots_adjust(wspace=0)
    plt.show()
    return axes, columns, i


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting Log Data
        Finally, we can plot our data using the code below. Essentially, the code is building up a series of subplots and plotting the data on the relevant tracks.  
  
        When we add curves to the tracks, we need to set the curve's properties, including the limits, colour and labels. We can also specify the shading between curves. An example has been added to the caliper curve to show shading between a bitsize value (8.5") and the CALI curve.  
  
        If there are a number of features that are common between the plots, we can iterate over them using a for loop.
        """
    )
    return


@app.cell
def _(plt, well, well_nan):
    (_fig, _ax) = plt.subplots(figsize=(15, 10))
    _ax1 = plt.subplot2grid((1, 6), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 6), (0, 1), rowspan=1, colspan=1, sharey=_ax1)
    _ax3 = plt.subplot2grid((1, 6), (0, 2), rowspan=1, colspan=1, sharey=_ax1)
    _ax4 = plt.subplot2grid((1, 6), (0, 3), rowspan=1, colspan=1, sharey=_ax1)
    _ax5 = _ax3.twiny()
    _ax6 = plt.subplot2grid((1, 6), (0, 4), rowspan=1, colspan=1, sharey=_ax1)
    _ax7 = _ax2.twiny()
    ax10 = _ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = _ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = _ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = _ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = _ax6.twiny()
    ax14.xaxis.set_visible(False)
    _ax1.plot(well['GR'], well.index, color='green', linewidth=0.5)
    _ax1.set_xlabel('Gamma')
    _ax1.xaxis.label.set_color('green')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylabel('Depth (m)')
    _ax1.tick_params(axis='x', colors='green')
    _ax1.spines['top'].set_edgecolor('green')
    _ax1.title.set_color('green')
    _ax1.set_xticks([0, 50, 100, 150, 200])
    _ax2.plot(well['RDEP'], well.index, color='red', linewidth=0.5)
    _ax2.set_xlabel('Resistivity - Deep')
    _ax2.set_xlim(0.2, 2000)
    _ax2.xaxis.label.set_color('red')
    _ax2.tick_params(axis='x', colors='red')
    _ax2.spines['top'].set_edgecolor('red')
    _ax2.set_xticks([0.1, 1, 10, 100, 1000])
    _ax2.semilogx()
    _ax3.plot(well['DEN'], well.index, color='red', linewidth=0.5)
    _ax3.set_xlabel('Density')
    _ax3.set_xlim(1.95, 2.95)
    _ax3.xaxis.label.set_color('red')
    _ax3.tick_params(axis='x', colors='red')
    _ax3.spines['top'].set_edgecolor('red')
    _ax3.set_xticks([1.95, 2.45, 2.95])
    _ax4.plot(well['AC'], well.index, color='purple', linewidth=0.5)
    _ax4.set_xlabel('Sonic')
    _ax4.set_xlim(140, 40)
    _ax4.xaxis.label.set_color('purple')
    _ax4.tick_params(axis='x', colors='purple')
    _ax4.spines['top'].set_edgecolor('purple')
    _ax5.plot(well['NEU'], well.index, color='blue', linewidth=0.5)
    _ax5.set_xlabel('Neutron')
    _ax5.xaxis.label.set_color('blue')
    _ax5.set_xlim(45, -15)
    _ax5.set_ylim(4150, 3500)
    _ax5.tick_params(axis='x', colors='blue')
    _ax5.spines['top'].set_position(('axes', 1.08))
    _ax5.spines['top'].set_visible(True)
    _ax5.spines['top'].set_edgecolor('blue')
    _ax5.set_xticks([45, 15, -15])
    _ax6.plot(well['CALI'], well.index, color='black', linewidth=0.5)
    _ax6.set_xlabel('Caliper')
    _ax6.set_xlim(6, 16)
    _ax6.xaxis.label.set_color('black')
    _ax6.tick_params(axis='x', colors='black')
    _ax6.spines['top'].set_edgecolor('black')
    _ax6.fill_betweenx(well_nan.index, 8.5, well['CALI'], facecolor='yellow')
    _ax6.set_xticks([6, 11, 16])
    _ax7.plot(well['RMED'], well.index, color='green', linewidth=0.5)
    _ax7.set_xlabel('Resistivity - Med')
    _ax7.set_xlim(0.2, 2000)
    _ax7.xaxis.label.set_color('green')
    _ax7.spines['top'].set_position(('axes', 1.08))
    _ax7.spines['top'].set_visible(True)
    _ax7.tick_params(axis='x', colors='green')
    _ax7.spines['top'].set_edgecolor('green')
    _ax7.set_xticks([0.1, 1, 10, 100, 1000])
    _ax7.semilogx()
    for _ax in [_ax1, _ax2, _ax3, _ax4, _ax6]:
        _ax.set_ylim(4500, 3500)
        _ax.grid(which='major', color='lightgrey', linestyle='-')
        _ax.xaxis.set_ticks_position('top')
        _ax.xaxis.set_label_position('top')
        _ax.spines['top'].set_position(('axes', 1.02))
    for _ax in [_ax2, _ax3, _ax4, _ax6]:
        plt.setp(_ax.get_yticklabels(), visible=False)
    plt.tight_layout()
    _fig.subplots_adjust(wspace=0.15)
    return ax10, ax11, ax12, ax13, ax14


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
