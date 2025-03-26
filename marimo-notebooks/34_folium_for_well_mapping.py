import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    import folium
    import pandas as pd
    return folium, pd


@app.cell
def _(pd):
    df = pd.read_csv('Data/NPD/wellboreExplorationAll.csv', usecols=['wlbWellboreName', 'wlbNsDecDeg', 'wlbEwDesDeg', 'wlbPurposePlanned', 'wlbCompletionYear'])
    return (df,)


@app.cell
def _(df):
    df.columns = ['Well Name', 'Purpose', 'Completion Year', 'Latitude', 'Longitude']
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.Purpose.unique()
    return


@app.cell
def _(df, folium):
    map = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], zoom_start=6, control_scale=True)
    return (map,)


@app.cell
def _(map):
    map
    return


@app.cell
def _(df, folium, map):
    #Add a single marker

    folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()]).add_to(map)
    return


@app.cell
def _(map):
    map
    return


@app.cell
def _(df, folium):
    map_1 = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], zoom_start=6, control_scale=True)
    folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()], icon=folium.Icon(color='red', icon='')).add_to(map_1)
    map_1
    return (map_1,)


@app.cell
def _(df, folium):
    map_2 = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], zoom_start=6, control_scale=True)
    folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()], icon=folium.Icon(color='red', icon='pushpin')).add_to(map_2)
    map_2
    return (map_2,)


@app.cell
def _(df, folium):
    map_3 = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], zoom_start=3, control_scale=True)
    for (_i, _row) in df.iterrows():
        _iframe = folium.IFrame('Well Name:' + str(_row['Well Name']))
        _popup = folium.Popup(_iframe, min_width=300, max_width=300)
        folium.Marker(location=[_row['Latitude'], _row['Longitude']], popup=_popup, c=_row['Purpose']).add_to(map_3)
    return (map_3,)


@app.cell
def _(map_3):
    map_3
    return


@app.cell
def _():
    purpose_colour = {'WILDCAT':'red', 'APPRAISAL':'green', 'WILDCAT-CCS':'blue'}
    return (purpose_colour,)


@app.cell
def _(purpose_colour):
    purpose_colour['WILDCAT']
    return


@app.cell
def _(df, folium, purpose_colour):
    map_4 = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], zoom_start=3, control_scale=True)
    for (_i, _row) in df.iterrows():
        _iframe = folium.IFrame(f"Well Name: {str(_row['Well Name'])} \n Purpose: {str(_row['Purpose'])}")
        _popup = folium.Popup(_iframe, min_width=300, max_width=300)
        try:
            icon_color = purpose_colour[_row['Purpose']]
        except:
            icon_color = 'gray'
        folium.Marker(location=[_row['Latitude'], _row['Longitude']], popup=_popup, c=_row['Purpose'], icon=folium.Icon(color=icon_color, icon='')).add_to(map_4)
    return icon_color, map_4


@app.cell
def _(map_4):
    map_4
    return


if __name__ == "__main__":
    app.run()
