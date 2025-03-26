import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _(med_combining_log_and_formation_data_1):
    med_combining_log_and_formation_data_1.py
    return


@app.cell
def _():
    import lasio as las
    import os
    import pandas as pd
    import csv
    return csv, las, os, pd


@app.cell
def _(las, os, pd):
    directory = 'Data/Notebook 36'
    df_list = []
    for _file in os.listdir(directory):
        if _file.endswith('.las'):
            _f = os.path.join(directory, _file)
            las_file = las.read(_f)
            _df = las_file.df()
            well_name = las_file.well.WELL.value
            _df['WELL'] = well_name
            _df = _df.reset_index()
            _df = _df.sort_values(['WELL', 'DEPT']).reset_index(drop=True)
            df_list.append(_df)
    well_df = pd.concat(df_list)
    return df_list, directory, las_file, well_df, well_name


@app.cell
def _(well_df):
    well_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading Formation Data
        """
    )
    return


@app.cell
def _(directory, os, pd):
    df_formation_list = []
    for _file in os.listdir(directory):
        if _file.endswith('.csv'):
            _f = os.path.join(directory, _file)
            _df = pd.read_csv(_f)
            df_formation_list.append(_df)
    formations_df = pd.concat(df_formation_list)
    return df_formation_list, formations_df


@app.cell
def _(formations_df):
    formations_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Converting the dataframe to a dictionary
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        https://datascience.stackexchange.com/questions/67578/export-pandas-dataframe-to-a-nested-dictionary-from-multiple-columns
        """
    )
    return


@app.cell
def _(formations_df):
    formations_dict = {k: _f.groupby('Top')['Stratigraphical Unit'].apply(list).to_dict() for (k, _f) in formations_df.groupby('Well')}
    return (formations_dict,)


@app.cell
def _(formations_dict):
    formations_dict
    return


@app.cell
def _(formations_dict):
    formations_dict['L07-01']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Merging the Formations and Well Data
        """
    )
    return


@app.cell
def _(formations_dict):
    def add_formation_name_to_df(depth, well_name):

        formations_depth = formations_dict[well_name].keys()   
    
        # Need to catch if we are at the last formation
        try:
            at_last_formation = False
            below = min([i for i in formations_depth if depth < i])
        except ValueError:
            at_last_formation = True

        # Need to catch if we are above the first listed formation
        try:
            above_first_formation = False
            above = max([i for i in formations_depth if depth > i])
        except:
            above_first_formation = True

        if above_first_formation:
            formation = ''

        # Check if the current depth matches an existing formation depth
        nearest_depth = min(formations_depth, key=lambda x:abs(x-depth))
        if depth == nearest_depth:
            formation = formations_dict[well_name][nearest_depth][0]

        else:
            if not at_last_formation:
                if depth >= above and depth <below:
                    formation = formations_dict[well_name][above][0]
            else:
                    formation = formations_dict[well_name][above][0]
        return formation
    return (add_formation_name_to_df,)


@app.cell
def _(formations_dict, well_name):
    depth = 930
    formations_depth = formations_dict[well_name].keys()   
    print(formations_depth)

    #https://stackoverflow.com/questions/36275459/find-the-closest-elements-above-and-below-a-given-number



    # Need to catch if we are at the last formation
    try:
        at_last_formation = False
        below = min([i for i in formations_depth if depth < i])
    except ValueError:
        at_last_formation = True

    # Need to catch if we are above the first listed formation
    try:
        above_first_formation = False
        above = max([i for i in formations_depth if depth > i])
    except:
        above_first_formation = True

    if above_first_formation:
        print('')
    
    # Check if the current depth matches an existing formation depth
    nearest_depth = min(formations_depth, key=lambda x:abs(x-depth))
    if depth == nearest_depth:
        print(f'Current Depth: {depth} is equal to {nearest_depth}')
        print(formations_dict[well_name][nearest_depth][0])

    else:
        if not at_last_formation:
            if depth >= above and depth <below:
                print(f'Current Depth: {depth} is between {above} and {below}')
                print(formations_dict[well_name][above][0])
        else:
                print(f'Current Depth: {depth} is deeper than {above}')
                print(formations_dict[well_name][above][0])
    return (
        above,
        above_first_formation,
        at_last_formation,
        below,
        depth,
        formations_depth,
        nearest_depth,
    )


@app.cell
def _(add_formation_name_to_df, well_df):
    well_df['FORMATION'] = well_df.apply(lambda x: add_formation_name_to_df(x['DEPT'], x['WELL']), axis=1)
    return


@app.cell
def _(well_df):
    well_df
    return


@app.cell
def _(well_df):
    well_df.loc[(well_df['WELL'] == 'L07-01') & (well_df['DEPT'] >= 929) & (well_df['DEPT'] <= 935)]
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
