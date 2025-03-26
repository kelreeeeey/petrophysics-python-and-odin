import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Creating Boxplots of Well Log Data in Seaborn
        *Created by: Andy McDonald*  
        *Article Version: 1.0*  


        ## What are Boxplots?
        A boxplot is a graphical and standardised way to display the distribution of data based on five key numbers: The "minimum",  1st Quartile (25th percentile), median (2nd Quartile./ 50th Percentile), the 3rd Quartile (75th percentile) and the "maximum". The minimum and maximum values are defined as Q1 - 1.5 * IQR  and Q3 + 1.5 * IQR respectively. Any points that fall outside of these limits are referred to as outliers.


        ![image.png](attachment:9e27f2a8-581e-4fb0-8e6e-d1d055db10ec.png)


        Boxplots can be used to:
        - Identify outliers or anomalous data points
        - To determine if our data is skewed
        - To understand the spread/range of the data

        To construct a boxplot, we first start with the median value / 50th percentile (Q2). This represents the middle value within our data.

        A box is then formed between the 25th and 75th percentiles (Q1 and Q3 respectively). The range represented by this box is known as the inter-quartile range (IQR). 

        From this box extends lines, which are also knwon as the whiskers. These extend to Q1 - 1.5 * IQR and Q3 + 1.5 * IQR or to the last data point if it is less than this value. 

        Any points that fall beyond the whisker limits are known as outliers.


        ## Dataset
        The dataset we are using for this tutorial forms part of a Machine Learning competition run by Xeek and FORCE 2020 (https://doi.org/10.5281/zenodo.4351155). The objective of the compettion was to predict lithology from existing labelled data. The dataset consists of 118 wells from the Norwegian Sea.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating Boxplots with Seaborn
        ### Importing Libraries and Data
        """
    )
    return


@app.cell
def _():
    import seaborn as sns
    import pandas as pd
    return pd, sns


@app.cell
def _(pd):
    df = pd.read_csv('Data/Xeek_train_subset_clean.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating a Boxplot for a Column
        """
    )
    return


@app.cell
def _(df, sns):
    sns.boxplot(x=df['GR']);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell
def _(df, sns):
    sns.boxplot(y=df['GR']);
    return


@app.cell
def _(df, sns):
    sns.boxplot( x=df['LITH'], y=df['GR']);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Changing the Size of the Figure
        """
    )
    return


@app.cell
def _(df, sns):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, figsize=(10, 10))

    sns.boxplot(x=df['LITH'], y=df['GR']);
    plt.xticks(rotation = 90)
    plt.show()
    return ax, fig, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Styling the Boxplot
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Changing the grid
        """
    )
    return


@app.cell
def _(df, sns):
    sns.set(rc={"figure.figsize":(10, 10)})

    sns.set_style('whitegrid')
    sns.boxplot( y=df['LITH'], x=df['GR']);
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Changing the box colour to a single colour
        """
    )
    return


@app.cell
def _(df, sns):
    sns.set_style('whitegrid')
    sns.boxplot( y=df['LITH'], x=df['GR'], color='red');
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Changing the box colour to a palette
        """
    )
    return


@app.cell
def _(df, sns):
    sns.set_style('whitegrid')
    sns.boxplot( y=df['LITH'], x=df['GR'], palette='Blues');
    return


@app.cell
def _(df, sns):
    _p = sns.boxplot(y=df['LITH'], x=df['GR'])
    _p.set_xlabel('Gamma Ray', fontsize=14, fontweight='bold')
    _p.set_ylabel('Lithology', fontsize=14, fontweight='bold')
    _p.set_title('Gamma Ray Distribution by Lithology', fontsize=16, fontweight='bold')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Setting Outlier (flier) Style
        """
    )
    return


@app.cell
def _(df, sns):
    flierprops = dict(marker='o', markersize=5, markeredgecolor='black', markerfacecolor='green', alpha=0.5)
    _p = sns.boxplot(y=df['LITH'], x=df['GR'], flierprops=flierprops)
    _p.set_xlabel('Gamma Ray', fontsize=14, fontweight='bold')
    _p.set_ylabel('Lithology', fontsize=14, fontweight='bold')
    _p.set_title('Gamma Ray Distribution by Lithology', fontsize=16, fontweight='bold')
    return (flierprops,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # References

        Bormann, Peter, Aursand, Peder, Dilib, Fahad, Manral, Surrender, & Dischington, Peter. (2020). FORCE 2020 Well well log and lithofacies dataset for machine learning competition [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4351156
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
