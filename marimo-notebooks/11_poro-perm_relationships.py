import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # 11 - Porosity-Permeability Relationships Using Linear Regression in Python  
  
        **Created By:** Andy McDonald  
        **Link to Article:** 
  
        Core data analysis is a key component in the evaluation of a field or discovery, as it provides direct samples of the geological formations in the subsurface over the interval of interest. It is often considered the 'ground truth' by many and is used as a reference for calibrating well log measurements and petrophysical analysis. Core data is expensive to obtain and not acquired on every well at every depth. Instead, it may be acquired at discrete intervals on a small number of wells within a field and then used as a reference for other wells.  
  
        Once the core data has been extracted from the well it is taken to a lab to be analysed. Along the length of the retrieved core sample a number of measurements are made. Two of which are porosity and permeability, both key components of a petrophysical analysis.

        **Porosity** is defined as the volume of space between the solid grains relative to the total rock volume. It provides an indication of the potential storage space for hydrocarbons. 
  
        **Permeability** provides an indication of how easy fluids can flow through the rock.

        Porosity is a key control on permeability, with larger pores resulting in wider pathways for the reservoir fluids to flow through.  
  
        Well logging tools do not provide a direct measurement for permeability and therefore it has to be inferred through relationships with core data from the same field or well, or from empirically derived equations.  
  
        One common method is to plot porosity (on a linear scale) against permeability (on a logarithmic scale) and observe the trend. From this, a regression can be applied to the porosity permeability (poro-perm) crossplot to derive an equation, which can subsequently be used to predict a continuous permeability from a computed porosity in any well.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To begin, we will import a number of common libraries before we start working with the actual data. For this article we will be using pandas, matplotlib and numpy. These three libraries allow us to load, work with and visualise our data.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    return np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The dataset we are using comes from the publicly available Equinor Volve Field dataset released in 2018. This file is from 15/9- 19A which contained full regular core analysis data. To load this data in we can use pd.read_csv and pass in the file name.  
  
        This dataset has already been depth aligned to well log data, so no adjustments to the sample depth are required.  
  
        When core slabs are analysed, a limited number of measurements are made at irregular intervals. In some cases, measurements may not be possible, for example in really tight (low permeability) sections. As a result, we can tell pandas to load any missing values / blank cells as Not a Number (NaN) by adding the argument na_values=' ' .
        """
    )
    return


@app.cell
def _(pd):
    core_data = pd.read_csv("Data/15_9-19A-CORE.csv", na_values=' ')
    return (core_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once we have the data loaded, we can view the details of what is in it by calling upon the `.head()` and `.describe()` methods.  
  
        The `.head()` method returns the first five rows of the dataframe and the header row.
        """
    )
    return


@app.cell
def _(core_data):
    core_data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `.describe()` method returns useful statistics about the numeric data contained within the dataframe such as the mean, standard deviation, maximum and minimum values.
        """
    )
    return


@app.cell
def _(core_data):
    core_data.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plottting Porosity vs Permeability
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using our core_data dataframe we can simply and quickly plot our data by adding .plot to the end of our dataframe and supplying some arguments. In this case we want a scatter plot (also known in petrophysics as a crossplot), with the x-axis as CPOR - Core Porosity and the y-axis as CKH - Core Permeability.
        """
    )
    return


@app.cell
def _(core_data):
    core_data.plot(kind="scatter", x="CPOR", y="CKHG")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        From this scatter plot we notice that there is a large concentration of points at low permeabilities with a few points at the higher end. We can tidy up our plot by converting the y axis to a logaritmic scale and adding a grid. This generates the the poro-perm crossplot that we are familiar with in petrophysics.
        """
    )
    return


@app.cell
def _(core_data, plt):
    core_data.plot(kind="scatter", x="CPOR", y="CKHG")
    plt.yscale('log')
    plt.grid(True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can agree that this looks much better now. We can further tidy up the plot by:
        * Switching to matplotlib for making out plot
        * Adding labels by using ax.set_ylabel() and ax.set_xlabel()
        * Setting ranges for the axis using ax.axis([0,40, 0.01, 100000)
        * Making the y-axis values easier to read by converting the exponential notation to full numbers. This is done using FuncFormatter from matplotlib and setting up a simple for loop
        """
    )
    return


@app.cell
def _(core_data, plt):
    from matplotlib.ticker import FuncFormatter
    (_fig, _ax) = plt.subplots()
    _ax.axis([0, 40, 0.01, 100000])
    _ax.plot(core_data['CPOR'], core_data['CKHG'], 'bo')
    _ax.set_yscale('log')
    _ax.grid(True)
    _ax.set_ylabel('Core Perm (mD)')
    _ax.set_xlabel('Core Porosity (%)')
    for _axis in [_ax.yaxis, _ax.xaxis]:
        _formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
        _axis.set_major_formatter(_formatter)
    plt.savefig('11-xplot-semi-log-fixed.png', dpi=300)
    return (FuncFormatter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Isn't that much better than the previous plot? We can now use this nicer looking plot within a petrophysical report or passing to other subsurface people within the team.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Deriving Relationship Between Porosity and Permeability
        There are two ways that we can carry out a poro-perm regression on our data:
        * Using numpy's polyfit function
        * Applying a regression using the statsmodels library

        Before we explore each option, we first have to create a copy of our dataframe and remove the null rows. Carrying out the regression with NaN values can result in errors.
        """
    )
    return


@app.cell
def _(core_data):
    poro_perm = core_data[['CPOR', 'CKHG']].copy()
    return (poro_perm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once it has been copied we can then drop the NaNs using dropna(). Including the argument inplace=True tells the method to replace the values in place rather than returning a copy of the dataframe.
        """
    )
    return


@app.cell
def _(poro_perm):
    poro_perm.dropna(inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Numpy polyfit()
        The simplest option for applying a linear regression through the data is using the polynomial fit function from numpy. This returns an array of co-efficients. As we are wanting to use a linear fit we can specify a value of 1 at the end of the function. This tells the function we want a first degree polynomial.  
  
        Also, are we are dealing with permeability data in the logarithmic scale, we need to take the logarithm of the values using np.log10.
        """
    )
    return


@app.cell
def _(np, poro_perm):
    poro_perm_polyfit = np.polyfit(poro_perm['CPOR'], np.log10(poro_perm['CKHG']), 1)
    return (poro_perm_polyfit,)


@app.cell
def _(poro_perm_polyfit):
    poro_perm_polyfit
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The first value is our slope and the second is our y-intercept.  
  
        Polyfit doesn't give us much more information about the regression such as the co-efficient of determination (R-squared). For this we need to look at another model.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Statsmodels Linear Regression
        The second option for generating a poro-perm linear regression is to use the Ordinary Least Squares (OLS) method from the statsmodels library.   
  
        First we need to import the library and create our data. We will assign our x value as Core Porosity (CPOR) and our y value as the log10 of Core Permeability (CKH). The y value will be the one we are aiming to build our prediction model from.  
  
        With the statsmodel OLS we need to add a constant column to our data as an intercept is not included by default unless we are using formulas. See here for the documentation.
        """
    )
    return


@app.cell
def _(core_data, np):
    import statsmodels.api as sm

    x = core_data['CPOR']
    x = sm.add_constant(x)
    y = np.log10(core_data['CKHG'])
    return sm, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can confirm the values of x by calling upon it and in Jupyter it will return a dataframe as seen here:
        """
    )
    return


@app.cell
def _(x):
    x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The next step is to build and fit our model. With the OLS method, we can supply an argument for missing values. In this example I have set it to drop. This will remove or drop the missing values from the data.
        """
    )
    return


@app.cell
def _(sm, x, y):
    model = sm.OLS(y, x, missing='drop')
    results = model.fit()
    return model, results


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Once we have fitted the model, we can view a full summary of the regression by calling upon `.summary()`  
  
          Which returns a nicely formatted table like the one below and includes key statistics as the R-squared and standard error.
        """
    )
    return


@app.cell
def _(results):
    results.summary()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also obtain the key parameters: slope and intercept, by calling upon `results.params`.
        """
    )
    return


@app.cell
def _(results):
    results.params
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If we want to access one of the parameters, for example the slope or constant for the CPOR value, we can access it like a list:
        """
    )
    return


@app.cell
def _(results):
    results.params[1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Finally, we can take our equation and apply it to our scatter plot.
        """
    )
    return


@app.cell
def _(FuncFormatter, core_data, plt, results):
    (_fig, _ax) = plt.subplots()
    _ax.axis([0, 30, 0.01, 100000])
    _ax.semilogy(core_data['CPOR'], core_data['CKHG'], 'bo')
    _ax.grid(True)
    _ax.set_ylabel('Core Perm (mD)')
    _ax.set_xlabel('Core Porosity (%)')
    _ax.semilogy(core_data['CPOR'], 10 ** (results.params[1] * core_data['CPOR'] + results.params[0]), 'r-')
    for _axis in [_ax.yaxis, _ax.xaxis]:
        _formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
        _axis.set_major_formatter(_formatter)
    plt.savefig('predicted_poro_perm_xplot.png', dpi=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Predicting a Continuous Permeability from Log Porosity
        Now that we have our equation and we are happy with the results, we can apply this to our log porosity to generate a continuous permeability curve.  
  
        First, we need to load in the well log data for this well:
        """
    )
    return


@app.cell
def _(pd):
    well = pd.read_csv('Data/15_9-19.csv', skiprows=[1])
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When we check the well header using well.head()we can see our newly created curve at the end of the dataframe:
        """
    )
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell
def _(results, well):
    well['PERM']= 10**(results.params[1] * (well['PHIT']*100) + results.params[0])
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Visualising the Final Predicted Curve
        The final step in our workflow is to plot the PHIT curve and the predicted permeability curve on a log plot alongside the core measurements.  
  
          This generates a simple two track log plot with our core measurements represented by black dots and our continuous curves by blue lines.
        """
    )
    return


@app.cell
def _(core_data, plt, well):
    (_fig, _ax) = plt.subplots(figsize=(5, 10))
    _ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1, sharey=_ax1)
    _ax1.plot(core_data['CPOR'] / 100, core_data['DEPTH'], color='black', marker='.', linewidth=0)
    _ax1.plot(well['PHIT'], well['DEPTH'], color='blue', linewidth=0.5)
    _ax1.set_xlabel('Porosity')
    _ax1.set_xlim(0.5, 0)
    _ax1.xaxis.label.set_color('black')
    _ax1.tick_params(axis='x', colors='black')
    _ax1.spines['top'].set_edgecolor('black')
    _ax1.set_xticks([0.5, 0.25, 0])
    _ax2.plot(core_data['CKHG'], core_data['DEPTH'], color='black', marker='.', linewidth=0)
    _ax2.plot(well['PERM'], well['DEPTH'], color='blue', linewidth=0.5)
    _ax2.set_xlabel('Permeability')
    _ax2.set_xlim(0.1, 100000)
    _ax2.xaxis.label.set_color('black')
    _ax2.tick_params(axis='x', colors='black')
    _ax2.spines['top'].set_edgecolor('black')
    _ax2.set_xticks([0.01, 1, 10, 100, 10000])
    _ax2.semilogx()
    for _ax in [_ax1, _ax2]:
        _ax.set_ylim(4025, 3825)
        _ax.grid(which='major', color='lightgrey', linestyle='-')
        _ax.xaxis.set_ticks_position('top')
        _ax.xaxis.set_label_position('top')
    for _ax in [_ax2]:
        plt.setp(_ax.get_yticklabels(), visible=False)
    plt.tight_layout()
    _fig.subplots_adjust(wspace=0.3)
    plt.savefig('final_track_plot.png', dpi=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As seen in track 2, our predicted permeability from a simple linear regression tracks the core permeability reasonably well. However, between about 3860 and 3875, our prediction reads lower than the actual core measurements. Also, it becomes harder to visualise the correlation at the lower interval to the more thinly bedded nature of the geology.  
  
          We can build up a final plot like so.
        """
    )
    return


@app.cell
def _(core_data, plt, well):
    (_fig, _ax) = plt.subplots(figsize=(15, 10))
    _ax1 = plt.subplot2grid((1, 8), (0, 0), rowspan=1, colspan=1)
    _ax2 = plt.subplot2grid((1, 8), (0, 1), rowspan=1, colspan=1, sharey=_ax1)
    ax3 = plt.subplot2grid((1, 8), (0, 2), rowspan=1, colspan=1, sharey=_ax1)
    ax4 = plt.subplot2grid((1, 8), (0, 3), rowspan=1, colspan=1, sharey=_ax1)
    ax5 = ax3.twiny()
    ax6 = plt.subplot2grid((1, 8), (0, 4), rowspan=1, colspan=1, sharey=_ax1)
    ax7 = _ax2.twiny()
    ax8 = plt.subplot2grid((1, 8), (0, 5), rowspan=1, colspan=1, sharey=_ax1)
    ax9 = plt.subplot2grid((1, 8), (0, 6), rowspan=1, colspan=1, sharey=_ax1)
    ax10 = _ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = _ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax6.twiny()
    ax14.xaxis.set_visible(False)
    _ax1.plot(well['GR'], well['DEPTH'], color='green', linewidth=0.5)
    _ax1.set_xlabel('Gamma')
    _ax1.xaxis.label.set_color('green')
    _ax1.set_xlim(0, 200)
    _ax1.set_ylabel('Depth (m)')
    _ax1.tick_params(axis='x', colors='green')
    _ax1.spines['top'].set_edgecolor('green')
    _ax1.title.set_color('green')
    _ax1.set_xticks([0, 50, 100, 150, 200])
    _ax2.set_xlabel('Resistivity - Deep')
    _ax2.set_xlim(0.2, 2000)
    _ax2.xaxis.label.set_color('red')
    _ax2.tick_params(axis='x', colors='red')
    _ax2.spines['top'].set_edgecolor('red')
    _ax2.set_xticks([0.1, 1, 10, 100, 1000])
    _ax2.semilogx()
    ax3.plot(well['RHOB'], well['DEPTH'], color='red', linewidth=0.5)
    ax3.set_xlabel('Density')
    ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color('red')
    ax3.tick_params(axis='x', colors='red')
    ax3.spines['top'].set_edgecolor('red')
    ax3.set_xticks([1.95, 2.45, 2.95])
    ax4.plot(well['DT'], well['DEPTH'], color='purple', linewidth=0.5)
    ax4.set_xlabel('Sonic')
    ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color('purple')
    ax4.tick_params(axis='x', colors='purple')
    ax4.spines['top'].set_edgecolor('purple')
    ax5.plot(well['NPHI'], well['DEPTH'], color='blue', linewidth=0.5)
    ax5.set_xlabel('Neutron')
    ax5.xaxis.label.set_color('blue')
    ax5.set_xlim(0.45, -0.15)
    ax5.tick_params(axis='x', colors='blue')
    ax5.spines['top'].set_position(('axes', 1.08))
    ax5.spines['top'].set_visible(True)
    ax5.spines['top'].set_edgecolor('blue')
    ax5.set_xticks([0.45, 0.15, -0.15])
    ax6.plot(well['CALI'], well['DEPTH'], color='black', linewidth=0.5)
    ax6.set_xlabel('Caliper')
    ax6.set_xlim(6, 16)
    ax6.xaxis.label.set_color('black')
    ax6.tick_params(axis='x', colors='black')
    ax6.spines['top'].set_edgecolor('black')
    ax6.fill_betweenx(well['DEPTH'], 8.5, well['CALI'], facecolor='yellow')
    ax6.set_xticks([6, 11, 16])
    ax7.set_xlabel('Resistivity - Med')
    ax7.set_xlim(0.2, 2000)
    ax7.xaxis.label.set_color('green')
    ax7.spines['top'].set_position(('axes', 1.08))
    ax7.spines['top'].set_visible(True)
    ax7.tick_params(axis='x', colors='green')
    ax7.spines['top'].set_edgecolor('green')
    ax7.set_xticks([0.1, 1, 10, 100, 1000])
    ax7.semilogx()
    ax8.plot(core_data['CPOR'] / 100, core_data['DEPTH'], color='black', marker='.', linewidth=0)
    ax8.plot(well['PHIT'], well['DEPTH'], color='blue', linewidth=0.5)
    ax8.set_xlabel('Porosity')
    ax8.set_xlim(0.5, 0)
    ax8.xaxis.label.set_color('black')
    ax8.tick_params(axis='x', colors='black')
    ax8.spines['top'].set_edgecolor('black')
    ax8.set_xticks([0.5, 0.25, 0])
    ax9.plot(core_data['CKHG'], core_data['DEPTH'], color='black', marker='.', linewidth=0)
    ax9.plot(well['PERM'], well['DEPTH'], color='blue', linewidth=0.5)
    ax9.set_xlabel('Permeability')
    ax9.set_xlim(0.1, 100000)
    ax9.xaxis.label.set_color('black')
    ax9.tick_params(axis='x', colors='black')
    ax9.spines['top'].set_edgecolor('black')
    ax9.set_xticks([0.01, 1, 10, 100, 10000])
    ax9.semilogx()
    for _ax in [_ax1, _ax2, ax3, ax4, ax6, ax8, ax9]:
        _ax.set_ylim(4100, 3800)
        _ax.grid(which='major', color='lightgrey', linestyle='-')
        _ax.xaxis.set_ticks_position('top')
        _ax.xaxis.set_label_position('top')
        _ax.spines['top'].set_position(('axes', 1.02))
    for _ax in [_ax2, ax3, ax4, ax6, ax8, ax9]:
        plt.setp(_ax.get_yticklabels(), visible=False)
    plt.tight_layout()
    _fig.subplots_adjust(wspace=0.15)
    return ax10, ax11, ax12, ax13, ax14, ax3, ax4, ax5, ax6, ax7, ax8, ax9


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Conclusion
        In this walkthrough, we have covered what core porosity and permeability area and how we can predict the latter from the former to generate an equation that can be used to predict a continuous curve. This can subsequently be used in geological models or reservoir simulations.
        As noted at the end, there are a few small mismatches. These would benefit from further investigation and potentially further modelling either by refining the regression or by applying another machine learning model.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
