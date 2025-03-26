import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 1. Loading and Displaying Well Data From CSV
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Created By: Andy McDonald
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The following tutorial illustrates loading basic well log data from a csv file by using pandas, and displaying the data using the plotting option available in pandas. 
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return np, pd


@app.cell
def _(pd):
    well = pd.read_csv("Data/L0509WellData.csv", header=0)
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To check that the data has been loaded in correctly, we can use the .head() function in pandas to view the first 5 rows and the header.
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
        We can also view some statistics on the curves by using the describe() function.
        """
    )
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before carrying out any displaying of data or calculations, we carry out some data cleansing. The first is the conversion of null values, represented by -999.25, to a Not a Number (NaN). We can achieve this using the replace function.
        """
    )
    return


@app.cell
def _(np, well):
    well.replace(-999, np.nan, inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we now call the describe and head functions on the well dataframe, we can see that the nulls have been been replaced.
        """
    )
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        By default, the well.head() function produces the first 5 rows of data. We can extend this by passing in a value to the head function.
        """
    )
    return


@app.cell
def _(well):
    well.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now we have some data appearing in the GR column.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Viewing Data on a Log Plot
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        With pandas, we can quickly bring up a plot of our well data by using the .plot() function on our well dataframe. <br><br>If we just specify the x and y axis, we can generate a simple line plot.
        """
    )
    return


@app.cell
def _(well):
    well.plot(x = 'DEPTH', y = 'GR')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can change the type of plot by using the keyword kind and passing in the word scatter. In this example we have a familiar density neutron crossplot. <b>Note</b> that we can change the y-axis scales so that they are flipped and show increasing porosity as you move up the axis.
        """
    )
    return


@app.cell
def _(well):
    well.plot(kind = 'scatter', x = 'NPHI', y = 'RHOB', ylim=(3, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also add some colour to our plot using the gamma ray as a third axis. This is done by including the c argument and specifying the column name. <br><br>
        This helps us identify the cleaner intervals from shalier intervals
        """
    )
    return


@app.cell
def _(well):
    well.plot(kind = 'scatter', x = 'NPHI', y = 'RHOB', c='GR', 
              colormap='jet', 
              ylim=(3, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Data can also be easily displayed as a histogram in the form of bars:
        """
    )
    return


@app.cell
def _(well):
    well['GR'].plot(kind="hist", bins = 30)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Or using a Kernel Density Estimate:
        """
    )
    return


@app.cell
def _(well):
    well['GR'].plot(kind="kde", xlim =(0,200))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        That is all for this short tutorial. In the next one we will take our plotting to the next level and construct the familiar log plot using matplotlib.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
