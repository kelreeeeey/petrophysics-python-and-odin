import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Converting CSV Files to LAS Files Using LASIO
        *Created by: Andy McDonald*  
        *Article Version:*  
        *YouTube Video:*  

        Well log data can be delivered in a variety of formats (DLIS, LAS, CSV, ASC etc.). however, if you have a CSV file containing well log data, and you want to convert it to LAS format there are a number of ways you can achieve this. So if you want to see how to do it using the LASIO library then keep watching.

        One of the issues you may come across when looking at well log data is the large variety of data formats. Data can be delivered or stored in DLIS files, LAS Files, CSV Files and many other different formats. This can often become a headache trying to work out which file to use or when you come to creating a standard file that can be easily read by commercial software or by other users.

        It is a simple format and it is a flat file that contains meta data about the well within the header section, and parameter information, as well as the log data measurements. These files are easy to open up in any text editor and you can quickly and easily read the content. 

        However there may be occasions where you end up with a CSV file containing well log measurements and you want to convert it to a LAS file. Well, that is what we are going cover in todays video. 

        We are going to see how we can take a simple CSV file like this and convert it to a LAS file like this using the excellent LASIO library.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Load Required Libraries
        First off, we will load in the required python libraries. For this tutorial we will be using lasio and pandas.

        For more information about using lasio, check out this article here: https://andymcdonaldgeo.medium.com/loading-and-displaying-well-log-data-b9568efd1d8
        """
    )
    return


@app.cell
def _():
    import lasio
    import pandas as pd
    return lasio, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Load in CSV File Using Pandas
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Next we need to load in our csv file.
        This is done using the `read_csv()` function from pandas and passing in the file location and file name.
        """
    )
    return


@app.cell
def _(pd):
    data = pd.read_csv('Data/Notebook 22/Notebook 22 - VOLVE - 15_9-19.csv')
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once the file has been read, we can then check what the contents of the file are  by calling upon the pandas `.head()` function.
        """
    )
    return


@app.cell
def _(data):
    data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can now see that we have 18 columns within our dataframe, and a mixture of well log measurements.

        To ensure that the data is all numeric and to understand how many nulls are present within the data we can call upon the pandas function `.info()`. This is not a necessary step, but it does allow us to check that the columns are numeric (either float64 or int64).
        """
    )
    return


@app.cell
def _(data):
    data.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Create an Empty LAS Object
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before we can transfer our data from CSV to LAS, we first need to create a blank LAS file. This is achieved by calling upon `lasio.LASFile()` and assigning it to a variable. In this example the variable is called `las_file`.
        """
    )
    return


@app.cell
def _(lasio):
    las_file = lasio.LASFile()
    return (las_file,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When we try to view the contents of the newly created LAS file we can see that the header information is empty.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.header
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also confirm that we have no data within the file by calling upon `las_file.curves`.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.curves
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Setting up the Metadata
        Now that we have a blank las object to work with, we now need to add information to our LAS header. 

        The first step is to create a number of variables that we want to fill in. Doing it this way, rather than passing them into the HeaderItem functions makes it easier to change them in the future and also makes it more readable. For instance, if we created a function where we wanted to update specifc parameters within the header based on different files, we can easily pass these variables into the function and we won't have to update the code within the function.
        """
    )
    return


@app.cell
def _():
    well_name = 'Random Well'
    field_name = 'Random Field'
    uwi = '123456789'
    country = 'Random Country'
    return country, field_name, uwi, well_name


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To begin assigning the values to the header, we need to call upon `las_file.well` and select the header attribute we want to add to. On the right hand side, we will update the HeaderItem and supply a value to it.
        """
    )
    return


@app.cell
def _(country, field_name, las_file, lasio, uwi, well_name):
    las_file.well['WELL'] = lasio.HeaderItem('WELL', value=well_name)
    las_file.well['FLD'] = lasio.HeaderItem('FLD', value=field_name)
    las_file.well['UWI'] = lasio.HeaderItem('UWI', value=uwi)
    las_file.well['CTRY'] = lasio.HeaderItem('CTRY', value=country)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once we have done this we can call upon our header again and we can now see that the values for the well name, UWI, country and field name have all been updated.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.header
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Adding Curves
        To add curves to the file we can use the `add_curve` function and pass in the data and units.

        This example here shows how we can add a single curve to the file called DEPT. Note that if adding the main depth data, it does need to go in as DEPT rather than DEPTH.
        """
    )
    return


@app.cell
def _(data, las_file):
    las_file.add_curve('DEPT', data['DEPTH'], unit='m')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To write out our file, we can call upon `.write()` and pass in the location and file name for our LAS file.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.write('Output/Notebook 22/OutputLAS.las')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Write Remaining Curves
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can reuse the file that we have created above and write the remaining curves.

        To make things easier, I have created a list containing the measurement units for each well log curve. Note that this does include the depth measurement. 
        """
    )
    return


@app.cell
def _():
    units = ['m',
     'inches',
     'unitless',
     'us/ft',
     'us/ft',
     'us/ft',
     'us/ft',
     'API',
     'v/v_decimal',
     'v/v_decimal',
     'v/v_decimal',
     'v/v_decimal',
     'v/v_decimal',
     'g/cm3',
     'g/cm3',
     'ohm.m',
     'ohm.m',
     'degC']
    return (units,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can then begin to loop through each of the logging measurements / columns within the dataframe along with the units list. This is achieved using the Python `zip` function.

        As we already have depth within our las file, we can skip this column by checking the column name. There are other ways in which this can be handled, for example by writing the depth and curves to the las file in one go.
        """
    )
    return


@app.cell
def _(data, las_file, units):
    for col, unit in zip(data.columns, units):
        if col != 'DEPTH':
            las_file.add_curve(col, data[col], unit=unit)
    return col, unit


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When we check the `curves` function, we can see that we have all of our curves and they all have the appropriate units. We can also see from the data.shape part of the listing we have 4101 values per curve which confirms we have data.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.curves
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can confirm that we have values by calling upon of the curves. In the example below, I have called upon GR, and we get an array returned containing the Gamma Ray values, which match the values in the dataframe presented earlier.
        """
    )
    return


@app.cell
def _(las_file):
    las_file['GR']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once we are happy with the las file, we can now export it to a file and use it in any other software package.
        """
    )
    return


@app.cell
def _(las_file):
    las_file.write('Output/Notebook 22/OutputLAS_FINAL.las')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Summary
        In this article we have covered how to convert a simple CSV file containing well log / petrophysical measurements into a industry standard LAS (Log ASCII Standard) file. Once you have created a blank LASFile object in lasio, you will be able to manually update the header items with the correct metadata and also update the curves with the correct values.

        ***Thanks for reading!***

        *If you have found this article useful, please feel free to check out my other articles looking at various aspects of Python and well log data. You can also find my code used in this article and others at [GitHub](https://github.com/andymcdgeo).*

        *If you want to get in touch you can find me on [LinkedIn](https://www.linkedin.com/in/andymcdonaldgeo/) or at my [website](http://andymcdonald.scot/).*

        *Interested in learning more about python and well log data or petrophysics? Follow me on [Medium](https://medium.com/@andymcdonaldgeo).*

        If you have enjoyed this article or any others and want to show your appreciate you are welcome to [Buy Me a Coffee](https://www.buymeacoffee.com/andymcdonaldgeo)
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
