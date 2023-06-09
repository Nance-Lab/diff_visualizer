
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