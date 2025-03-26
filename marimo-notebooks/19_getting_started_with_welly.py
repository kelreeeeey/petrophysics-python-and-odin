import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # 19 - Exploring Well Log Data using the Welly Python Library

        The welly library was developed by Agile Geoscience to help with loading, processing and analysing well log data from a single well or multiple wells. The library allows exploration of the meta data found within the headers of las files and also contains a plotting function to display a typical well log. Additionally, the welly library contains tools for identifying and handling data quality issues.

        The Welly library can be found at the Agile Geoscience GitHub at https://github.com/agile-geoscience/welly

        In this short tutorial we will see how to load a well from the Volve field and exploring some of the functionality available within this library.

        ## The Dataset

        The dataset we are using comes from the publicly available Equinor Volve Field dataset released in 2018. The file used in this tutorial is from well 15/19-F1B. 

        Details on the Volve Dataset can be found [here](https://www.equinor.com/en/what-we-do/norwegian-continental-shelf-platforms/volve.html)

        ## Importing Libraries and Data
        The first step in this tutorial will be to load in the required modules, Well and Curve, from the Welly libray. These modules are used to work with well log data and with individual curves.
        """
    )
    return


@app.cell
def _():
    from welly import Well
    from welly import Curve

    import matplotlib.pyplot as plt
    return Curve, Well, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Our LAS file can be loaded in using the `Well.from_las()` method. This will create a new well object.
        """
    )
    return


@app.cell
def _(Well):
    well = Well.from_las('Data/15_19_F1B_WLC_PETRO_COMPUTED_INPUT_1.LAS')
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Data Exploration
        ## File and Well Information
        Now that our data has been loaded in we can begin exploring the contents and meta data for the selected well. 
        If we call upon our `well` object we will be presented with a summary table which contains the wellname, location, co-ordinates, and a list of curve mnemonics.
        """
    )
    return


@app.cell
def _(well):
    well
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also call upon specific functions to access the required information. 

        The first is the `header` which will return key header information, including the well name, Unique Well Identifier (UWI), the field name and company name. 
        """
    )
    return


@app.cell
def _(well):
    well.header
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's now have a look at the location information for this well. To do so we can call upon the `.location` method for our data object.
        """
    )
    return


@app.cell
def _(well):
    well.location
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This returns a location object in the form of a dictionary. The file we are using does not contain much information about the location of the well, but we do have information about the latitude and longitude. These can be extracted by appending `.latitude` and `.longitude` to the location method and put into an easier to read format.

        Using the print function for these methods provides a nicer output to read.
        """
    )
    return


@app.cell
def _(well):
    lati = well.location.latitude
    long = well.location.longitude

    print(lati)
    print(long)
    return lati, long


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Exploring the Data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We saw in the previous section when looking at the well header that we had a number of curves. We can get an idea of how many by calling up on the `count_curves()` function.
        """
    )
    return


@app.cell
def _(well):
    well.count_curves()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This returns a total count of 22 curves.

        We can also obtain a list of the curve menmonics within the las file using the method `_get_curve_menmonics()`.
        """
    )
    return


@app.cell
def _(well):
    well._get_curve_mnemonics()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Another way to view all of the curves is by calling upon `.data`. This returns a dictionary object containing the well name, along with the first 3 and the last 3 values for that curve.

        As seen in the example below, many of the first and last values are listed as nan, which stands for Not a Number.
        """
    )
    return


@app.cell
def _(well):
    well.data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can delve a little deeper into each of the curves within the las file by passing in the name of the curve like so:
        """
    )
    return


@app.cell
def _(well):
    well.data['GR']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This provides us with some summary statistics of the curve, such as:
        - what the null value is
        - the curve units
        - the curve data range
        - the step value of the data
        - the total number of samples
        - the total number of missing values (NaNs)
        - Min, Max and Mean of the curve
        - Curve description
        - A list of the first 3 and last 3 values


        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Data QC
        Checking the quality of well log data is an important part of the petrophysics workflow. 

        The borehole environment can be a hostile place with high temperatures, high pressures, irregular borehole shapes etc all of which can have an impact on the logging measurements. This can result in numerous issues such as missing values, outliers, constant values and erroneous values.

        The welly library comes with a number of quality control checks which will allow us to check all of the data or specific curves for issues.

        The quality control checks include:
        - Checking for gaps / missing values : `.no_nans(curve)`
        - Checking if the entire curve is empty or not : `.not_empty(curve)`
        - Checking if the curve contains constant values : `.no_flat(curve)`
        - Checking units: `check_units(list_of_units)`
        - Checking if values are all positive : `all_positive(curve)`
        - Checking if curve is within a range : `all_between(min_value, max_value)`

        The full list of methods can be found within the Welly help documents at: https://welly.readthedocs.io

        Before we start we will need to import the quality module like so:
        """
    )
    return


@app.cell
def _():
    import welly.quality as wq
    return (wq,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before we run any quality checks we first need to create a list of what tests we want to run and on what data we want to run those tests.

        To do this we can build up a dictionary, with the key being the curve(s) we want to run the checks on. If want to run it on all of the curves we need to use the key `Each`.

        For every curve we will check if there are any flatline values, any gaps and making sure the curve is not empty.
        For the gamma ray (GR) and bulk density (RHOB) curves we are going to check that all of the values are positive, that they are between standard ranges and that the units are what we expect them to be.
        """
    )
    return


@app.cell
def _(wq):
    tests = {'Each': [wq.no_flat,
                     wq.no_gaps,
                     wq.not_empty],
            'GR': [
                    wq.all_positive,
                    wq.all_between(0, 250),
                    wq.check_units(['API', 'GAPI']),
            ],
            'RHOB': [
                    wq.all_positive,
                    wq.all_between(1.5, 3),
                    wq.check_units(['G/CC', 'g/cm3']),
            ]}
    return (tests,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We could run the tests as they are, however, the output is not easy to read. To make easier and nicer, we will using the HTML function from IPython.display to make a pretty table.

        Once the module is imported we can create a variable called `data_qc_table` to store the information in. Assigned to this variable will be `data.qc_table_html(tests)` which generates the table from the `tests` dictionary we created above.
        """
    )
    return


@app.cell
def _(tests, well):
    from IPython.display import HTML
    data_qc_table = well.qc_table_html(tests)
    HTML(data_qc_table)
    return HTML, data_qc_table


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        After running the tests we can see that we have a coloured HTML table returned. Anything highlighted in green is True and anything in red is False.

        From the table we can see that the BS (BitSize) curve failed on one of the three tests. Under the `no_flat` column we have a False value flagged which suggests that this curve contains constant/flat values. This has been correctly flagged as the bitsize curve measures the drill bit diameter, which will be constant for a given run or series of runs.

        We can also see that a number of curves have been flagged as containing gaps.

        The tests that were run just for GR and RHOB can also be seen in the table. When we run specific tests on specific curves, the remainder of the the results will be greyed out.

        We can run another test to identify the fraction of the data that is not nan. For this we setup a new test and apply to all curves using `Each`.
        """
    )
    return


@app.cell
def _(HTML, well, wq):
    tests_nans = {'Each': [wq.fraction_not_nans]}

    data_nans_qc_table = well.qc_table_html(tests_nans)
    HTML(data_nans_qc_table)
    return data_nans_qc_table, tests_nans


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once we run these tests we are presented with a table similar to the one above. In the last column we have the total fraction of values for each curve this is not a nan. These values are in decimal, with a value of 1.0 representing 100% completeness. The Score column contains a rounded version of this number.

        We can write a short loop and print the percentage values out for each curve. This provides a cleaner table to get an idea of missing data percentage for each curve.
        """
    )
    return


@app.cell
def _(tests_nans, well):
    print((f'Curve \t % Complete').expandtabs(10))
    print((f'----- \t ----------').expandtabs(10))

    for k,v in well.qc_data(tests_nans).items():
    
        for i,j in v.items():
            values = round(j*100, 2)
        print((f'{k} \t {values}%').expandtabs(10))
    return i, j, k, v, values


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        From the results we can see that a number of curves have a high percentage of missing values. This could be attributable to some of the measurements not starting until deeper in the well. We will be able to determine this in the next section with plots.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Data Plotting
        Visualising well log data is at the heart of petrophysics, with log plots being one of the most common display formats.
        The welly library allows fast and easy generation of well log plots. 

        First we generate a list of data that we want to display in each track. If we want to display more than one curve in a track we can embed another list e.g. `['MD', ['DT', 'DTS']]`. The curves within the inner list will be plotted on the same track and on the same scale.

        Next, we can call upon the plot function and pass in the tracks list.

        """
    )
    return


@app.cell
def _(well):
    _tracks = ['MD', 'GR', 'RHOB', 'NPHI', ['DT', 'DTS']]
    well.plot(tracks=_tracks)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As discussed in the data quality section, our assumption that some of the logging curves do not extend all the way to the top of the well. This is very common practice and avoids the need for and the cost of running tools from the top of the well to the bottom.

        Let's zoom in a little bit closer on the lower interval. To do this we can use a regular matplotlib function to set the y-axis limits. Note that we do need to reverse the numbers so that the deeper value is first, and the shallower one second.
        """
    )
    return


@app.cell
def _(plt, well):
    _tracks = ['MD', 'BS', 'CALI', 'GR', 'RHOB', 'NPHI', ['DT', 'DTS']]
    well.plot(tracks=_tracks)
    plt.ylim(3500, 3000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can see from the result that we now have a nice looking plot with very little effort.

        However, the control over the plot appearance is limited with the current implementation not allowing granular control over the plot such as colours, scales and displaying curves with reversed scales (e.g. Neutron & Density curves).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Well Log Data to Pandas Dataframe
        In this final section, we will look at exporting the well log data from welly to pandas. Pandas is one of the most popular libraries for storing, analysing and manipulating data.

        The conversion is a simple process and can be achieved by calling `.df()` on our well object.
        """
    )
    return


@app.cell
def _(well):
    df = well.df()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can confirm the data has been converted by calling upon the `.describe()` method from pandas to view the summary statistics of the data.
        """
    )
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Summary

        The welly library, developed by Agile-Geoscience is a great tool for working with and exploring well log files. In this example we have seen how to load a single las file, explore the meta information about the well and the curve contents, and display the log data on a log plot.

        Welly has significant more functionality that can handle multiple well logs as well as creating synthetic siesmiograms from the well data.

        You can find and explore the welly repository [here](https://github.com/agile-geoscience/welly).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
