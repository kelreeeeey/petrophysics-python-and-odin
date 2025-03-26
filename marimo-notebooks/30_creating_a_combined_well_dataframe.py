import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    import lasio
    import pandas as pd
    return lasio, pd


@app.cell
def _(lasio):
    df_19SR = lasio.read('Data/15-9-19_SR_COMP.las').df()
    return (df_19SR,)


@app.cell
def _(df_19SR):
    df_19SR.reset_index(inplace=True)
    return


@app.cell
def _(df_19SR):
    df_19SR
    return


@app.cell
def _(pd):
    df_19SR_formations = pd.read_csv('Data/Volve/15_9_19_SR_TOPS_NPD.csv', 
                                     header=None, names=['Formation', 'DEPT'])

    df_19SR_formations['DEPT'] = df_19SR_formations['DEPT'].astype(float)
    return (df_19SR_formations,)


@app.cell
def _(df_19SR_formations):
    df_19SR_formations
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Method 1
        """
    )
    return


@app.cell
def _(df_19SR, df_19SR_formations, pd):
    combined = pd.merge_asof(df_19SR, df_19SR_formations, on='DEPT', tolerance=0.1, direction='nearest')
    return (combined,)


@app.cell
def _(combined):
    combined.loc[(combined['DEPT'] >= 4046) & (combined['DEPT'] <= 4047.5)]
    return


@app.cell
def _(combined):
    combined['Formation'] = combined['Formation'].fillna(method='ffill')
    return


@app.cell
def _(combined):
    combined
    return


@app.cell
def _(combined):
    combined.loc[(combined['DEPT'] >= 4046) & (combined['DEPT'] <= 4047.5)]
    return


@app.cell
def _(combined):
    combined.loc[(combined['DEPT'] >= 4339) & (combined['DEPT'] <= 4341)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Method 2
        """
    )
    return


@app.cell
def _(df_19SR_formations):
    def add_formations_to_df(depth_value:float) -> str:
        formation_depths = df_19SR_formations['DEPT'].to_list()
        formation_names = df_19SR_formations['Formation'].to_list()
    
        for i, depth in enumerate(formation_depths):
            # Check if we are at last formation
            if i == len(formation_depths)-1:
                return formation_names[i]
        
            # Check if we are before first formation
            elif depth_value <= formation_depths[i]:
                return ''
        
            # Check if current depth between current and next formation
            elif depth_value >= formation_depths[i] and depth_value <= formation_depths[i+1]:
                return formation_names[i]
    return (add_formations_to_df,)


@app.cell
def _(add_formations_to_df, df_19SR):
    df_19SR['FORMATION'] = df_19SR['DEPT'].apply(add_formations_to_df)
    return


@app.cell
def _(df_19SR):
    df_19SR
    return


@app.cell
def _(df_19SR):
    df_19SR.loc[(df_19SR['DEPT'] >= 4339) & (df_19SR['DEPT'] <= 4341)]
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
