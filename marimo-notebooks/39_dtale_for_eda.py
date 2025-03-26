import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    #!pip install dtale
    return


@app.cell
def _():
    import pandas as pd
    import dtale
    return dtale, pd


@app.cell
def _(pd):
    df = pd.read_csv('Data/Xeek_Well_15-9-15.csv')
    return (df,)


@app.cell
def _(df, dtale):
    dtale.show(df)
    return


if __name__ == "__main__":
    app.run()
