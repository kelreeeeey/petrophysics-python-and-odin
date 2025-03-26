import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    import pandas as pd

    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    import seaborn as sns
    import matplotlib.pyplot as plt
    return (
        KNeighborsClassifier,
        StandardScaler,
        accuracy_score,
        classification_report,
        confusion_matrix,
        pd,
        plt,
        sns,
        train_test_split,
    )


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
    df_1 = df.dropna()
    return (df_1,)


@app.cell
def _(df_1):
    X = df_1[['RDEP', 'RHOB', 'GR', 'NPHI', 'PEF', 'DTC']]
    y = df_1['LITH']
    return X, y


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_test, X_train, y_test, y_train


@app.cell
def _(StandardScaler, X_test, X_train):
    scaler = StandardScaler()
    X_train_1 = scaler.fit_transform(X_train)
    X_test_1 = scaler.transform(X_test)
    return X_test_1, X_train_1, scaler


@app.cell
def _(KNeighborsClassifier):
    clf = KNeighborsClassifier()
    return (clf,)


@app.cell
def _(X_train_1, clf, y_train):
    clf.fit(X_train_1, y_train)
    return


@app.cell
def _(X_test_1, clf):
    y_pred = clf.predict(X_test_1)
    return (y_pred,)


@app.cell
def _(accuracy_score, y_pred, y_test):
    accuracy_score(y_test, y_pred)
    return


@app.cell
def _(classification_report, y_pred, y_test):
    print(classification_report(y_test, y_pred))
    return


@app.cell
def _(X_test_1):
    test_data = X_test_1.copy()
    return (test_data,)


@app.cell
def _(X_test_1, clf, test_data):
    test_data['PRED_LITH'] = clf.predict(X_test_1)
    return


@app.cell
def _(test_data):
    test_data
    return


@app.cell
def _(sns, test_data):
    _g = sns.FacetGrid(test_data, col='ACT_LITH', col_wrap=4, col_order=['Shale', 'Sandstone', 'Sandstone/Shale', 'Limestone', 'Tuff', 'Marl', 'Anhydrite', 'Dolomite', 'Chalk', 'Coal', 'Halite'])
    _g.map(sns.scatterplot, 'NPHI', 'RHOB', alpha=0.5)
    _g.set(xlim=(-0.15, 1))
    _g.set(ylim=(3, 1))
    return


@app.cell
def _(sns, test_data):
    _g = sns.FacetGrid(test_data, col='PRED_LITH', col_wrap=4, col_order=['Shale', 'Sandstone', 'Sandstone/Shale', 'Limestone', 'Tuff', 'Marl', 'Anhydrite', 'Dolomite', 'Chalk', 'Coal', 'Halite'])
    _g.map(sns.scatterplot, 'NPHI', 'RHOB', alpha=0.5)
    _g.set(xlim=(-0.15, 1))
    _g.set(ylim=(3, 1))
    return


@app.cell
def _(confusion_matrix, plt, sns, y_pred, y_test):
    # Confusion Matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    print(cf_matrix)

    labels = ['Shale', 'Sandstone', 'Sandstone/Shale', 'Limestone', 'Tuff',
           'Marl', 'Anhydrite', 'Dolomite', 'Chalk', 'Coal', 'Halite']
    labels.sort()

    fig = plt.figure(figsize=(10,10))
    ax = sns.heatmap(cf_matrix, annot=True, cmap='Reds', fmt='.0f',
                    xticklabels=labels, 
                    yticklabels = labels)

    ax.set_title('Seaborn Confusion Matrix with labels\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');
    return ax, cf_matrix, fig, labels


if __name__ == "__main__":
    app.run()
