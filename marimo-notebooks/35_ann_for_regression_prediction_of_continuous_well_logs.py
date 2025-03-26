import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Scikit Learn ANN for Predicting Continuous Well Measurements
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        med_tutorial_scikit_learn_1.py
        """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv('Data/Volve/volve_wells.csv', usecols=['WELL', 'DEPTH', 'RHOB', 'GR', 'NPHI', 'PEF', 'DT'])
    return (df,)


@app.cell
def _(df):
    df_1 = df.dropna()
    return (df_1,)


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
def _(df_1):
    df_1
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
    training_wells = ['15/9-F-11 A', '15/9-F-1 A']

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
def _(df_1, test_well, training_wells):
    train_val_df = df_1[df_1['WELL'].isin(training_wells)].copy()
    test_df = df_1[df_1['WELL'].isin(test_well)].copy()
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
        ## Proprocessing
        """
    )
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
    from sklearn.neural_network import MLPRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn import metrics
    return MLPRegressor, StandardScaler, metrics, train_test_split


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
        ### Applying Standard Scaler
        """
    )
    return


@app.cell
def _(StandardScaler):
    scaler = StandardScaler()
    return (scaler,)


@app.cell
def _(X_train, scaler):
    X_train_1 = scaler.fit_transform(X_train)
    return (X_train_1,)


@app.cell
def _(X_train_1):
    X_train_1
    return


@app.cell
def _(X_val, scaler):
    X_val_1 = scaler.transform(X_val)
    return (X_val_1,)


@app.cell
def _(X_val_1):
    X_val_1
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform (X_test)
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
def _(MLPRegressor):
    model = MLPRegressor(hidden_layer_sizes=(64, 64,64), 
                         activation="relu" ,
                         random_state=42, max_iter=2000)
    return (model,)


@app.cell
def _(X_train_1, model, y_train):
    model.fit(X_train_1, y_train)
    return


@app.cell
def _(X_val_1, model):
    y_pred = model.predict(X_val_1)
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
    mae = metrics.mean_absolute_error(y_val, y_pred)
    return (mae,)


@app.cell
def _(metrics, y_pred, y_val):
    mse = metrics.mean_squared_error(y_val, y_pred)
    rmse = mse**0.5
    return mse, rmse


@app.cell
def _(rmse):
    rmse
    return


@app.cell
def _(metrics, y_pred, y_val):
    r2 = metrics.r2_score(y_val, y_pred)
    r2
    return (r2,)


@app.cell
def _(mae, r2, rmse):
    print(f"""
    MAE: \t{mae:.2f}
    RMSE: \t{rmse:.2f}
    r2: \t{r2:.2f}
    """)
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
    plt.show()
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
def _(scaler, test_well_x):
    test_well_x_1 = scaler.transform(test_well_x)
    return (test_well_x_1,)


@app.cell
def _(model, test_df, test_well_x_1):
    test_df['TEST_DT'] = model.predict(test_well_x_1)
    return


@app.cell
def _(plt, test_df):
    plt.scatter(test_df['DT'], test_df['TEST_DT'])
    plt.xlim(40, 140)
    plt.ylim(40, 140)
    plt.ylabel('Predicted DT')
    plt.xlabel('Actual DT')
    plt.plot([40,140], [40,140], 'black') #1 to 1 line
    plt.show()
    return


@app.cell
def _(plt, test_df):
    plt.figure(figsize=(12, 4))
    plt.plot(test_df['DEPTH'], test_df['DT'], label='Actual DT')
    plt.plot(test_df['DEPTH'], test_df['TEST_DT'], label='Predicted DT')

    plt.xlabel('Depth (m)', fontsize=14, fontweight='bold')
    plt.ylabel('DT', fontsize=14,fontweight='bold')

    plt.ylim(40, 140)
    plt.legend(fontsize=14)
    plt.grid()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
