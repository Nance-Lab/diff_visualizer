import pandas as pd
import numpy as np
from sklearn.preprocessing import scale, StandardScaler
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA


def pca_plot(df, n_components=2, labels=None, scale=True, plot=True, save=False, save_path=None):
    """
    Function to perform PCA on a dataframe and plot the results. 
    """
    print('This is the NEW function!!!')
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
    principal_df = pd.DataFrame(principal_components[:, :2], columns=['Component 1', 'Component 2'])
    principal_df[labels] = label_col
    # Get the explained variance 
    explained_variance = pca.explained_variance_ratio_
    # Plot the results 
    if plot:
        plt.figure(figsize=(10, 10))
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.title('PCA Plot')
        for label in np.unique(label_col):
            print(label)
            label_df = principal_df[principal_df[labels]==label]
            plt.scatter(label_df['Component 1'], label_df['Component 2'], label=label, alpha=0.5, s=4)
        plt.legend(loc='lower left')
        plt.xlim([-13,13])
        plt.ylim([-13,13])
        plt.show()
    # Save the plot 
    if save:
        plt.savefig(save_path)
    # Return the explained variance 
    return explained_variance

def plot_pca_bi_plot(score,coeff,labels=None, targets=None, num_points='all'):
    """
    Function to plot a biplot of the PCA results.

    """
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    for uclass in np.unique(targets):
        x = (xs[targets==uclass])*scalex
        y = (ys[targets==uclass])*scaley
        if num_points == 'all':
            plt.scatter(x, y, alpha=0.5, s=1)
        else:
            inds = np.random.randint(0, len(x), num_points)
            plt.scatter(x[inds], y[inds], alpha=0.5, s=1)
    #plt.scatter(xs * scalex,ys * scaley)#, c = y)
    for i in range((n//2), n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'k', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0], coeff[i,1], labels[i], color = 'k', ha = 'center', va = 'center')
    plt.xlim(-0.6,.6)
    plt.ylim(-.6,.6)
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()