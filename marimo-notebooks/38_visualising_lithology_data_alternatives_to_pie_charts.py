import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    return np, pd, plt


@app.cell
def _(pd):
    df = pd.read_csv('Data/Xeek_Well_15-9-15.csv')

    lith_percentage = round(df['LITH'].value_counts()/len(df) *100, 2)
    lith_data_df = lith_percentage.to_frame().reset_index()
    lith_data_df.columns = ['LITH', 'PERCENTAGE']

    lith_data_df

    lith_data_df.to_dict()
    return df, lith_data_df, lith_percentage


@app.cell
def _(pd):
    lith_dict = {'LITH': ['Shale', 'Sandstone', 'Sandstone/Shale', 'Chalk', 'Limestone', 'Marl', 'Tuff'], 'PERCENTAGE': [61.36, 15.36, 9.76, 5.47, 5.11, 2.17, 0.77]}
    lith_data_df_1 = pd.DataFrame.from_dict(lith_dict)
    return lith_data_df_1, lith_dict


@app.cell
def _(lith_data_df_1):
    lith_data_df_1
    return


@app.cell
def _(lith_data_df_1):
    lith_data_df_1['PERCENTAGE'].sum()
    return


@app.cell
def _():
    lith = ['Shale', 'Sandstone', 'Sandstone/Shale', 
            'Chalk', 'Limestone', 'Marl', 'Tuff']

    percentage = [61.36, 15.36, 9.76, 5.47, 5.11, 2.17, 0.76]

    colours = ['#8dd3c7', '#deb887', '#fb8072', 
               '#bebada', '#80b1d3', '#fdb462', '#b3de69']
    return colours, lith, percentage


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Pie Chart
        """
    )
    return


@app.cell
def _():
    colours_1 = ['#8dd3c7', '#deb887', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    return (colours_1,)


@app.cell
def _(colours_1, lith_data_df_1, plt):
    lith_labels = lith_data_df_1['LITH'].unique()
    plt.figure(figsize=(10, 10))
    plt.pie(lith_data_df_1['PERCENTAGE'], labels=lith_labels, colors=colours_1, startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'grey'})
    plt.show()
    return (lith_labels,)


@app.cell
def _(colours_1, lith_data_df_1, lith_labels, plt):
    import math
    plt.figure(figsize=(10, 10))
    pie_chart = plt.pie(lith_data_df_1['PERCENTAGE'], labels=lith_labels, colors=colours_1, startangle=90, autopct='%0.1f%%', wedgeprops={'linewidth': 1, 'edgecolor': 'grey'}, pctdistance=0.5)
    plt.show()
    return math, pie_chart


@app.cell
def _(colours_1, lith_data_df_1, lith_labels, math, plt):
    plt.figure(figsize=(10, 10))
    pie_chart_1 = plt.pie(lith_data_df_1['PERCENTAGE'], colors=colours_1, startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'grey'})
    for (label, pie_slice) in zip(lith_labels, pie_chart_1[1]):
        (x, y) = pie_slice.get_position()
        angle = int(math.degrees(math.atan2(y, x)))
        horiz_align = 'left'
        if x < 0:
            angle = angle - 180
            horiz_align = 'left'
        plt.annotate(label, xy=(x, y), rotation=angle, ha=horiz_align, va='center', rotation_mode='anchor', size=8)
    plt.show()
    return angle, horiz_align, label, pie_chart_1, pie_slice, x, y


@app.cell
def _(colours_1, lith_data_df_1, lith_labels, plt):
    plt.figure(figsize=(10, 10))
    plt.pie(lith_data_df_1['PERCENTAGE'], colors=colours_1, startangle=90, autopct='%0.1f%%', wedgeprops={'linewidth': 1, 'edgecolor': 'grey'}, pctdistance=1.1)
    plt.legend(lith_labels, frameon=False)
    plt.show()
    return


@app.cell
def _(colours_1, lith_data_df_1, plt):
    plot_labels = [f'{i} \n({str(j)} %)' for (i, j) in zip(lith_data_df_1.LITH, lith_data_df_1.PERCENTAGE)]
    plt.figure(figsize=(10, 10))
    plt.pie(lith_data_df_1['PERCENTAGE'], labels=plot_labels, colors=colours_1, startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'}, labeldistance=1.15)
    centre_circle = plt.Circle((0, 0), 0.7, fc='white', ec='grey')
    outer_circle = plt.Circle((0, 0), 1.0, fc='None', ec='grey')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    fig.gca().add_artist(outer_circle)
    plt.show()
    return centre_circle, fig, outer_circle, plot_labels


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Bar Chart
        """
    )
    return


@app.cell
def _(lith_data_df_1, plt):
    colours_2 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    plt.figure(figsize=(10, 10))
    plt.bar(x=lith_data_df_1['LITH'], height=lith_data_df_1['PERCENTAGE'], color=colours_2)
    plt.xlabel('Percentage', fontsize='15', fontweight='bold', labelpad=30)
    plt.ylabel('Country', fontsize='15', fontweight='bold', labelpad=30)
    plt.show()
    return (colours_2,)


@app.cell
def _(colours_2, lith_data_df_1, plt):
    lith_data_df_1[['PERCENTAGE']].T.plot.barh(stacked=True, legend=True, figsize=(15, 2), color=colours_2, edgecolor='grey')
    plt.axis('off')
    plt.legend(lith_data_df_1['LITH'].unique(), loc='lower center', ncol=7, bbox_to_anchor=(0.5, -0.2), frameon=False)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Treemap
        """
    )
    return


@app.cell
def _(colours_2, lith_data_df_1, plt):
    import squarify
    plot_labels_1 = [f'{i} \n({str(j)} %)' for (i, j) in zip(lith_data_df_1.LITH, lith_data_df_1.PERCENTAGE)]
    plt.figure(figsize=(10, 10))
    squarify.plot(sizes=lith_data_df_1['PERCENTAGE'], label=plot_labels_1, color=colours_2, edgecolor='grey')
    plt.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    plt.show()
    return plot_labels_1, squarify


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Waffle Chart
        """
    )
    return


app._unparsable_cell(
    r"""
    !pip install pywaffle
    """,
    name="_"
)


@app.cell
def _(lith_data_df_1, plt):
    from pywaffle import Waffle
    plot_labels_2 = [f'{i} ({str(j)} %)' for (i, j) in zip(lith_data_df_1.LITH, lith_data_df_1.PERCENTAGE)]
    colours_3 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    fig_1 = plt.figure(FigureClass=Waffle, figsize=(10, 10), rows=5, columns=20, values=list(lith_data_df_1['PERCENTAGE']), colors=colours_3, labels=plot_labels_2, legend={'loc': 'lower center', 'bbox_to_anchor': (0.5, -0.8), 'ncol': 3, 'fontsize': 12})
    plt.show()
    return Waffle, colours_3, fig_1, plot_labels_2


@app.cell
def _(Waffle, lith_data_df_1, plt):
    colours_4 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    off_colour = 'lightgrey'
    (fig_2, axs) = plt.subplots(len(lith_data_df_1), 1, figsize=(10, 15))
    for ((i, ax), color) in zip(enumerate(axs.flatten()), colours_4):
        plot_colours = [color, off_colour]
        perc = lith_data_df_1.iloc[i]['PERCENTAGE']
        values = [perc, 100 - perc]
        lith_1 = lith_data_df_1.iloc[i]['LITH']
        Waffle.make_waffle(ax=ax, rows=5, columns=20, values=values, colors=plot_colours)
        ax.set_title(lith_1)
    plt.tight_layout()
    plt.show()
    return (
        ax,
        axs,
        color,
        colours_4,
        fig_2,
        i,
        lith_1,
        off_colour,
        perc,
        plot_colours,
        values,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Circle Packing Chart
        """
    )
    return


app._unparsable_cell(
    r"""
    !pip install circlify
    """,
    name="_"
)


@app.cell
def _(pd, plt):
    import circlify
    lith_data_df_2 = pd.DataFrame({'LITH': {0: 'Shale', 1: 'Sandstone', 2: 'Sandstone/Shale', 3: 'Chalk', 4: 'Limestone', 5: 'Marl', 6: 'Tuff'}, 'PERCENTAGE': {0: 61.36, 1: 15.36, 2: 9.76, 3: 5.47, 4: 5.11, 5: 2.17, 6: 0.76}})
    colours_5 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    plot_labels_3 = [f'{i} \n({str(j)} %)' for (i, j) in zip(lith_data_df_2.LITH, lith_data_df_2.PERCENTAGE)]
    circle_plot = circlify.circlify(lith_data_df_2['PERCENTAGE'].tolist(), target_enclosure=circlify.Circle(x=0, y=0))
    circle_plot.reverse()
    (fig_3, axs_1) = plt.subplots(figsize=(15, 15))
    lim = max((max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circle_plot))
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    for (circle, colour, label_1) in zip(circle_plot, colours_5, plot_labels_3):
        (x_1, y_1, r) = circle
        axs_1.add_patch(plt.Circle((x_1, y_1), r, linewidth=1, facecolor=colour, edgecolor='grey'))
        plt.annotate(label_1, (x_1, y_1), va='center', ha='center', fontweight='bold')
    plt.axis('off')
    plt.show()
    return (
        axs_1,
        circle,
        circle_plot,
        circlify,
        colour,
        colours_5,
        fig_3,
        label_1,
        lim,
        lith_data_df_2,
        plot_labels_3,
        r,
        x_1,
        y_1,
    )


@app.cell
def _(circle_plot):
    circle_plot.reverse()
    return


@app.cell
def _(circle_plot):
    circle_plot
    return


@app.cell
def _(lith_data_df_2, plt):
    plt.figure(figsize=(10, 5))
    plt.stem(lith_data_df_2['PERCENTAGE'])
    plt.grid(color='lightgrey', alpha=0.5)
    plt.xticks(ticks=range(0, len(lith_data_df_2)), labels=lith_data_df_2['LITH'])
    plt.xlabel('Lithology', fontsize=14, fontweight='bold')
    plt.ylim(0, 100)
    plt.ylabel('Percentage', fontsize=14, fontweight='bold')
    plt.show()
    return


@app.cell
def _(colours_5, lith_data_df_2, plt):
    plt.figure(figsize=(10, 5))
    plt.scatter(lith_data_df_2['LITH'], lith_data_df_2['PERCENTAGE'], c=colours_5, s=100, edgecolors='grey', zorder=3)
    plt.vlines(lith_data_df_2['LITH'], ymin=0, ymax=lith_data_df_2['PERCENTAGE'], colors=colours_5, linewidth=4, zorder=2)
    plt.ylim(0, 100)
    plt.ylabel('Percentage', fontsize=14, fontweight='bold')
    plt.xlabel('Lithology', fontsize=14, fontweight='bold')
    plt.grid(color='lightgrey', alpha=0.5, zorder=1)
    plt.show()
    return


@app.cell
def _(np, pd, plt):
    lith_data_df_3 = pd.DataFrame({'LITH': {0: 'Shale', 1: 'Sandstone', 2: 'Sandstone/Shale', 3: 'Chalk', 4: 'Limestone', 5: 'Marl', 6: 'Tuff'}, 'PERCENTAGE': {0: 61.36, 1: 15.36, 2: 9.76, 3: 5.47, 4: 5.11, 5: 2.17, 6: 0.76}})
    lithologies = list(lith_data_df_3['LITH'])
    percentages = list(lith_data_df_3['PERCENTAGE'])
    lithologies = [*lithologies, lithologies[0]]
    percentages = [*percentages, percentages[0]]
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(lithologies))
    plt.figure(figsize=(10, 10))
    plt.subplot(polar=True)
    plt.plot(label_loc, percentages, lw=4)
    (lines, labels) = plt.thetagrids(np.degrees(label_loc), labels=lithologies)
    plt.plot()
    plt.show()
    return label_loc, labels, lines, lith_data_df_3, lithologies, percentages


@app.cell
def _(lith_data_df_3):
    import plotly.express as px
    fig_4 = px.line_polar(lith_data_df_3, r='PERCENTAGE', theta='LITH', line_close=True, width=800, height=800)
    fig_4.update_traces(fill='toself', line=dict(color='red'))
    fig_4.show()
    return fig_4, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Radial Bar Chart
        """
    )
    return


@app.cell
def _(np, pd, plt):
    lith_data_df_4 = pd.DataFrame({'LITH': {0: 'Shale', 1: 'Sandstone', 2: 'Sandstone/Shale', 3: 'Chalk', 4: 'Limestone', 5: 'Marl', 6: 'Tuff'}, 'PERCENTAGE': {0: 61.36, 1: 15.36, 2: 9.76, 3: 5.47, 4: 5.11, 5: 2.17, 6: 0.76}})
    colours_6 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    labels_1 = lith_data_df_4['LITH'].unique()
    (fig_5, ax_1) = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))
    angles = np.linspace(0, 2 * np.pi, len(lith_data_df_4), endpoint=False)
    upper_limit = 100
    lower_limit = 0
    max_value = lith_data_df_4['PERCENTAGE'].max()
    indexes = list(range(0, len(lith_data_df_4)))
    angles = [element * width for element in indexes]
    width = 2 * np.pi / len(lith_data_df_4)
    bars = ax_1.bar(x=angles, height=lith_data_df_4['PERCENTAGE'], width=width, color=colours_6, edgecolor='black', zorder=2, alpha=0.8)
    plt.grid(zorder=0)
    plt.tick_params(axis='x', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    plt.ylim(0, 70)
    ax_1.legend(bars, labels_1, loc='center right', bbox_to_anchor=(1.3, 0.5))
    plt.show()
    return (
        angles,
        ax_1,
        bars,
        colours_6,
        fig_5,
        indexes,
        labels_1,
        lith_data_df_4,
        lower_limit,
        max_value,
        upper_limit,
        width,
    )


@app.cell
def _(lith_data_df_4, np, plt):
    plt.figure(figsize=(10, 10))
    ax_2 = plt.subplot(111, polar=True)
    upperLimit = 100
    lowerLimit = 0
    max_value_1 = lith_data_df_4['PERCENTAGE'].max()
    slope = (max_value_1 - lowerLimit) / max_value_1
    heights = lith_data_df_4['PERCENTAGE']
    bar_width = 2 * np.pi / len(lith_data_df_4)
    indexes_1 = list(range(1, len(lith_data_df_4.index) + 1))
    angles_1 = [element * bar_width for element in indexes_1]
    bars_1 = ax_2.bar(x=angles_1, height=heights, width=bar_width, bottom=lowerLimit, linewidth=2, edgecolor='white')
    return (
        angles_1,
        ax_2,
        bar_width,
        bars_1,
        heights,
        indexes_1,
        lowerLimit,
        max_value_1,
        slope,
        upperLimit,
    )


@app.cell
def _(colours_6, lith_data_df_4, np, plt):
    iN = len(lith_data_df_4)
    arrCnts = np.array(lith_data_df_4['PERCENTAGE'])
    lObjectsALLlbls = lith_data_df_4['LITH'].unique()
    theta = np.arange(0, 2 * np.pi, 2 * np.pi / iN)
    width_1 = 2 * np.pi / iN * 0.9
    fig_6 = plt.figure(figsize=(8, 8))
    ax_3 = fig_6.add_axes([0.1, 0.1, 0.75, 0.75], polar=True)
    bars_2 = ax_3.bar(theta, arrCnts, width=width_1, bottom=20, color=colours_6, edgecolor='black', zorder=2, alpha=0.8)
    bottom = 50
    rotations = np.rad2deg(theta)
    (y0, y1) = ax_3.get_ylim()
    for (x_2, bar, rotation, label_2) in zip(theta, bars_2, rotations, lObjectsALLlbls):
        offset = (bottom + bar.get_height()) / (y1 - y0)
        h = offset + len(label_2) / 2.0 * 0.032
        lab = ax_3.text(x_2, h, label_2, transform=ax_3.get_xaxis_transform(), ha='center', va='center')
        lab.set_rotation(rotation)
    plt.show()
    return (
        arrCnts,
        ax_3,
        bar,
        bars_2,
        bottom,
        fig_6,
        h,
        iN,
        lObjectsALLlbls,
        lab,
        label_2,
        offset,
        rotation,
        rotations,
        theta,
        width_1,
        x_2,
        y0,
        y1,
    )


@app.cell
def _(np, pd, plt):
    lith_data_df_5 = pd.DataFrame({'LITH': {0: 'Shale', 1: 'Sandstone', 2: 'Sandstone/Shale', 3: 'Chalk', 4: 'Limestone', 5: 'Marl', 6: 'Tuff'}, 'PERCENTAGE': {0: 61.36, 1: 15.36, 2: 9.76, 3: 5.47, 4: 5.11, 5: 2.17, 6: 0.76}})
    colours_7 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    (fig_7, ax_4) = plt.subplots()
    liths = lith_data_df_5['LITH'].values
    percents = lith_data_df_5['PERCENTAGE'].values
    percents = percents / percents.sum() * 100
    cumulative = np.cumsum(percents)
    cumulative = np.insert(cumulative, 0, 0)
    for i_1 in range(len(liths)):
        ax_4.fill_betweenx(y=[0, 100], x1=cumulative[i_1], x2=cumulative[i_1 + 1], color=colours_7[i_1], alpha=0.5)
    ax_4.set_ylim(0, 100)
    ax_4.set_xlim(0, 100)
    ax_4.set_xlabel('Percentage')
    ax_4.legend(liths, loc='upper right')
    plt.show()
    return (
        ax_4,
        colours_7,
        cumulative,
        fig_7,
        i_1,
        lith_data_df_5,
        liths,
        percents,
    )


@app.cell
def _(ax_4, colours_7, lith_data_df_5, np, plt):
    liths_1 = lith_data_df_5['LITH'].values
    percents_1 = lith_data_df_5['PERCENTAGE'].values
    percents_1 = percents_1 / percents_1.sum() * 100
    cumulative_1 = np.cumsum(percents_1)
    cumulative_1 = np.insert(cumulative_1, 0, 0)
    for i_2 in range(len(liths_1)):
        ax_4.fill_betweenx(y=[0, 100], x1=cumulative_1[i_2], x2=cumulative_1[i_2 + 1], color=colours_7[i_2], alpha=0.5)
    ax_4.set_ylim(0, 100)
    ax_4.set_xlim(0, 100)
    ax_4.set_xlabel('Percentage')
    ax_4.legend(liths_1, loc='upper right')
    ax_4.invert_yaxis()
    plt.show()
    return cumulative_1, i_2, liths_1, percents_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Dot Plot
        """
    )
    return


@app.cell
def _(pd, plt):
    lith_data_df_6 = pd.DataFrame({'LITH': {0: 'Shale', 1: 'Sandstone', 2: 'Sandstone/Shale', 3: 'Chalk', 4: 'Limestone', 5: 'Marl', 6: 'Tuff'}, 'PERCENTAGE': {0: 61.36, 1: 15.36, 2: 9.76, 3: 5.47, 4: 5.11, 5: 2.17, 6: 0.76}})
    colours_8 = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    labels_2 = lith_data_df_6['LITH'].unique()
    percentage_values = round(lith_data_df_6['PERCENTAGE'], 0)
    percentage_values = [int(x) for x in percentage_values]
    (fig_8, ax_5) = plt.subplots(figsize=(5, 10))
    for (i_3, (lith_2, percentage_1, colour_1)) in enumerate(zip(labels_2, percentage_values, colours_8)):
        ax_5.plot([i_3] * percentage_1, list(range(percentage_1)), marker='o', color='white', markerfacecolor=colour_1, markersize='8', linestyle='')
    plt.ylim(0, 70)
    return (
        ax_5,
        colour_1,
        colours_8,
        fig_8,
        i_3,
        labels_2,
        lith_2,
        lith_data_df_6,
        percentage_1,
        percentage_values,
    )


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
