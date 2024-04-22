import pandas as pd
import numpy as np
from sklearn.preprocessing import scale, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def pca_plot(
    df, n_components=2, labels=None, scale=True, plot=True, save=False, save_path=None
):
    """
    Function to perform PCA on a dataframe and plot the results.

    Parameters
    ----------
        df (pd.DataFrame): Dataframe containing the data to plot
        n_components (int): Number of principal components to plot
        labels (String): column name of the labels in the dataframe. If None, no labels will be plotted
        scale (bool): Whether to scale the data before performing PCA
        plot (bool): Whether to plot the results
        save (bool): Whether to save the plot
        save_path (String): Path to save the plot

    Returns
    -------
        fig: matplotlib figure of the PCA plot
    """
    if labels:
        label_col = df[labels]
        df = df.drop(labels, axis=1)
    # Scale the data
    if scale:
        df = StandardScaler().fit_transform(df)
    # Perform PCA
    pca = PCA(n_components=n_components)
    pca.fit(df)
    # Get the principal components
    principal_components = pca.transform(df)
    # Create a dataframe of the principal components
    principal_df = pd.DataFrame(
        principal_components[:, :2], columns=["Component 1", "Component 2"]
    )
    principal_df[labels] = label_col
    # Get the explained variance
    explained_variance = pca.explained_variance_ratio_
    # Plot the results
    if plot:
        plt.figure(figsize=(10, 10))
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.title("PCA Plot")
        for label in np.unique(label_col):
            print(label)
            label_df = principal_df[principal_df[labels] == label]
            plt.scatter(
                label_df["Component 1"],
                label_df["Component 2"],
                label=label,
                alpha=0.5,
                s=4,
            )
        plt.legend(loc="lower left")
        plt.xlim([-13, 13])
        plt.ylim([-13, 13])
        # plt.show()
    # Save the plot
    if save:
        plt.savefig(save_path)
    # Return the explained variance
    return plt.gcf(), explained_variance


def plot_pca_bi_plot(
    df,
    n_components=2,
    features=None,
    target_col=None,
    num_points="all",
    title="PCA Biplot of First and Second Principal Components",
):
    """
    Function to plot a biplot of the PCA results.

    Parameters
    ----------
        score (np.array): Array of the PCA scores
        coeff (np.array): Array of the PCA coefficients
        labels (list): List of the feature names
        target_col (string): Name of the column containing the labels
        num_points (int): Number of points to plot. If 'all', all points will be plotted

    Returns
    -------
        fig: matplotlib figure of the biplot

    """
    fig = plt.figure(figsize=(12, 8))

    if target_col:
        labels = np.array(df[target_col])
        label_col = df[target_col]
        df = df.drop(target_col, axis=1)

    df = df[features]
    # Scale the data
    df = StandardScaler().fit_transform(df)
    # Perform PCA
    pca = PCA(n_components=n_components).fit(df)
    # Get the principal components
    principal_components = pca.transform(df)
    # Create a dataframe of the principal components
    principal_df = pd.DataFrame(
        principal_components[:, :2], columns=["Component 1", "Component 2"]
    )
    principal_df[target_col] = label_col
    # Get the explained variance
    score = principal_components[:, 0:2]
    coeff = np.transpose(pca.components_[0:2, :])

    xs = score[:, 0]
    ys = score[:, 1]
    n = coeff.shape[0]
    scalex = 1.0 / (xs.max() - xs.min())
    scaley = 1.0 / (ys.max() - ys.min())
    for uclass in np.unique(labels):
        x = (xs[labels == uclass]) * scalex
        y = (ys[labels == uclass]) * scaley
        if num_points == "all":
            plt.scatter(x, y, alpha=0.5, s=1, label=uclass)
        else:
            inds = np.random.randint(0, len(x), num_points)
            plt.scatter(x[inds], y[inds], alpha=0.5, s=1, label=uclass)
    # plt.scatter(xs * scalex,ys * scaley)#, c = y)
    for i in range((n // 2), n):
        plt.arrow(0, 0, coeff[i, 0], coeff[i, 1], color="r", alpha=0.5)
        if features is None:
            plt.text(
                coeff[i, 0] * 1.15,
                coeff[i, 1] * 1.15,
                "Var" + str(i + 1),
                color="k",
                ha="center",
                va="center",
            )
        else:
            plt.text(
                coeff[i, 0],
                coeff[i, 1],
                features[i],
                color="k",
                ha="center",
                va="center",
            )
    plt.xlim(-0.6, 0.6)
    plt.ylim(-0.6, 0.6)
    plt.xlabel(f"PC{1}")
    plt.ylabel(f"PC{2}")
    plt.grid()
    plt.legend(loc="lower left")
    plt.title(title)
    # fig = plt.gcf()
    return fig
