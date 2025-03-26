import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Importing Libraries & Data
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from sklearn.ensemble import IsolationForest
    return IsolationForest, pd, sns


@app.cell
def _(pd):
    df = pd.read_csv('Data/Xeek_Well_15-9-15.csv')
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df_1 = df.dropna()
    return (df_1,)


@app.cell
def _(df_1):
    df_1.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Building an Isolation Forest Model (2 Features)
        """
    )
    return


@app.cell
def _():
    anomaly_inputs = ['NPHI', 'RHOB']
    return (anomaly_inputs,)


@app.cell
def _(IsolationForest):
    model_IF = IsolationForest(contamination=0.1, random_state=42)
    return (model_IF,)


@app.cell
def _(anomaly_inputs, df_1, model_IF):
    model_IF.fit(df_1[anomaly_inputs])
    return


@app.cell
def _(anomaly_inputs, df_1, model_IF):
    df_1['anomaly_scores'] = model_IF.decision_function(df_1[anomaly_inputs])
    return


@app.cell
def _(anomaly_inputs, df_1, model_IF):
    df_1['anomaly'] = model_IF.predict(df_1[anomaly_inputs])
    return


@app.cell
def _(df_1):
    df_1.loc[:, ['NPHI', 'RHOB', 'anomaly_scores', 'anomaly']]
    return


@app.cell
def _(sns):
    def outlier_plot(data, outlier_method_name, x_var, y_var, 
                     xaxis_limits=[0,1], yaxis_limits=[0,1]):
    
        print(f'Outlier Method: {outlier_method_name}')
    
        method = f'{outlier_method_name}_anomaly'
    
        print(f"Number of anomalous values {len(data[data['anomaly']==-1])}")
        print(f"Number of non anomalous values  {len(data[data['anomaly']== 1])}")
        print(f'Total Number of Values: {len(data)}')
    
        g = sns.FacetGrid(data, col='anomaly', height=4, hue='anomaly', hue_order=[1,-1])
        g.map(sns.scatterplot, x_var, y_var)
        g.fig.suptitle(f'Outlier Method: {outlier_method_name}', y=1.10, fontweight='bold')
        g.set(xlim=xaxis_limits, ylim=yaxis_limits)
        axes = g.axes.flatten()
        axes[0].set_title(f"Outliers\n{len(data[data['anomaly']== -1])} points")
        axes[1].set_title(f"Inliers\n {len(data[data['anomaly']==  1])} points")
        return g
    return (outlier_plot,)


@app.cell
def _(df_1, outlier_plot):
    outlier_plot(df_1, 'Isolation Forest', 'NPHI', 'RHOB', [0, 0.8], [3, 1.5])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Building an Isolation Forest Model Using Multiple Features
        """
    )
    return


@app.cell
def _():
    anomaly_inputs_1 = ['NPHI', 'RHOB', 'GR', 'CALI', 'PEF', 'DTC']
    return (anomaly_inputs_1,)


@app.cell
def _(IsolationForest, df_1):
    anomaly_inputs_2 = ['NPHI', 'RHOB', 'GR', 'CALI', 'PEF', 'DTC']
    model_IF_1 = IsolationForest(contamination=0.1, random_state=42)
    model_IF_1.fit(df_1[anomaly_inputs_2])
    df_1['anomaly_scores'] = model_IF_1.decision_function(df_1[anomaly_inputs_2])
    df_1['anomaly'] = model_IF_1.predict(df_1[anomaly_inputs_2])
    return anomaly_inputs_2, model_IF_1


@app.cell
def _(df_1, outlier_plot):
    outlier_plot(df_1, 'Isolation Forest', 'NPHI', 'RHOB', [0, 0.8], [3, 1.5])
    return


@app.cell
def _(anomaly_inputs_2, df_1, sns):
    palette = ['#ff7f0e', '#1f77b4']
    sns.pairplot(df_1, vars=anomaly_inputs_2, hue='anomaly', palette=palette)
    return (palette,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
