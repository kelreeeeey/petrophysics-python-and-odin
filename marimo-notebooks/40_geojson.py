import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Adding Field Outlines from GeoJSON Files to Folium Maps
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import folium
    return folium, pd


@app.cell
def _():
    import geojson
    return (geojson,)


@app.cell
def _():
    field_locations = 'NSTA_Offshore_Fields_WGS84.geojson'
    return (field_locations,)


@app.cell
def _(geojson):
    with open('NSTA_Offshore_Fields_WGS84.geojson') as f:
        gj = geojson.load(f)
    
    gj
    return f, gj


@app.cell
def _(folium):
    m = folium.Map(location=[58, 5], 
                     zoom_start=6, control_scale=True)
    return (m,)


@app.cell
def _(field_locations, folium, m):
    folium.GeoJson(field_locations,
                   tooltip=folium.GeoJsonTooltip(fields=['FIELDNAME'])
                  ).add_to(m)
    return


@app.cell
def _(m):
    m
    return


@app.cell
def field_type_colour():
    def field_type_colour(feature):
        if feature['properties']['FIELDTYPE'] == 'COND':
            return 'orange'
        elif feature['properties']['FIELDTYPE'] == 'OIL':
            return 'green'
        elif feature['properties']['FIELDTYPE'] == 'GAS':
            return 'red'
    return (field_type_colour,)


@app.cell
def _(field_locations, field_type_colour, folium):
    m_1 = folium.Map(location=[58, 5], zoom_start=6, control_scale=True)
    folium.GeoJson(field_locations, name='geojson', tooltip=folium.GeoJsonTooltip(fields=['FIELDNAME']), style_function=lambda feature: {'fillColor': field_type_colour(feature), 'fillOpacity': 0.9, 'weight': 0}).add_to(m_1)
    return (m_1,)


@app.cell
def _(m_1):
    m_1
    return


@app.cell
def _(field_locations, field_type_colour, folium):
    m_2 = folium.Map(location=[58, 5], zoom_start=6, control_scale=True)
    folium.GeoJson(field_locations, name='geojson', tooltip=folium.GeoJsonTooltip(fields=['FIELDNAME', 'PROD_DATE', 'CURR_OPER']), style_function=lambda feature: {'fillColor': field_type_colour(feature), 'fillOpacity': 0.9, 'weight': 0}).add_to(m_2)
    return (m_2,)


@app.cell
def _(m_2):
    m_2
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
