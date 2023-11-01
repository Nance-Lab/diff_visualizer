import seaborn as sns
import matplotlib.pyplot as plt

def feature_violin_plot(df, feature_to_plot, label_column=None, figsize=(2,2), title=None):
    """
    Function to plot a violin plot of a feature in a dataframe. 

    Parameters
    ----------
        df (pd.DataFrame): Dataframe containing the data to plot
        feature_to_plot (String): Name of the feature to plot
        label_column (String): column name of the labels in the dataframe. If None, no labels will be plotted
        figsize (tuple): Size of the figure to plot
        title (String): Title of the plot

    Returns
    -------
        fig: seaborn figure of the violin plot
    """
    #df = df[df[feature_to_plot]<10] #temporary fix for outliers

    fig = plt.figure(figsize=figsize)
    if label_column is None:
        sns.violinplot(x=df[feature_to_plot])
    else:
        sns.violinplot(x=label_column, y=feature_to_plot, data=df)
    plt.title(title)
    return fig
