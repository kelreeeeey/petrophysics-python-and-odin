import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Gamma Ray Normalisation
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **Created by:** Andy McDonald  

        This notebook illustrates carry out a simple normalisation on Gamma Ray data from the Volve Dataset.
        Medium Article Link: 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What is Normalization?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Normalization is the process of re-scaling or re-calibrating the well logs so that they are consistent with other logs in other wells within the field. This can be achieved by applying a single point normalization (linear shift) or a two point normalization ('stretch and squeeze') to the required curve. 

        Normalization is commonly applied to gamma ray logs, but can be applied to neutron porosity, bulk density, sonic and spontaneous potential logs. Resistivity logs are generally not normalized unless there is a sufficient reason to do so (Shier, 2004). It should be noted that applying normalization can remove geological variations and features across the study area and should be considered carefully. Shier (2004) provides an excellent discussion and guidelines on how to carry out normalization on well log data.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading and Checking Data
        The first step is to import the required libraries: pandas and matplotlib.
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


@app.cell
def _(data):
    data['WELL'].unique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using the unique method on the dataframe, we can see that we have 3 wells within this Volve Data subset:  
        - 15/9-F-1 C
        - 15/9-F-4
        - 15/9-F-7
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting the Raw Data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell
def _(data):
    wells = data.groupby('WELL')
    wells.head()
    return (wells,)


@app.cell
def _(wells):
    wells.min()
    return


@app.cell
def _(plt, wells):
    (_fig, _ax) = plt.subplots(figsize=(8, 6))
    for (_label, _df) in wells:
        _df.GR.plot(kind='kde', ax=_ax, label=_label)
        plt.xlim(0, 200)
    plt.grid(True)
    plt.legend()
    plt.savefig('before_normalisation.png', dpi=300)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        From the plot above, we will assume that the key well is 15/9-F-7 and we will normalise the other two datasets to this one.  
  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Calculating the Percentiles
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is possible that datasets can contain erroneous values which may affect the minimum and the maximum values within a curve. Therefore, some interpreters prefer to base their normalisation parameters on percentiles.  
  
        In this example, I have used the 5th and 95th percentiles.

        The first step is to calculate the percentile (or quantile as pandas refers to it) by grouping the data by wells and then applying the .quantile method to a specific column. In this case, GR. The quantile function takes in a decimal value, so a value of 0.05 is equivalent to the 5th percentile and 0.95 is equivalent to the 95th percentile.  
        """
    )
    return


@app.cell
def _(data):
    gr_percentile_05 = data.groupby('WELL')['GR'].quantile(0.05)
    print(gr_percentile_05)
    return (gr_percentile_05,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This calculation generates a pandas Series object. We can see what is in the series by calling upon it like so.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So now we need to bring that back into our main dataframe. We can do this using the map function, which will combine two data series that share a common column. Once it is mapped we can call upon the `.describe()` method and confirm that it has been added to the dataframe.
        """
    )
    return


@app.cell
def _(data, gr_percentile_05):
    data['05_PERC'] = data['WELL'].map(gr_percentile_05)
    return


@app.cell
def _(data):
    data.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can then repeat the process for the 95th percentile:
        """
    )
    return


@app.cell
def _(data):
    gr_percentile_95 = data.groupby('WELL')['GR'].quantile(0.95)
    return (gr_percentile_95,)


@app.cell
def _(gr_percentile_95):
    gr_percentile_95
    return


@app.cell
def _(data, gr_percentile_95):
    data['95_PERC'] = data['WELL'].map(gr_percentile_95)
    return


@app.cell
def _(data):
    data.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Create the Normalisation Function
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In order to normalize the data, we need create a custom function.  
        The following equation comes from Daniel Shier: 'Well Log Normalization: Methods and Guidelines'.

        $$Curve_{norm} = Ref_{low} +(Ref_{high}-Ref_{low}) * \Bigg[ \frac {CurveValue - Well_{low}}{ Well_{high} - Well_{low}}\Bigg]$$
        """
    )
    return


@app.cell
def normalise():
    def normalise(curve, ref_low, ref_high, well_low, well_high):
        return ref_low + ((ref_high - ref_low) * ((curve - well_low) / (well_high - well_low)))
    return (normalise,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can now set of key well high and low parameters.
        """
    )
    return


@app.cell
def _():
    key_well_low = 25.6464
    key_well_high = 110.5413
    return key_well_high, key_well_low


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To apply the function to each value and use the correct percentiles for each well we can use the `apply()` method to the pandas dataframe and then a `lamda` function for our custom function.
        """
    )
    return


@app.cell
def _(data, key_well_high, key_well_low, normalise):
    data['GR_NORM'] = data.apply(lambda x: normalise(x['GR'], key_well_low, key_well_high, 
                                                     x['05_PERC'], x['95_PERC']), axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting the Normalized Data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To view our final normalized data, we can re-use the code from above to generate the histogram. When we do, we can see that all curves have been normalized to our reference well.
        """
    )
    return


@app.cell
def _(plt, wells):
    (_fig, _ax) = plt.subplots(figsize=(8, 6))
    for (_label, _df) in wells:
        _df.GR_NORM.plot(kind='kde', ax=_ax, label=_label)
        plt.xlim(0, 200)
    plt.grid(True)
    plt.legend()
    plt.savefig('after_normalisation.png', dpi=300)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
