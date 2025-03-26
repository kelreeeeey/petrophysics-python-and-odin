import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 5. Petrophysical Calculations
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Created By: Andy McDonald

        The following tutorial illustrates how to calculate key petrophysical properties using pandas
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Shale Volume Function
        """
    )
    return


@app.cell
def shale_volume():
    def shale_volume(gamma_ray, gamma_ray_max, gamma_ray_min):
        vshale = (gamma_ray - gamma_ray_min) / (gamma_ray_max - gamma_ray_min)
        return round(vshale, 4)
    return (shale_volume,)


@app.cell
def _(shale_volume):
    shale_volume(120, 200, 15)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Density Porosity Function
        """
    )
    return


@app.cell
def density_porosity():
    def density_porosity(input_density, matrix_density, fluid_density):
        denpor = (matrix_density - input_density) / (matrix_density - fluid_density)
        return round(denpor, 4)
    return (density_porosity,)


@app.cell
def _(density_porosity):
    density_porosity(2.45, 2.65, 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Water Saturation Functions
        """
    )
    return


@app.cell
def sw_archie():
    def sw_archie(porosity, rt, rw, archieA, archieM, archieN):
        sw = ((archieA / (porosity ** archieM)) * (rw/rt))**(1/archieN)
        return sw
    return (sw_archie,)


@app.cell
def _(sw_archie):
    sw_archie(0.1, 10, 0.1, 1, 2, 2)
    return


@app.cell
def sw_simandoux():
    # equations from https://www.spec2000.net/01-quickmath.htm
    def sw_simandoux(phie, rt, rw, archieA, archieM, archieN, vshale, rshale):
        A = (1 - vshale) * archieA * rw / (phie ** archieM)
        B = A * vshale / (2 * rshale)
        C = A / rt
    
        sw = ((B **2 + C)**0.5 - B) **(2 / archieN)
        return sw
    return (sw_simandoux,)


@app.cell
def _(sw_simandoux):
    sw_simandoux(0.1, 10, 0.1, 1, 2, 2, 0.3, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Loading Well Data From CSV
        """
    )
    return


@app.cell
def _(pd):
    well = pd.read_csv("Data/15_9-19.csv", header=0, skiprows=[1])
    return (well,)


@app.cell
def _(well):
    well.head()
    return


@app.cell
def _(np, well):
    well.replace(-999.00, np.nan, inplace=True)
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell
def _(plt, well):
    well['GR'].plot(kind='hist', bins=230)
    plt.xlim(0, 250)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Calculate Petrophysical Properties

        Using the functions created above, we can pass through the required columns in order to calculate the key petrophysical properties
        """
    )
    return


@app.cell
def _(shale_volume, well):
    #Calculate Shale Volume
    well['VSHALE'] = shale_volume(well['GR'], well['GR'].quantile(q=0.99),
                                 well['GR'].quantile(q=0.01))
    return


@app.cell
def _(density_porosity, well):
    #Calculate density porosity
    well['PHI'] = density_porosity(well['RHOB'], 2.65, 1)
    return


@app.cell
def _(well):
    #Calculate PHIE
    well['PHIECALC'] = well['PHI'] - (well['VSHALE'] * 0.3)
    return


@app.cell
def _(well):
    well.head(10)
    return


@app.cell
def _(sw_archie, well):
    #Calculate Archie SW
    well['SW'] = sw_archie(well['PHI'], well['RT'], well['RW'], 1, 2, 2)
    return


@app.cell
def _(sw_simandoux, well):
    #Calculate Simandoux SW
    well['SW_SIM'] = sw_simandoux(well['PHIECALC'], well['RT'], well['RW'], 1, 2, 2, well['VSHALE'],2)
    return


@app.cell
def _(well):
    #Limit SW to 1
    well['SW_LIM'] = well['SW'].mask(well['SW']>1, 1)
    well['SW__SIM_LIM'] = well['SW_SIM'].mask(well['SW_SIM']>1, 1)
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Creating a Log Plot to Display the Results
        """
    )
    return


@app.cell
def _(plt, well):
    fig, ax = plt.subplots(figsize=(15,10))

    #Set up the plot axes
    ax1 = plt.subplot2grid((1,7), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,7), (0,1), rowspan=1, colspan = 1)
    ax3 = plt.subplot2grid((1,7), (0,2), rowspan=1, colspan = 1)
    ax4 = plt.subplot2grid((1,7), (0,3), rowspan=1, colspan = 1)
    ax5 = ax3.twiny() #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,7), (0,4), rowspan=1, colspan = 1)
    ax7 = ax6.twiny()
    ax8 = plt.subplot2grid((1,7), (0,5), rowspan=1, colspan = 1)
    ax9 = plt.subplot2grid((1,7), (0,6), rowspan=1, colspan = 1)

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)

    # Gamma Ray track
    ax1.plot("GR", "DEPTH", data = well, color = "green")
    ax1.set_xlabel("Gamma")
    ax1.xaxis.label.set_color("green")
    ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    ax1.set_xticks([0, 50, 100, 150, 200])

    # Resistivity track
    ax2.plot("RT", "DEPTH", data = well, color = "red")
    ax2.set_xlabel("Resistivity")
    ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    ax2.set_xticks([0.1, 1, 10, 100, 1000])
    ax2.semilogx()

    # Density track
    ax3.plot("RHOB", "DEPTH", data = well, color = "red")
    ax3.set_xlabel("Density")
    ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    ax3.set_xticks([1.95, 2.45, 2.95])

    # Sonic track
    ax4.plot("DT", "DEPTH", data = well, color = "purple")
    ax4.set_xlabel("Sonic")
    ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")

    # Neutron track placed ontop of density track
    ax5.plot("NPHI", "DEPTH", data = well, color = "blue")
    ax5.set_xlabel('Neutron')
    ax5.xaxis.label.set_color("blue")
    ax5.set_xlim(0.45, -0.15)
    ax5.set_ylim(4150, 3500)
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.08))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")
    ax5.set_xticks([0.45,  0.15, -0.15])

    # Porosity track
    ax6.plot("PHI", "DEPTH", data = well, color = "black")
    ax6.set_xlabel("Total PHI")
    ax6.set_xlim(0.5, 0)
    ax6.xaxis.label.set_color("black")
    ax6.tick_params(axis='x', colors="black")
    ax6.spines["top"].set_edgecolor("black")
    ax6.set_xticks([0, 0.25, 0.5])

    # Porosity track
    ax7.plot("PHIECALC", "DEPTH", data = well, color = "blue")
    ax7.set_xlabel("Effective PHI")
    ax7.set_xlim(0.5, 0)
    ax7.xaxis.label.set_color("blue")
    ax7.tick_params(axis='x', colors="blue")
    ax7.spines["top"].set_position(("axes", 1.08))
    ax7.spines["top"].set_visible(True)
    ax7.spines["top"].set_edgecolor("blue")
    ax7.set_xticks([0, 0.25, 0.5])

    # Sw track
    ax8.plot("SW_LIM", "DEPTH", data = well, color = "black")
    ax8.set_xlabel("SW - Archie")
    ax8.set_xlim(0, 1)
    ax8.xaxis.label.set_color("black")
    ax8.tick_params(axis='x', colors="black")
    ax8.spines["top"].set_edgecolor("black")
    ax8.set_xticks([0, 0.5, 1])

    # Sw track
    ax9.plot("SW_SIM", "DEPTH", data = well, color = "blue")
    ax9.set_xlabel("SW - Simandoux")
    ax9.set_xlim(0, 1)
    ax9.xaxis.label.set_color("blue")
    ax9.tick_params(axis='x', colors="blue")
    ax9.spines["top"].set_edgecolor("blue")
    ax9.set_xticks([0, 0.5, 1])

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax8, ax9]:
        ax.set_ylim(4150, 3500)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
    
    
    plt.tight_layout()
    return (
        ax,
        ax1,
        ax10,
        ax11,
        ax12,
        ax2,
        ax3,
        ax4,
        ax5,
        ax6,
        ax7,
        ax8,
        ax9,
        fig,
    )


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
