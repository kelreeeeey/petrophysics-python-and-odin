import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    from pywaffle import Waffle
    import pandas as pd
    import matplotlib.pyplot as plt
    return Waffle, pd, plt


@app.cell
def _(pd):
    lith_dict = {'LITH': ['Shale', 'Sandstone', 
                          'Sandstone/Shale', 'Chalk', 
                          'Limestone', 'Marl', 'Tuff'],
                 'Well1': [61,15, 10, 5, 
                                5, 3, 1],
                 'Well2': [35 ,21, 16, 12, 
                                7, 5, 4]}

    lith_data_df = pd.DataFrame.from_dict(lith_dict)
    return lith_data_df, lith_dict


@app.cell
def _(lith_data_df):
    lith_data_df
    return


@app.cell
def _():
    colours = ['#8dd3c7', '#deb887', '#bebada', '#fb8072', 
               '#80b1d3', '#fdb462', '#b3de69']
    return (colours,)


@app.cell
def _(Waffle, colours, lith_data_df, plt):
    _plot_labels = [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well1)]
    plt.figure(FigureClass=Waffle, figsize=(10, 10), rows=5, columns=20, values=list(lith_data_df['Well1']), colors=colours, labels=_plot_labels, icons='circle', font_size='20', legend={'loc': 'lower center', 'bbox_to_anchor': (0.5, -0.8), 'ncol': 3, 'fontsize': 12}, starting_location='NW')
    plt.show()
    return


@app.cell
def _(Waffle, colours, lith_data_df, plt):
    _plot_labels = [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well2)]
    _fig = plt.figure(FigureClass=Waffle, figsize=(10, 10), rows=5, columns=20, values=list(lith_data_df['Well2']), colors=colours, labels=_plot_labels, legend={'loc': 'lower center', 'bbox_to_anchor': (0.5, -0.8), 'ncol': 3, 'fontsize': 12}, rounding_rule='ceil')
    plt.show()
    return


@app.cell
def _(Waffle, colours, lith_data_df, plt):
    _plot_labels = [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well2)]
    _fig = plt.figure(FigureClass=Waffle, figsize=(10, 10), rows=5, columns=20, values=list(lith_data_df['Well2']), colors=colours, labels=_plot_labels, legend={'loc': 'center left', 'bbox_to_anchor': (1.0, 0.5), 'ncol': 1, 'fontsize': 10}, rounding_rule='ceil')
    plt.show()
    return


@app.cell
def _(Waffle, colours, lith_data_df, plt):
    _plot_labels = [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well1)]
    _fig = plt.figure(FigureClass=Waffle, plots={211: {'values': list(lith_data_df['Well1']), 'labels': [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well1)], 'legend': {'loc': 'center left', 'bbox_to_anchor': (1.0, 0.5), 'ncol': 1, 'fontsize': 12}, 'title': {'label': 'Well 1 Lithology Composition', 'fontsize': 18}}, 212: {'values': list(lith_data_df['Well2']), 'labels': [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df.LITH, lith_data_df.Well2)], 'legend': {'loc': 'center left', 'bbox_to_anchor': (1.0, 0.5), 'ncol': 1, 'fontsize': 12}, 'title': {'label': 'Well 2 Lithology Composition', 'fontsize': 18}}}, figsize=(15, 10), rows=5, columns=20, colors=colours)
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(Waffle, colours, lith_data_df, plt):
    off_colour = 'lightgrey'
    (_fig, axs) = plt.subplots(len(lith_data_df), 1, figsize=(10, 15))
    for ((i, ax), color) in zip(enumerate(axs.flatten()), colours):
        plot_colours = [color, off_colour]
        perc = lith_data_df.iloc[i]['Well1']
        values = [perc, 100 - perc]
        lith = lith_data_df.iloc[i]['LITH']
        Waffle.make_waffle(ax=ax, rows=5, columns=20, values=values, colors=plot_colours)
        ax.set_title(lith)
    plt.tight_layout()
    plt.show()
    return ax, axs, color, i, lith, off_colour, perc, plot_colours, values


@app.cell
def _(Waffle, data, plt):
    _fig = plt.figure(FigureClass=Waffle, plots={311: {'values': data['Factory A'] / 1000, 'labels': [f'{k} ({v})' for (k, v) in data['Factory A'].items()], 'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 8}, 'title': {'label': 'Vehicle Production of Factory A', 'loc': 'left', 'fontsize': 12}}, 312: {'values': data['Factory B'] / 1000, 'labels': [f'{k} ({v})' for (k, v) in data['Factory B'].items()], 'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.2, 1), 'fontsize': 8}, 'title': {'label': 'Vehicle Production of Factory B', 'loc': 'left', 'fontsize': 12}}, 313: {'values': data['Factory C'] / 1000, 'labels': [f'{k} ({v})' for (k, v) in data['Factory C'].items()], 'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.3, 1), 'fontsize': 8}, 'title': {'label': 'Vehicle Production of Factory C', 'loc': 'left', 'fontsize': 12}}}, rows=5, cmap_name='Accent', rounding_rule='ceil', figsize=(5, 5))
    _fig.suptitle('Vehicle Production by Vehicle Type', fontsize=14, fontweight='bold')
    _fig.supxlabel('1 block = 1000 vehicles', fontsize=8, ha='right')
    return


if __name__ == "__main__":
    app.run()
