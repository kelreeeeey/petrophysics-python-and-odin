import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Random Forest for Predicting Continuous Well Measurements
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Importing Libraries and Loading Data
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
    df = pd.read_csv('Data/Volve/volve_wells.csv', usecols=['WELL', 'DEPTH', 'RHOB', 'GR', 'NPHI', 'PEF', 'DT'])
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Create Training, Testing and Validation Datasets
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Our dataset should have 4 wells within it. We can confirm this by calling upon the `unique()` function
        """
    )
    return


@app.cell
def _(df):
    df['WELL'].unique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As we are using measurements taken from multiple wells, one way to split our data into training and testing is to set aside a single well (blind test well) which will be used to see how our model performs on unseen data.
        """
    )
    return


@app.cell
def _():
    # Training Wells
    training_wells = ['15/9-F-11 B', '15/9-F-11 A', '15/9-F-1 A']

    # Test Well
    test_well = ['15/9-F-1 B']
    return test_well, training_wells


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        "Extract" the data from the main dataframe using the well lists above
        """
    )
    return


@app.cell
def _(df, test_well, training_wells):
    train_val_df = df[df['WELL'].isin(training_wells)].copy()
    test_df = df[df['WELL'].isin(test_well)].copy()
    return test_df, train_val_df


@app.cell
def _(train_val_df):
    train_val_df.describe()
    return


@app.cell
def _(test_df):
    test_df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Remove NaN Values From Dataframe
        Removing missing values from the dataframe is one way to deal with them, however, doing so reduces the amount of training data you have available. Other methods can be used to infill the NaNs with sensible values.
        """
    )
    return


@app.cell
def _(test_df, train_val_df):
    train_val_df.dropna(inplace=True)
    test_df.dropna(inplace=True)
    train_val_df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Implementing the Random Forest Model
        """
    )
    return


@app.cell
def _():
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    return RandomForestRegressor, metrics, train_test_split


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Selecting Training and Target Features
        """
    )
    return


@app.cell
def _(train_val_df):
    X = train_val_df[['RHOB', 'GR', 'NPHI', 'PEF']]
    y = train_val_df['DT']
    return X, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Note that the name test used here is commonly used within machine learning. In this case the variables X_test and y_test are our validation data. In other words it is used to help tune our model. 
        """
    )
    return


@app.cell
def _(X, train_test_split, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    return X_train, X_val, y_train, y_val


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Checking the shapes of X_train and X_test to make sure they have been split correctly.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Building the Model
        """
    )
    return


@app.cell
def _(RandomForestRegressor):
    regr = RandomForestRegressor()
    return (regr,)


@app.cell
def _(X_train, regr, y_train):
    regr.fit(X_train, y_train)
    return


@app.cell
def _(X_val, regr):
    y_pred = regr.predict(X_val)
    return (y_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Check the Prediction Results
        """
    )
    return


@app.cell
def _(metrics, y_pred, y_val):
    metrics.mean_absolute_error(y_val, y_pred)
    return


@app.cell
def _(metrics, y_pred, y_val):
    mse = metrics.mean_squared_error(y_val, y_pred)
    rmse = mse**0.5
    return mse, rmse


@app.cell
def _(rmse):
    rmse
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Simple metrics like above are a nice way to see how a model has performed, but you should always check the actual data. 

        In the plot below, we are comparing the real data against the predicted data.
        """
    )
    return


@app.cell
def _(plt, y_pred, y_val):
    plt.scatter(y_val, y_pred)
    plt.xlim(40, 140)
    plt.ylim(40, 140)
    plt.ylabel('Predicted DT')
    plt.xlabel('Actual DT')
    plt.plot([40,140], [40,140], 'black') #1 to 1 line
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Test Well Prediction
        Once the model has been fine tuned, we can apply it to our blind test well and see how it performs.
        """
    )
    return


@app.cell
def _(test_df):
    test_well_x = test_df[['RHOB', 'GR', 'NPHI', 'PEF']]
    return (test_well_x,)


@app.cell
def _(regr, test_df, test_well_x):
    test_df['TEST_DT'] = regr.predict(test_well_x)
    return


@app.cell
def _(plt, test_df):
    plt.scatter(test_df['DT'], test_df['TEST_DT'])
    plt.xlim(40, 140)
    plt.ylim(40, 140)
    plt.ylabel('Predicted DT')
    plt.xlabel('Actual DT')
    plt.plot([40,140], [40,140], 'black') #1 to 1 line
    return


@app.cell
def _(plt, test_df):
    plt.figure(figsize=(15, 5))
    plt.plot(test_df['DEPTH'], test_df['DT'], label='Actual DT')
    plt.plot(test_df['DEPTH'], test_df['TEST_DT'], label='Predicted DT')
    plt.xlabel('Depth (m)')
    plt.ylabel('DT')
    plt.ylim(40, 140)
    plt.legend()
    plt.grid()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
