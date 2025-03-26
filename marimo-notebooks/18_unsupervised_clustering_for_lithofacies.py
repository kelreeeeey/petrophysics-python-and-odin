import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # How to Use Unsupervised Clustering on Well Log Data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Understanding the subsurface lithology is an important task in geoscience and petrophysics. Using a variety of electrical measurements generated from well logging technology we are able to make inferences about the underlying geology, such as the lithology, facies, porosity, and permeability. 

        Machine Learning algorithms have routinely been adopted to group well log measurements into distinct lithological groupings, known as facies. This process can be achieved using either unsupervised learning or supervised learning algorithms. 

        __Supervised learning__ is the most common and practical of machine learning tasks and it is designed to learn from example using input data that has been mapped to the "correct" output. Alternatively, we can run the modelling using __Unsupervised Learning__, where we let the algorithms identify underlying patterns within the data that may not be easily visible during data exploration. 

        In this tutorial we will be carrying out unsupervised learning classification using three clustering methods (K Means Clustering, Gaussian Mixture Modelling and DBSCAN) and comparing the results with an established Lithofacies curve.

        ## What is Clustering / Cluster Analysis?
        Clustering of data is a common form of exploratory data analysis (EDA) which is used to divide up the data into different groups based on shared characteristics or properties. Data points that are similar to each other are grouped together in the same cluster, and those that are different are placed in another cluster.

        ### K-Means Clustering
        K-Means clustering is a very commonly used unsupervised machine learning algorithm. It is used to group data into K number of clusters by minimising the distance between the data point and the centroid. 

        The centroid is initialised at k random points in the data space and all points around it are assigned to the relevant cluster based on the distance to the centroid. The centroid is then adjusted to the central point of the cluster and the points surrounding it are reassigned. This continues until either there is no change in the centroids or the points remain in the same cluster or until a maximum number of iterations is reached.

        K-Means is a hard clustering method where a data point either belongs to a cluster or it does not. It also carries out clustering by applying a circle (or hyper-sphere in multi-dimensional datasets)to the data.


        ### Gaussian Mixture Modelling
        The GMM method also allows data points to be clustered, except that it accounts for data variance, results in a softer classification and rather than being distance based it is distribution based. 

        Also, the data point being classified has a probability of being one cluster or another. 

        While K-Means clustering works great if the data clusters are circular, however, in petrophysical and geological situations data rarely forms nice circular patterns. GMM modelling uses eliptical shaped cluster/decision boundaries and are therefore more flexible.

        An excellent article looking at the differences between the two methods can be found at https://www.analyticsvidhya.com/blog/2019/10/gaussian-mixture-models-clustering/

        ## Dataset
        The dataset we are using for this tutorial forms part of a Machine Learning competition run by Xeek and FORCE 2020 (https://doi.org/10.5281/zenodo.4351155). The objective of the compettion was to predict lithology from existing labelled data. The dataset consists of 118 wells from the Norwegian Sea.

        ## Importing Libraries & Data Loading
        The first step of the project is to import the libraries that we require.  For this example we will be using [NumPy](https://numpy.org) for working with arrays, [pandas](https://pandas.pydata.org) for storing data, [seaborn](https://seaborn.pydata.org) and [matplotlib](https://matplotlib.org) for displaying the data.
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import matplotlib.colors as colors
    return colors, np, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We will then read in the data using `pd.read_csv` and then view the data description using the `describe()` method. 
        """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv("Data/xeek_train_subset.csv")
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As it is quite a big table, we can view the columns by calling upon `df.columns`.
        """
    )
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We don't need all of the columns for this example, so we will take a copy of the dataframe with the required logging measurements, including the well name and the depth curve.
        """
    )
    return


@app.cell
def _(df):
    workingdf = df[["WELL", "DEPTH_MD", "RDEP", "RHOB", "GR", "NPHI", "PEF", "DTC", "FORCE_2020_LITHOFACIES_LITHOLOGY"]].copy()
    return (workingdf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We will also rename the `FORCE_2020_LITHOFACIES_LITHOLOGY` column to something simpler like `FACIES`.
        """
    )
    return


@app.cell
def _(workingdf):
    workingdf.rename(columns={'FORCE_2020_LITHOFACIES_LITHOLOGY':'FACIES'}, inplace=True)
    return


@app.cell
def _(workingdf):
    workingdf
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Column Remapping / Renaming
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To make things simpler with plotting, and understanding what the lithology numbers supplied with the data mean, we can create two dictionaries and map the `FACIES` column to two new columns.

        The first is creating a dictionary for the string representations of the numbers.
        """
    )
    return


@app.cell
def _():
    lithology_numbers = {30000: 'Sandstone',
                     65030: 'Sandstone/Shale',
                     65000: 'Shale',
                     80000: 'Marl',
                     74000: 'Dolomite',
                     70000: 'Limestone',
                     70032: 'Chalk',
                     88000: 'Halite',
                     86000: 'Anhydrite',
                     99000: 'Tuff',
                     90000: 'Coal',
                     93000: 'Basement'}
    return (lithology_numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The second dictionary is simplifying the lithology number to range from 1 to 12 instead of the large range of numbers used in the original data. This will help when it comes to making a log plot.
        """
    )
    return


@app.cell
def _():
    simple_lithology_numbers = {30000: 1,
                     65030: 2,
                     65000: 3,
                     80000: 4,
                     74000: 5,
                     70000: 6,
                     70032: 7,
                     88000: 8,
                     86000: 9,
                     99000: 10,
                     90000: 11,
                     93000: 12}
    return (simple_lithology_numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To create new columns in our dataframe, we start with defining the column name `workingdf['LITH']` and then we assign the mapped values using the `.map()` method.

        We do this for both the string and simple number representations of the facies.
        """
    )
    return


@app.cell
def _(lithology_numbers, workingdf):
    workingdf['LITH'] = workingdf['FACIES'].map(lithology_numbers)
    return


@app.cell
def _(simple_lithology_numbers, workingdf):
    workingdf['LITH_SI'] = workingdf['FACIES'].map(simple_lithology_numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When we view the dataframe, we can see that we now have our two new columns at the end.
        """
    )
    return


@app.cell
def _(workingdf):
    workingdf
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Visualising the Data

        As there is already a FACIES column with this data, we can take a quick look to see how the data is distributed across each lithofacies.

        To do this we can use Seaborn's `FacetGrid` method to plot individual density-neutron crossplots (scatterplots) for each lithology. 

        The FacetGrid is used to create an underlying structure for the plot. In this example, the FacetGrid has been passed the dataframe we are working with (`workingdf`), the column we want to split the plots up by (`col`) and the point at which we want to wrap to a new row (`col_wrap`). In this instance, once there are 4 columns, then the data will wrap.

        We can then map a density neutron crossplot ontop of that `FacetGrid`.
        """
    )
    return


@app.cell
def _(sns, workingdf):
    g = sns.FacetGrid(workingdf, col='LITH', col_wrap=4)
    g.map(sns.scatterplot, 'NPHI', 'RHOB', alpha=0.5)
    g.set(xlim=(-0.15, 1))
    g.set(ylim=(3, 1))
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before we plot any data we need to create a few functions. The first is a create plot function, which will take a number of arguments and our facies curve, and will generate a conventional log plot.
        """
    )
    return


@app.cell
def _(colors, np, plt):
    def create_plot(wellname, dataframe, curves_to_plot, depth_curve, log_curves=[], facies_curves=[]):
        # Count the number of tracks we need
        num_tracks = len(curves_to_plot)
    
        facies_color = ['#F4D03F', '#F5B041','#DC7633','#6E2C00', '#1B4F72','#2E86C1', '#AED6F1', '#A569BD', '#196F3D', 'red','black', 'blue']
    
            
        # Setup the figure and axes
        fig, ax = plt.subplots(nrows=1, ncols=num_tracks, figsize=(num_tracks*2, 10))
    
        # Create a super title for the entire plot
        fig.suptitle(wellname, fontsize=20, y=1.05)
    
        # Loop through each curve in curves_to_plot and create a track with that data
        for i, curve in enumerate(curves_to_plot):
            if curve in facies_curves:
                cmap_facies = colors.ListedColormap(facies_color[0:dataframe[curve].max()], 'indexed')
            
                cluster=np.repeat(np.expand_dims(dataframe[curve].values,1), 100, 1)
                im=ax[i].imshow(cluster, interpolation='none', cmap=cmap_facies, aspect='auto',vmin=dataframe[curve].min(),vmax=dataframe[curve].max(), 
                                extent=[0,20, depth_curve.max(), depth_curve.min()])
            
    #             for key in lithology_setup.keys():
    #                 color = lithology_setup[key]['color']
    #                 ax[i].fill_betweenx(depth_curve, 0, dataframe[curve].max(), 
    #                                   where=(dataframe[curve]==key),
    #                                   facecolor=color)
    #                 
            else:
                ax[i].plot(dataframe[curve], depth_curve)

        
            # Setup a few plot cosmetics
            ax[i].set_title(curve, fontsize=14, fontweight='bold')
            ax[i].grid(which='major', color='lightgrey', linestyle='-')
        
            # We want to pass in the deepest depth first, so we are displaying the data 
            # from shallow to deep
            ax[i].set_ylim(depth_curve.max(), depth_curve.min())
    #         ax[i].set_ylim(3500, 3000)

            # Only set the y-label for the first track. Hide it for the rest
            if i == 0:
                ax[i].set_ylabel('DEPTH (m)', fontsize=18, fontweight='bold')
            else:
                plt.setp(ax[i].get_yticklabels(), visible = False)
        
            # Check to see if we have any logarithmic scaled curves
            if curve in log_curves:
                ax[i].set_xscale('log')
                ax[i].grid(which='minor', color='lightgrey', linestyle='-')
        

    
        plt.tight_layout()
        plt.show()
    
        return cmap_facies
    return (create_plot,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Splitting Data by Well Function
        The second method we will create will be used to split up our dataframe by wells. This is done using the `groupby` function, and will allow us to store each dataframe within a list for easy access later.
        """
    )
    return


@app.cell
def well_splitter():
    def well_splitter(dataframe, groupby_column):
        grouped = dataframe.groupby(groupby_column)
    
        # Create empty lists
        wells_as_dfs = []
        wells_wellnames = []

        #Split up the data by well
        for well, data in grouped:
            wells_as_dfs.append(data)
            wells_wellnames.append(well)

        print('index  wellname')
        for i, name in enumerate(wells_wellnames):
            print(f'{i}      {name}')
    
        return wells_as_dfs, wells_wellnames
    return (well_splitter,)


@app.cell
def _(well_splitter, workingdf):
    grouped_wells, grouped_names = well_splitter(workingdf, 'WELL')
    return grouped_names, grouped_wells


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We now have a list of wells and their index position with the list object. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Clustering - Unsupervised
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this section, we are going to setup our clustering models and run them on our dataset.

        First we will import our clustering models from the sklearn library.
        """
    )
    return


@app.cell
def _():
    from sklearn.cluster import KMeans
    from sklearn.mixture import GaussianMixture
    return GaussianMixture, KMeans


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Finding the Optimum Number of Clusters

        To make sure that K-Means and Gaussian Mixture Modelling models are working efficiently we need to provide them with a starting number of clusters. If the number of clusters is incorrectly selected, the algorithms may not perform well or could take longer to resolve (especially if the number is too high).

        We can attempt to identify the optimum number of clusters using an elbow plot, where the goal is to select a number for the clusters based on the 'elbow' or inflection formed in the results. There are other methods such as the silhouette method for picking the number of clusters.

        For this example, we will use the elbow plot. To do this we evaluate the model performance over a given range of clusters, and then from the plot identify the most suitable number.
        """
    )
    return


@app.cell
def _(KMeans, plt):
    def optimise_k_means(data, max_k):
        means = []
        inertias = []
        for k in range(1, max_k):
            _kmeans = KMeans(n_clusters=k)
            _kmeans.fit(data)
            means.append(k)
            inertias.append(_kmeans.inertia_)
        fig = plt.subplots(figsize=(10, 5))
        plt.plot(means, inertias, 'o-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Inertia')
        plt.grid(True)
        plt.show()
    return (optimise_k_means,)


@app.cell
def _(KMeans, plt, workingdf):
    from yellowbrick.cluster import SilhouetteVisualizer

    def visualise_k_means_sillouette(data, max_k):
        (fig, ax) = plt.subplots(2, 3, figsize=(10, 5))
        means = []
        silhouette_avg = []
        for k in range(2, max_k):
            print(k)
            _kmeans = KMeans(n_clusters=k)
            (q, mod) = divmod(k, 2)
            vis = SilhouetteVisualizer(_kmeans, colors='yellowbrick', ax=ax[q - 1][mod])
            vis.fit(data)
    data = workingdf[['GR', 'RHOB', 'NPHI', 'DTC']]
    _kmeans = KMeans(n_clusters=10)
    visualizer = SilhouetteVisualizer(_kmeans, colors='yellowbrick')
    visualizer.fit(data)
    visualizer.show()
    return SilhouetteVisualizer, data, visualise_k_means_sillouette, visualizer


@app.cell
def _(KMeans, plt, workingdf):
    from sklearn.metrics import silhouette_score

    def optimise_k_means_sillouette(data, max_k):
        means = []
        silhouette_avg = []
        range_n_clusters = [2, 3, 4, 5, 6, 7, 8]
        silhouette_avg = []
        for num_clusters in range_n_clusters:
            _kmeans = KMeans(n_clusters=num_clusters)
            _kmeans.fit(data)
            cluster_labels = _kmeans.labels_
            silhouette_avg.append(silhouette_score(data, cluster_labels))
        plt.plot(range_n_clusters, silhouette_avg, 'bo-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Analysis For Kmeans', fontsize=14, fontweight='bold')
        plt.show()
    optimise_k_means_sillouette(workingdf[['GR', 'RHOB', 'NPHI', 'DTC']], 5)
    return optimise_k_means_sillouette, silhouette_score


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For clustering to work, we need to remove any missing values. This is achieved using the `dropna()` function.
        """
    )
    return


@app.cell
def _(workingdf):
    workingdf.dropna(inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can then use the `describe()` function to make sure our data is still good after the missing data values have been removed. In this example we have gone from 133198 to 82732 depth levels.
        """
    )
    return


@app.cell
def _(workingdf):
    workingdf.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To keep our model simple we will work with four logging measurements (columns): Gamma Ray (GR), Bulk Density (RHOB), Neutron Porosity (NPHI) and Acoustic Compressional Slowness (DTC).
        """
    )
    return


@app.cell
def _(optimise_k_means, workingdf):
    optimise_k_means(workingdf[['GR', 'RHOB', 'NPHI', 'DTC']], 30)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the plot above, we can see that the inertia (sum of the squared distances to the nearest cluster center) decreases as we increase the number of clusters. There is no clear defined break within this dataset, however, we can see that the slope changes from about 5 clusters onwards. The picking of this value will be dependent on the interpreter and could range from 4 to 10.

        So for this example we will take 5 as the optimum number of clusters.

        ### Fitting the Clustering Models
        """
    )
    return


@app.cell
def _(KMeans, workingdf):
    _kmeans = KMeans(n_clusters=5)
    _kmeans.fit(workingdf[['GR', 'RHOB', 'NPHI', 'DTC']])
    workingdf['KMeans'] = _kmeans.labels_
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To make the comparison simple, we will use the same number of clusters in the Gaussian Mixture Model. For this model the number of clusters parameter is known as n_components.
        """
    )
    return


@app.cell
def _(GaussianMixture, workingdf):
    # Create the gmm model with the selected number of clusters/components
    gmm = GaussianMixture(n_components=5)

    # Fit the model to our dataset
    gmm.fit(workingdf[['GR', 'RHOB', 'NPHI', 'DTC']])

    # Predict the labels
    gmm_labels = gmm.predict(workingdf[['GR', 'RHOB', 'NPHI', 'DTC']])

    # Assign the labels back to the workingdf
    workingdf['GMM'] = gmm_labels
    return gmm, gmm_labels


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Plotting the Results

        Now that the clusters have been computed using KMeans and GMM methods, we can plot the data to see how well the predicted in relation to the labelled lithologies. Note that these methods are unsupervised and do not use the labelled data for training. We are comparing here how well unsupervised methods perform with well log data.

        As we predicted into the main `workingdf` dataframe, we need to split the data up again into individual wells. We can do this by calling upon the simple function created earlier.
        """
    )
    return


@app.cell
def _(well_splitter, workingdf):
    dfs_wells, wellnames = well_splitter(workingdf, 'WELL')
    return dfs_wells, wellnames


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The first plot we will look at is the logplot. We will pass in the original lithofacies (LITH_SI) column and the newly computed KMeans and GMM results.
        """
    )
    return


@app.cell
def _(create_plot, dfs_wells, wellnames):
    # Setup the curves to plot
    curves_to_plot = ['GR', 'RHOB', 'NPHI', 'DTC',  'LITH_SI', 'KMeans','GMM']
    logarithmic_curves = ['RDEP']
    facies_curve=['KMeans','GMM', 'LITH_SI']

    # Create plot by passing in the relevant well index number
    well = 4
    cmap_facies = create_plot(wellnames[well], 
                dfs_wells[well], 
                curves_to_plot, 
                dfs_wells[well]['DEPTH_MD'], 
                logarithmic_curves, facies_curve)
    return cmap_facies, curves_to_plot, facies_curve, logarithmic_curves, well


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the plot above we have the original Lithology and our computed KMeans and GMM cluster results in the last three subplots. 

        The first thing to note is that the colours do not neccessarily mean the data is from the same group across each method. There are way to map these so that the colouring is consistent, but for the purposes of this tutorial, we will not go into this.

        Looking at well 16/10-1 (index 4), we have 10 separate facies/groups displayed and we can see that these mostly tie up with the changes in the logging measurements. For example the decrease in Gamma Ray (GR) from around 2300m to around 2775m ties in nicely with the blue and light blue grouping. In the KMeans and GMM models, this section has also been highlighted as being in the same cluster in both methods, however, there is no variation in this section. As both of these methods were set to a max of 5 clusters, we will not be able to capture the same degree of variation.

        To resolve this, we could increase the number of clusters.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Viewing Results on Scatterplots / Crossplots

        Another way to view the performance of the clustering is through scatter plots. We can do this using the common density-neutron scatterplots / crossplots and using matplotlib.
        """
    )
    return


@app.cell
def _(cmap_facies, dfs_wells, plt, well):
    fig, ax = plt.subplots(figsize=(20,10))
    ax1 = plt.subplot2grid((1,3), (0,0))
    ax1.scatter(dfs_wells[well]['NPHI'], dfs_wells[well]['RHOB'], c=dfs_wells[well]['KMeans'], s=8, cmap=cmap_facies)
    ax1.set_title('KMeans', fontsize=22, y=1.05)

    ax2 = plt.subplot2grid((1,3), (0,1))
    ax2.scatter(dfs_wells[well]['NPHI'], dfs_wells[well]['RHOB'], c=dfs_wells[well]['GMM'], s=8)
    ax2.set_title('GMM', fontsize=22, y=1.05)

    ax3 = plt.subplot2grid((1,3), (0,2))
    ax3.scatter(dfs_wells[well]['NPHI'], dfs_wells[well]['RHOB'], c=dfs_wells[well]['LITH_SI'], s=8)
    ax3.set_title('Lithology (Supplied)', fontsize=22, y=1.05)

    for ax in [ax1, ax2, ax3]:
        ax.set_xlim(0, 0.7)
        ax.set_ylim(3, 1.5)
        ax.set_ylabel('RHOB', fontsize=18, labelpad=30)
        ax.set_xlabel('NPHI', fontsize=18, labelpad=30)
        ax.grid()
        ax.set_axisbelow(True)

        ax.tick_params(axis='both', labelsize=14)
    plt.tight_layout()
    return ax, ax1, ax2, ax3, fig


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Even though there is mixing of the clusters in each method, the interval that was discussed in the log plot section can be identified in the lower left of the plot, where we have higher density values and lower neutron porosity values.

        In the KMeans grouping, this cluster shows as one complete cluster, however, in the GMM method we can see it matches closer to the supplied lithology.

        ### Viewing Results on a Pairplot
        As we used four input curves for our model, we should look at all of these to see how the clusters vary. The best way to do this is to use the excellent pairplot from the seaborn library. This plot displays the relationships between the data in the dataset on a grid. This allows a quick and easy way to identify and visualise the data. Along the diagonal the distribution of the data split by cluster is also plotted.

        As we are looking at well number 4 we need to pass in that dataframe to the pairplot (dfs_wells[4])
        """
    )
    return


@app.cell
def _(dfs_wells, sns):
    sns.pairplot(dfs_wells[4], vars=['GR', 'RHOB','NPHI', 'DTC'], hue='KMeans', palette='Dark2',
                 diag_kind='kde', plot_kws = {'s': 15, 'marker':'o', 'alpha':1})
    return


@app.cell
def _(dfs_wells, sns):
    sns.pairplot(dfs_wells[4], vars=['GR', 'RHOB','NPHI', 'DTC'], hue='GMM', palette='Dark2',
                 diag_kind='kde', plot_kws = {'s': 15, 'marker':'o', 'alpha':1})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This provides us a much nicer plot to look at and also allows us to see how the data is clustered in the other logging curves. We can see that the GMM model provides some improvement in defining the clusters, especially in the DTC vs RHOB plot.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Summary
        In this article we have covered the basics for carrying out unsupervised cluster analysis using two popular algorithms - KMeans Clustering and Gaussian Mixture Modelling. Using an optimisation method we have determined, by eye, that the optimum number of clusters was five, however, it is worth experimenting with more clusters to see if this provides a better match.

        Once the clustering was complete, we saw multiple ways to visualise the results: a standard log plot setup, scatter plots and seaborn's pairplot. 

        As K-Means clustering utilises spherical clusters, it may not always be appropriate to well log data and the subsurface. However, Gaussian Mixture Modelling does appear to provide a slight improvement in clustering.

        ***Thanks for reading!***

        *If you have found this article useful, please feel free to check out my other articles looking at various aspects of Python and well log data. You can also find my code used in this article and others at [GitHub](https://github.com/andymcdgeo).*

        *If you want to get in touch you can find me on [LinkedIn](https://www.linkedin.com/in/andymcdonaldgeo/) or at my [website](http://andymcdonald.scot/).*

        *Interested in learning more about python and well log data or petrophysics? Follow me on [Medium](https://medium.com/@andymcdonaldgeo).*

        If you have enjoyed this article or any others and want to show your appreciate you are welcome to [Buy Me a Coffee](https://www.buymeacoffee.com/andymcdonaldgeo)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # References

        Bormann, Peter, Aursand, Peder, Dilib, Fahad, Manral, Surrender, & Dischington, Peter. (2020). FORCE 2020 Well well log and lithofacies dataset for machine learning competition [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4351156
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
