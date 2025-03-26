import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import missingno as mno
    return mno, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Load Data
        """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv('Data/Xeek_train_subset_clean.csv')
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Explore Data
        """
    )
    return


@app.cell
def _(df):
    df['LITH'].nunique()
    return


@app.cell
def _(df):
    df['LITH'].unique()
    return


@app.cell
def _(df, sns):
    _g = sns.FacetGrid(df, col='LITH', col_wrap=4)
    _g.map(sns.scatterplot, 'NPHI', 'RHOB', alpha=0.5)
    _g.set(xlim=(-0.15, 1))
    _g.set(ylim=(3, 1))
    return


@app.cell
def _(df, sns):
    _g = sns.FacetGrid(df, col='LITH', col_wrap=4)
    _g.map(sns.scatterplot, 'DTC', 'RHOB', alpha=0.5)
    _g.set(xlim=(40, 240))
    _g.set(ylim=(3, 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Deal With Missing Data
        """
    )
    return


@app.cell
def _(df, mno):
    mno.bar(df)
    return


@app.cell
def _(df):
    df.dropna(inplace=True)
    return


@app.cell
def _(df, mno):
    mno.bar(df)
    return


@app.cell
def _(df):
    df['LITH'].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating the Random Forest Model
        ### Preparing Data
        """
    )
    return


@app.cell
def _():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    from sklearn.ensemble import RandomForestClassifier
    return (
        RandomForestClassifier,
        accuracy_score,
        classification_report,
        confusion_matrix,
        train_test_split,
    )


@app.cell
def _(df):
    # Select inputs and target
    X = df[['RDEP', 'RHOB', 'GR', 'NPHI', 'PEF', 'DTC']]
    y = df['LITH']
    return X, y


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Creating Model
        """
    )
    return


@app.cell
def _(RandomForestClassifier):
    clf = RandomForestClassifier()
    return (clf,)


@app.cell
def _(X_train, clf, y_train):
    clf.fit(X_train, y_train)
    return


@app.cell
def _(X_test, clf):
    y_pred = clf.predict(X_test)
    return (y_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Evaluating Model
        """
    )
    return


@app.cell
def _(accuracy_score, y_pred, y_test):
    accuracy_score(y_test, y_pred)
    return


@app.cell
def _(classification_report, y_pred, y_test):
    print(classification_report(y_test, y_pred))
    return


@app.cell
def _():
    # Classification Report
    return


@app.cell
def _(confusion_matrix, y_pred, y_test):
    # Confusion Matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    print(cf_matrix)
    return (cf_matrix,)


@app.cell
def _():
    labels = ['Shale', 'Sandstone', 'Sandstone/Shale', 'Limestone', 'Tuff',
           'Marl', 'Anhydrite', 'Dolomite', 'Chalk', 'Coal', 'Halite']
    labels.sort()
    return (labels,)


@app.cell
def _(cf_matrix, labels, plt, sns):
    fig = plt.figure(figsize=(10,10))
    ax = sns.heatmap(cf_matrix, annot=True, cmap='Reds', fmt='.0f',
                    xticklabels=labels, 
                    yticklabels = labels)

    ax.set_title('Seaborn Confusion Matrix with labels\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');
    return ax, fig


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
