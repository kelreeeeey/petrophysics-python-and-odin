import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Creating Geospatial Heatmaps with Folium and Plotly Express
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('xeek_force_2020_dtc_mapping.csv').drop(['Unnamed: 0'],axis=1)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotly Express
        """
    )
    return


@app.cell
def _():
    import plotly_express as px
    return (px,)


@app.cell
def _(df, px):
    fig = px.density_mapbox(df,
                            lat='Latitude', lon='Longitude',
                            z='DTC', radius=70,
                            center=dict(lat=df.Latitude.mean(), 
                                        lon=df.Longitude.mean()), 
                            zoom=4,
                            mapbox_style="open-street-map", 
                            height=900)
    return (fig,)


@app.cell
def _(fig):
    fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Folium
        """
    )
    return


@app.cell
def _():
    import folium
    from folium.plugins import HeatMap
    return HeatMap, folium


@app.cell
def _(df, folium):
    m = folium.Map(location=[df.Latitude.mean(), 
                             df.Longitude.mean()], 
                   zoom_start=6, control_scale=True)
    return (m,)


@app.cell
def _(m):
    m
    return


@app.cell
def _(HeatMap, df, m):
    map_values1 = df[['Latitude','Longitude','DTC']]

    data = map_values1.values.tolist()

    hm = HeatMap(data, 
                    min_opacity=0.05, 
                    max_opacity=0.9, 
                    radius=25).add_to(m)
    return data, hm, map_values1


@app.cell
def _(m):
    m
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
