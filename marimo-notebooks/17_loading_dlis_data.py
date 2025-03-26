import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # 17 - Working with DLIS Files Using DLISIO
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Andy McDonald
        **Link to Article:**

        Click on the button below to run this notebook on binder without needing to download it or install any libraries.  
        Please note that the interactive widgets will not work on Binder or when viewing the notebook on GitHub.  
        **Binder:**

        ## Introduction
        There are a number of different formats that well log and petrophysical data can be stored in. In the earlier articles and notebooks of this series, we have mainly focused on loading data from CSV files ([here](https://github.com/andymcdgeo/Petrophysics-Python-Series/blob/master/01%20-%20Loading%20and%20Displaying%20Well%20Data%20From%20CSV.ipynb)) and LAS files ([here](https://towardsdatascience.com/loading-multiple-well-log-las-files-using-python-39ac35de99dd) and [here](https://andymcdonaldgeo.medium.com/loading-and-displaying-well-log-data-b9568efd1d8)). Even though LAS files are one of the common formats, they have a flat structure with a header section containing meta data about the well and the file followed by a series of columns containing values for each logging curve. As they are flat, they can't easily store array data. It is possible, but they individual elements of the array are split out into individual columns/curves within a LAS file as opposed to a single array. This is where DLIS files come in.

        Within this article, we will cover:
        - the basics of loading a DLIS file
        - exploring the contents and parameters within a DLIS file
        - displaying processed acoustic waveform data

        We will not be covering acoustic waveform processing. Just the display of previously processed data.

        This article was inspired by the work of Erlend M. Viggen (https://erlend-viggen.no/dlis-files/) who has created an excellent Jupyter Notebook which goes into more detail about working with DLIS files.  

        ### DLIS Files
        Digital Log Interchange Standard (DLIS) files are structured binary files that contain data tables for well information and well logging data. The file format was developed in the late 1980's by Schlumberger and subsequently published in 1991 by the American Petroleum Institute to create a standardised well log data format. Full details of the standard format can be found [here.](http://w3.energistics.org/rp66/v1/Toc/main.html). The DLIS file format can often be difficult and awkward to work with at times due to the format being developed nearly 30 years ago, and different software packages and vendors can create their own flavours of DLIS by adding in new structures and object-types.

        DLIS files contain large amounts of metadata associated with the well and data. These sections do not contain the well data, these are stored within Frames, of which there can be many representing different logging passes/runs or processing stages (e.g. Raw or Interpreted).  Frames are table objects which contain the well log data, where each column represents a logging curve, and that data is indexed by time or depth. Each logging curve within the frame is referred to as a channel. The channels can be a single dimension or multi-dimensional

        ### dlisio
        dlsio is a python library that has been developed by Equinor ASA to read DLIS files and Log Information Standard79 (LIS79) files. Details of the library can be found [here](https://dlisio.readthedocs.io/en/stable/index.html).

        ### Data
        The data used within this article was sourced from the [NLOG: Dutch Oil and Gas Portal](https://www.nlog.nl/en/welcome-nlog).

        **Privacy Notice:** DLIS files can contain information that can identify individuals that were involved in the logging operations. To protect their identity from appearing in search engine results without their excplicit consent, these fields have been hidden in this article/notebook.

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Library Imports 
        The first step with any project is to load in the libraries that we want to use. For this notebook we will be using [NumPy](https://numpy.org) for working with arrays, [pandas](https://pandas.pydata.org) for storing data, and [matplotlib](https://matplotlib.org) for displaying the data. To load the data, we will be using the [dlisio](https://github.com/equinor/dlisio) library. 

        Also, as we will be working with dataframes to view parameters, which can be numerous, we need to change the maximum number of rows that will be displayed when that dataframe is called. This is achieved by `pd.set_option('display.max_rows', 500)`.
        """
    )
    return


@app.cell
def _():
    from dlisio import dlis
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    pd.set_option('display.max_rows', 500)
    return dlis, np, pd, plt


@app.cell
def _():
    import dlisio
    dlisio.__version__
    return (dlisio,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading a DLIS File
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As we are working with a single DLIS file, we can use the following code to load the file. A physical DLIS file can contain multiple logical files, therefore, using this syntax allows the first file to be output to `f` and any subsequent logical files placed into `tail`.
        """
    )
    return


@app.cell
def _(dlis):
    f, *tail = dlis.load('Data/NLOG_LIS_LAS_7857_FMS_DSI_MAIN_LOG.DLIS')
    return f, tail


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can see the contents of each of these by calling upon their names. If we call upon `f`, we can see that it returns a `LogicalFile(00001_AC_WORK` and if we call upon `tail`, we get a blank list, which lets us know that there are no other logical files within the DLIS.
        """
    )
    return


@app.cell
def _(f, tail):
    print(f)
    print(tail)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To view the high level contents of the file we can use the `.describe()` method. This returns information about the number of frames, channels and objects within the Logical File. When we apply this to `f` we can see we have a file with 4 frames and 484 channels (logging curves), in addition to a number of known and unknown objects. 
        """
    )
    return


@app.cell
def _(f):
    f.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Viewing the File's Metadata
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Data Origin

        The first set of metadata we will look at is the origin. This provides information about the source of the data within the file. Occassionally, data may originate from multiple sources so we need to account for this by unpacking the origins into two variables. We can always check if there is other origin information by printing the length of the list.
        """
    )
    return


@app.cell
def _(f):
    origin, *origin_tail = f.origins
    print(len(origin_tail))
    return origin, origin_tail


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For this article, we will focus on `origin`. We can view the details of it, by calling upon `describe()`. This provides details about the field, well, and other file information.
        """
    )
    return


@app.cell
def _(origin):
    origin.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Frames
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Frames within a DLIS file can represent different logging passes or different stages of data, such as raw well log measurements to pertophysical interpretations or processed data. Each frame has a number of properties. The example code below prints out the properties in an easy-to-read format.
        """
    )
    return


@app.cell
def _(f):
    for frame in f.frames:
    
        # Search through the channels for the index and obtain the units
        for channel in frame.channels:
            if channel.name == frame.index:
                depth_units = channel.units
    
        print(f'Frame Name: \t\t {frame.name}')
        print(f'Index Type: \t\t {frame.index_type}')
        print(f'Depth Interval: \t {frame.index_min} - {frame.index_max} {depth_units}')
        print(f'Depth Spacing: \t\t {frame.spacing} {depth_units}')
        print(f'Direction: \t\t {frame.direction}')
        print(f'Num of Channels: \t {len(frame.channels)}')
        print(f'Channel Names: \t\t {str(frame.channels)}')
        print('\n\n')
    return channel, depth_units, frame


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This returns the following summary. Which indicates that two frames exist within this file. With the first frame containing basic well log curves of bitsize (BIT), caliper (CAL), gamma ray (GR) and tension (TEN). The second frame contains the post-processed acoustic waveform data.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Parameters within the DLIS File
        As seen earlier, we have a number of objects associated with the DLIS file. To make them easier to read we can create a short function that creates a pandas dataframe containing the parameters.
        """
    )
    return


@app.cell
def _(pd):
    def summary_dataframe(object, **kwargs):
        # Create an empty dataframe
        df = pd.DataFrame()
    
        # Iterate over each of the keyword arguments
        for i, (key, value) in enumerate(kwargs.items()):
            list_of_values = []
        
            # Iterate over each parameter and get the relevant key
            for item in object:
                # Account for any missing values.
                try:
                    x = getattr(item, key)
                    list_of_values.append(x)
                except:
                    list_of_values.append('')
                    continue
        
            # Add a new column to our data frame
            df[value]=list_of_values
    
        # Sort the dataframe by column 1 and return it
        return df.sort_values(df.columns[0])
    return (summary_dataframe,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The parameters can be accessed by calling upon `f.parameters`. To access the parameters, we can use the attributes `name`, `long_name` and `values` and pass these into the summary function.

        This returns a long table of each of the parameters. The example below is a small section of that table. From it, we can see parameters such as bottom log interval, borehole salinity and bottom hole temperature.
        """
    )
    return


@app.cell
def _(f, summary_dataframe):
    param_df = summary_dataframe(f.parameters, name='Name', long_name='Long Name', values='Value')

    # Hiding people's names that may be in parameters.
    # These two lines can be commented out to show them
    mask = param_df['Name'].isin(['R8', 'RR1', 'WITN', 'ENGI'])
    param_df = param_df[~mask]

    param_df
    return mask, param_df


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Channels

        The channels within a frame are the individual curves or arrays. To view a quick summary of these, we can pass in a number of attributes to the `summary_dataframe()` method.
        """
    )
    return


@app.cell
def _(f, summary_dataframe):
    channels = summary_dataframe(f.channels, name='Name', long_name='Long Name', dimension='Dimension', units='Units', frame='Frame')
    channels
    return (channels,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Tools 
        The tools object within the DLIS file contains information relating to the tools that were used to acquire the data. We can get a summary of the tools available be calling upon the `summary_dataframe` method.
        """
    )
    return


@app.cell
def _(f, summary_dataframe):
    tools = summary_dataframe(f.tools, name='Name', description='Description')
    tools
    return (tools,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As we are looking to plot acoustic waveform data, we can look at the parameters for the DSSTB - Dipole Shear Imager tool. First, we need to grab the object from the dlis and then pass it into the `summary_dataframe` function.

        From the returned table, we can view each of the parameters that relate to the tool and the processing of the data.
        """
    )
    return


@app.cell
def _(f, summary_dataframe):
    dsstb = f.object('TOOL', 'DSSTB')
    dsstb_params = summary_dataframe(dsstb.parameters, name='Name', long_name='Long Name', values='Values')
    dsstb_params
    return dsstb, dsstb_params


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Working With Data Objects
        Now that some of the meta data has been explored, we can now attempt to access the data stored within the file.

        Frames and data can be accessed by calling upon the `.object()` for the file. First, we can assign the frames to variables, which will make things easier when accessing the data within them, especially if the frames contain channels/curves with the same name. The `.object()` method requires the type of the object being accessed, i.e. 'FRAME' or 'CHANNEL' and its name. In this case we can refer back to the previous step which contains the channels and the frame names. We can see that the basic logging curves are in one frame and the acoustic data is in another.
        """
    )
    return


@app.cell
def _(f):
    frame1 = f.object('FRAME','60B')
    return (frame1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also directly access the channels for a specific curve. However, this can cause confusion when working with frames containing channels/curves with the same name. 

        The example below shows how to call key properties of the channel/curve. Details of which can be found [here.](https://dlisio.readthedocs.io/en/stable/dlis/api.html#dlisio.dlis.Channel)
        """
    )
    return


@app.cell
def _(f):
    dtc = f.object('CHANNEL', 'PWF4')

    # Print out the properties of the channel/curve
    print(f'Name: \t\t{dtc.name}')
    print(f'Long Name: \t{dtc.long_name}')
    print(f'Units: \t\t{dtc.units}')
    print(f'Dimension: \t{dtc.dimension}') #if >1, then data is an array
    return (dtc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Plotting Data
        Now that we know how to access the frames and channels of the DLIS file, we can now assign variable names to the curves that we are looking to plot. In this article, we will be plotting:

        - DTCO: Delta-T Compressional
        - DTSM: Delta-T Shear
        - SPR4: STC Slowness Projection, Receiver Array - Monopole P&S
        - PWF4: DSST Packed Waveform Data - Monopole P&S

        We will also need to assign a depth curve (TDEP) from the frame. Looking back at the information section of the frame, the `Depth Interval` is 0.1 inches. This needs to be converted to metres by multiplying by 0.00254.
        """
    )
    return


@app.cell
def _(frame1):
    curves = frame1.curves()

    depth = curves['TDEP'] * 0.00254
    dtco = curves['DTCO']
    dtsm = curves['DTSM']
    stc_mono = curves['SPR4']
    wf_mono = curves['PWF4']

    print(f'{depth.min()} - {depth.max()}')
    return curves, depth, dtco, dtsm, stc_mono, wf_mono


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To make an initial check on data, we can create a quick log plot of DTCO and DTSM against depth using matplotlib.
        """
    )
    return


@app.cell
def _(depth, dtco, dtsm, plt):
    plt.plot(depth, dtco)
    plt.plot(depth, dtsm)
    plt.ylim(40, 240)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Plotting the Semblance Map

        We will start with setting up a subplot with two axes and using `subplot2grid`. The first axis will contain the semblance plot and the second will be twinned with the first. This allows the data to be plotted on the same y-axis.

        To plot the semblance data we need to use `imshow`. When we do this, we need to pass in the extent of the array both in terms of depth range (using `depth.min() and depth.max()`) and the data range (40 - 240 us/ft).

        On top of that, the DTCO and DTSM curves can be plotted. This allows us to see how these curves were picked from the semblance map.


        """
    )
    return


@app.cell
def _(depth, dtco, dtsm, plt, stc_mono):
    (_fig, axes) = plt.subplots(figsize=(7, 10))
    _ax1 = plt.subplot2grid((1, 1), (0, 0))
    _ax2 = _ax1.twiny()
    _ax1.imshow(stc_mono, interpolation='bilinear', aspect='auto', cmap=plt.cm.jet, vmin=0, vmax=100, extent=[40, 240, depth.min(), depth.max()])
    _ax1.set_ylim(depth.max(), depth.min())
    _ax2.plot(dtco, depth, color='black')
    _ax2.plot(dtsm, depth, color='brown')
    _ax2.set_xlim(40, 240)
    plt.show()
    return (axes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Plotting the Processed Waveform Data

        We can modify the plot to add in a subplot for the acoustic waveform data associated with the semblance map. If we look at the shape of wf_mono we can see it returns (1606, 8, 512). This indicates that the array is multi-dimensional. The middle number indicates that we have 8 receivers worth of data.
        """
    )
    return


@app.cell
def _(wf_mono):
    wf_mono.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To access the first receiver, which is usually the closest one to the transmitter array, we can create a slice of the data like so:
        """
    )
    return


@app.cell
def _(wf_mono):
    wf_r1 = wf_mono[:, 0, :]
    print(wf_r1.min())
    print(wf_r1.max())
    return (wf_r1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This code returns the minimum and maximum values of the array, which can be used as a guide for scaling colours.

        Taking the plot code from the semblance map section, we can enhance it by adding another subplot. In this subplot, we will use another `imshow()` plot and pass in the relevant parameters. The `vmin` and `vmax` parameters can be used to tweak the image to bring out or reduce the detail within the waveform.
        """
    )
    return


@app.cell
def _(depth, dtco, dtsm, plt, stc_mono, wf_r1):
    _fig = plt.subplots(figsize=(10, 10))
    _ax1 = plt.subplot2grid((1, 2), (0, 0))
    _ax2 = _ax1.twiny()
    ax3 = plt.subplot2grid((1, 2), (0, 1))
    _ax1.imshow(stc_mono, interpolation='bilinear', aspect='auto', cmap=plt.cm.jet, vmin=0, vmax=100, extent=[40, 240, depth.min(), depth.max()])
    _ax1.set_title('Monopole Semblance')
    _ax2.plot(dtco, depth, color='black')
    _ax2.set_xlim(40, 240)
    _ax2.set_xticks([])
    _ax2.plot(dtco, depth, color='black')
    _ax2.plot(dtsm, depth, color='brown')
    ax3.set_title('Monopole Waveform R1')
    ax3.imshow(wf_r1, interpolation='bilinear', aspect='auto', cmap=plt.cm.seismic, vmin=-2000, vmax=2000, extent=[0, 3000, depth.min(), depth.max()])
    ax3.set_xlim(0, 1000)
    for ax in [_ax1, _ax2, ax3]:
        ax.set_ylim(depth.max(), depth.min())
    return ax, ax3


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Adding Interactive Controls

        Rather than rerunning the cell each time the depth and/or DT plot scales require changing, we can add a few interactive widgets to help with this. This can be achieved by importing `ipywidgets` and `IPython.display`. 
        The plot code can be placed inside a function and decorated with the widgets code. In the example below, we are passing in MinDepth, MaxDepth, MinDT and MaxDT. All four of which can be called upon in the code.
        """
    )
    return


@app.cell
def _(depth, dtco, dtsm, plt, stc_mono, wf_r1):
    import ipywidgets as widgets
    from IPython.display import display

    @widgets.interact(MinDepth=(depth.min(), depth.max(), 10), MaxDepth=(depth.min(), depth.max(), 10), MinDT=(40, 240, 5), MaxDT=(40, 240, 5))
    def acoustic_plot(MinDepth=depth.min(), MaxDepth=depth.max(), MinDT=40, MaxDT=240):
        _fig = plt.subplots(figsize=(10, 10))
        _ax1 = plt.subplot2grid((1, 2), (0, 0))
        _ax2 = _ax1.twiny()
        ax3 = plt.subplot2grid((1, 2), (0, 1))
        _ax1.imshow(stc_mono, interpolation='bilinear', aspect='auto', cmap=plt.cm.jet, vmin=0, vmax=100, extent=[40, 240, depth.min(), depth.max()])
        _ax1.set_xlim(MinDT, MaxDT)
        _ax1.set_title('Monopole Semblance')
        _ax2.plot(dtco, depth, color='black')
        _ax2.set_xlim(MinDT, MaxDT)
        _ax2.set_xticks([])
        _ax2.plot(dtco, depth, color='black')
        _ax2.plot(dtsm, depth, color='brown')
        ax3.set_title('Monopole Waveform R1')
        ax3.imshow(wf_r1, interpolation='bilinear', aspect='auto', cmap=plt.cm.seismic, vmin=-2000, vmax=2000, extent=[0, 3000, depth.min(), depth.max()])
        ax3.set_xlim(0, 1000)
        for ax in [_ax1, _ax2, ax3]:
            ax.set_ylim(MaxDepth, MinDepth)
    return acoustic_plot, display, widgets


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Summary
        In this article, we have covered how to load a DLIS file using the DLISIO Python library. Once the DLIS file is loaded, different parameter tables and logging curves can be viewed and extracted. We have also seen how we can take processed acoustic waveform data and plot it using matplotlib. DLIS files don't have to be daunting to work with in Python. Once the basic structure and commands from DLISIO are understood it becomes much simpler.


        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ***Thanks for reading!***

        *If you have found this article useful, please feel free to check out my other articles looking at various aspects of Python and well log data. You can also find my code used in this article and others at [GitHub](https://github.com/andymcdgeo).*

        *If you want to get in touch you can find me on [LinkedIn](https://www.linkedin.com/in/andymcdonaldgeo/) or at my [website](http://andymcdonald.scot/).*

        *Interested in learning more about python and well log data or petrophysics? Follow me on [Medium](https://medium.com/@andymcdonaldgeo).*
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## References
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        [Viggen, E.M. Extracing data from DLIS Files](https://erlend-viggen.no/dlis-files/)  
        [Viggen, E.M, Harstad, E., and Kvalsvik J. (2020), Getting started with acoustic well log data using the dlisio Python library on the Volve Data Village dataset](https://www.researchgate.net/publication/340645995_Getting_started_with_acoustic_well_log_data_using_the_dlisio_Python_library_on_the_Volve_Data_Village_dataset)

        [NLOG: Dutch Oil and Gas Portal](https://www.nlog.nl/en/welcome-nlog)

        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
