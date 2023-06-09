""" 
Module for making PCA plots from MPT datasets
"""

from matplotlib import pyplot as plt
import numpy as np


def plot_pca(pca_embeddings_df, target_column, num_points='all'):
# Normal PCA
    fig = plt.figure(figsize=(12,7))
    for unique_class in pca_embeddings_df[target_column].unique():
        print(unique_class)
<<<<<<< HEAD
        df = pca_embeddings_df[pca_embeddings_df[target_column] == unique_class] # We plot less points to make a cleaner figure
=======
        df = pca_embeddings_df[pca_embeddings_df[target_column] == unique_class].sample(100) # We plot less points to make a cleaner figure
>>>>>>> e9ea4459f035cbc4b8b8487f7ae1785bcf937d07
        x = df['Component 1']
        y = df['Component 2']
        plt.scatter(x,y, alpha=0.5, s=4, label=unique_class)#, c=colors[unique_class])
    plt.legend(loc='lower left')
    plt.xlim([-13,13])
    plt.ylim([-13,13])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('First and Second Principal Components of Age Dataset')

    return fig


# Bi plot
def myplot(score,coeff,labels=None, targets=None, num_points='all'):


    """
    examples to run this:
    fig = plt.figure(figsize=(12,8))
    myplot(pca_embeddings[:,0:2],np.transpose(pca.components_[0:2, :]), labels=col_names, targets=labels, num_points=2500)
    plt.title('Bi-plot of First and Second Principal Components of Age Dataset')

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
            plt.scatter(x, y, alpha=0.5, s=1, label=uclass)
        else:
            inds = np.random.randint(0, len(x), num_points)
            plt.scatter(x[inds], y[inds], alpha=0.5, s=1, label=uclass)
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
    plt.legend(loc='lower left')

    #plt.grid()
