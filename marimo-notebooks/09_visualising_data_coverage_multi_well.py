import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Visualising Well Data Coverage Using Matplotlib
        **Created by:** Andy McDonald

        This notebook illustrates how you can visualise data extent for multiple wells.  
        **Data Used:** Volve Dataset  
        **Medium Article:** https://andymcdonaldgeo.medium.com/visualising-well-data-coverage-using-matplotlib-f30591c89754
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Exploratory Data Analysis (EDA) is an integral part of Data Science. The same is true for the petrophysical domain and can often be referred to as the Log QC or data review stage of a project. It is at this stage that we begin to go through the data in detail and identify what data we really have, where we have it and what is the quality of the gathered data.  
  
        A significant portion of the time that we spend (in some cases up to 90%! - Kohlleffel, 2015) working with well log data is spent trying to understand it and wrangle it into a state that is fit for interpretation. The remaining 10% is when we can get down to the business of carrying out the petrophysical interpretation. This can vary depending on the initial state of the project being worked on.  
  
        At the QC stage, we often we find ourselves with multiple input files, random curve names, missing data and extra curves that have no immediate use. This can lead to confusion and frustration, especially when working with multiple tools and vintage datasets. In cases where we have missing data, we need to identify it and determine the best way to handle it. This can be difficult to do by looking at single LAS files in a text editor, but it can be made easier using software. One such method is by using Python, a common and popular programming language.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading the Data and Libraries
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As with any Python project we need to load in the required data and libraries. For this notebook we will be using pandas and matplotlib.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt


@app.cell
def _(pd):
    data = pd.read_csv('Data/VolveWells.csv')
    return (data,)


@app.cell
def _(data):
    data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        From a first glance, we can see that we have 12 columns in our dataset. The first column is the Well, followed by the Depth curve, which is subsequently followed by each of the logging curves.  
  
        We can see what wells we have in our dataset by using a simple for loop. This provides a nicely formatted view.
        """
    )
    return


@app.cell
def _(data):
    for well in data['WELL'].unique():
        print(well)
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Data Preparation
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In order for our plot to work as intended, we need to modify the column order of our dataset. This can be achieved by first creating a list of the columns in the order that we want.
        """
    )
    return


@app.cell
def _():
    plot_cols = ['WELL', 'DEPTH', 'CALI', 'BS', 'GR', 'NEU', 'DEN', 'PEF', 'RDEP', 'RMED', 'AC', 'ACS']
    return (plot_cols,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Then we can replace the existing dataframe with the new column order by passing the list directly into the dataframe:
        """
    )
    return


@app.cell
def _(data, plot_cols):
    data_1 = data[plot_cols]
    return (data_1,)


@app.cell
def _(data_1):
    data_1.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The next step involves creating a copy of our dataframe. This will allow us to keep the original dataframe for further work later in a project.
        """
    )
    return


@app.cell
def _(data_1):
    data_nan = data_1.copy()
    return (data_nan,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In places where we have a real value we will assign it a number which will be dependent on its position in the dataframe. In places where we have a NaN (Not a Number) value, we are going to give it a value of number - 1. This will allow us to shade between one number and another whilst using a single subplot for each well. This keeps things simple and negates the need for creating subplots for each curve in each well.
        """
    )
    return


@app.cell
def _(data_nan):
    for num, col in enumerate(data_nan.columns[2:]):
        data_nan[col] = data_nan[col].notnull() * (num + 1)
        data_nan[col].replace(0, num, inplace=True)
        print(col, num) #Print out the col name and number to verify it works
    return col, num


@app.cell
def _(data_nan):
    data_nan.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting the Data
        Now we have come to the plotting stage. In order for each well to plot in a separate subplot, we have to group the dataframe by the well name:
        """
    )
    return


@app.cell
def _(data_nan):
    grouped = data_nan.groupby('WELL')
    return (grouped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We use ax.fillbetweenx() to fill between our two values for each curve that we set up earlier. For example, CALI has two values to indicate data presence: 1 when there is a real value and 0 when there is a NaN. Similarly, GR has two values: 3 when there is real data and 2 when there is a NaN.
        """
    )
    return


@app.cell
def _(grouped, plt):
    #Setup the labels we want to display on the x-axis
    labels = ['CALI', 'BS', 'GR', 'NEU', 'DEN', 'PEF', 'RDEP', 'RMED', 'AC', 'ACS']

    #Setup the figure and the subplots
    fig, axs = plt.subplots(1, 3, figsize=(20,10))

    #Loop through each well and column in the grouped dataframe
    for (name, df), ax in zip(grouped, axs.flat):
        ax.set_xlim(0,9)
    
        #Setup the depth range
        ax.set_ylim(5000, 0)
    
        #Create multiple fill betweens for each curve# This is between
        # the number representing null values and the number representing
        # actual values
    
        ax.fill_betweenx(df.DEPTH, 0, df.CALI, facecolor='grey')
        ax.fill_betweenx(df.DEPTH, 1, df.BS, facecolor='lightgrey')
        ax.fill_betweenx(df.DEPTH, 2, df.GR, facecolor='mediumseagreen')
        ax.fill_betweenx(df.DEPTH, 3, df.NEU, facecolor='lightblue')
        ax.fill_betweenx(df.DEPTH, 4, df.DEN, facecolor='lightcoral')
        ax.fill_betweenx(df.DEPTH, 5, df.PEF, facecolor='violet')
        ax.fill_betweenx(df.DEPTH, 6, df.RDEP, facecolor='darksalmon')
        ax.fill_betweenx(df.DEPTH, 7, df.RMED, facecolor='wheat')
        ax.fill_betweenx(df.DEPTH, 8, df.AC, facecolor='thistle')
        ax.fill_betweenx(df.DEPTH, 9, df.ACS, facecolor='tan')
    
        #Setup the grid, axis labels and ticks
        ax.grid(axis='x', alpha=0.5, color='black')
        ax.set_ylabel('DEPTH (m)', fontsize=14, fontweight='bold')
    
        #Position vertical lines at the boundaries between the bars
        ax.set_xticks([1,2,3,4,5,6,7,8,9,10], minor=False)
    
        #Position the curve names in the centre of each column
        ax.set_xticks([0.5, 1.5 ,2.5 ,3.5 ,4.5 ,5.5 ,6.5 , 7.5, 8.5, 9.5], minor=True)
    
        #Setup the x-axis tick labels
        ax.set_xticklabels(labels,  rotation='vertical', minor=True, verticalalignment='bottom')
        ax.set_xticklabels('', minor=False)
        ax.tick_params(axis='x', which='minor', pad=-10)
    
        #Assign the well name as the title to each subplot
        ax.set_title(name, fontsize=16, fontweight='bold')

    plt.savefig('missingdata.png')
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.15, wspace=0.25)
    plt.show()
    return ax, axs, df, fig, labels, name


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        From this plot we can determine:  
        **15/9-F-1 C**
        * Minor gaps in the gamma ray and resistivity curves. As the gaps appear at same position on both resistivity curves we can make an initial assumption that they may be related to casing shoes. Further investigation would be needed to confirm this.
        * Nuclear curves (DEN, NEU, PEF) and the caliper are only run over a short section, possibly indicating the zone of interest.
        * No acoustic curves (AC and ACS)

        **15/9-F-4**
        * Contains all available curves, with the majority over a small section towards the bottom of the well. 
        * There are multiple gaps in the gamma ray (GR) and acoustic shear (ACS) curves. Could be tool related. Further investigation would reveal the cause.

        **15/9-F-7**
        * Minimal amount of data present over a short and shallow section.
        * Only bitsize, gamma ray and resistivity measurements presents.
        * Could potentially be caused by a tool failure or issues encountered whilst drilling. This information could be confirmed by reviewing the End of Well Reports, if they are available.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
