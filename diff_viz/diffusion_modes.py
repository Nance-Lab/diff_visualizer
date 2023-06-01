"""
Functions for plotting diffusion modes of nanoparticle trajecories from MPT data
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_diffusion_modes_single_label(ecm, label_name, bar_width=0.01, figsize=(1, 4), color_constrained='#b7a57a',
                                    color_normal='#999999', color_directed='#4b2e83', ylim=(0, 1),
                                    legend_loc='lower right', legend_fontsize=8, title_fontsize=15,
                                    tick_fontsize=15):
    """
    Plot the percentage of diffusion modes per age using a bar chart.

    Parameters:
        ecm (pandas.DataFrame): DataFrame containing diffusion mode data with 'alpha' column.
        label_name (str): Name of the label for the bar chart.
        bar_width (float): Width of the bars in the bar chart. Default is 0.01.
        figsize (tuple): Figure size (width, height) in inches. Default is (1, 4).
        color_constrained (str): Color for the 'Subdiffusive' bars. Default is '#b7a57a'.
        color_normal (str): Color for the 'Brownian' bars. Default is '#999999'.
        color_directed (str): Color for the 'Superdiffusive' bars. Default is '#4b2e83'.
        ylim (tuple): y-axis limits. Default is (0, 1).
        legend_loc (str): Location of the legend. Default is 'lower right'.
        legend_fontsize (int): Font size of the legend. Default is 8.
        title_fontsize (int): Font size of the plot title. Default is 15.
        tick_fontsize (int): Font size of the axis ticks. Default is 15.

    Returns:
        matplotlib.figure.Figure: The generated figure.

    """
    fig = plt.figure(figsize=figsize)

    # Calculate the percentage of each diffusion mode
    superdiffusive_percent = ecm[ecm['alpha'] > 1.1].shape[0] / ecm.shape[0]
    brownian_percent = ecm[(ecm['alpha'] <= 1.1) & (ecm['alpha'] >= 0.9)].shape[0] / ecm.shape[0]
    subdiffusive_percent = ecm[ecm['alpha'] < 0.9].shape[0] / ecm.shape[0]

    # Plot the bar chart with customizable parameters
    plt.bar(label_name, subdiffusive_percent, label='Subdiffusive', width=bar_width, color=color_constrained)
    plt.bar(label_name, brownian_percent, bottom=subdiffusive_percent, color=color_normal, label='Brownian', width=bar_width)
    plt.bar(label_name, superdiffusive_percent, bottom=subdiffusive_percent+brownian_percent, color=color_directed,
            label='Superdiffusive', width=bar_width)

    plt.ylim(ylim)
    plt.legend(loc=legend_loc, fontsize=legend_fontsize)
    plt.title('Percentage of Diffusion Modes per Age', fontsize=title_fontsize, fontname='Arial', fontweight='bold')
    plt.xticks(fontsize=tick_fontsize, fontname='Arial', fontweight='bold')
    plt.yticks(fontsize=tick_fontsize, fontname='Arial', fontweight='bold')

    return fig

def plot_diffusion_modes(df, label_column, bar_width=0.5, figsize=(4, 8), color_subdiffusive='#b7a57a',
                         color_brownian='#999999', color_superdiffusive='#4b2e83', ylim=(0, 1),
                         legend_loc='lower right', legend_fontsize=14, title_fontsize=15,
                         title_font='Arial', tick_fontsize=15):
    """
    Plot the percentage of diffusion modes per age category.

    Parameters:
        df (pandas.DataFrame): DataFrame containing diffusion mode data.
        label_column (str): Column name indicating the label.
        bar_width (float): Width of the bars in the bar chart. Default is 0.5.
        figsize (tuple): Figure size (width, height) in inches. Default is (4, 8).
        color_subdiffusive (str): Color for the 'Subdiffusive' bars. Default is '#b7a57a'.
        color_brownian (str): Color for the 'Brownian' bars. Default is '#999999'.
        color_superdiffusive (str): Color for the 'Superdiffusive' bars. Default is '#4b2e83'.
        ylim (tuple): y-axis limits. Default is (0, 1).
        legend_loc (str): Location of the legend. Default is 'lower right'.
        legend_fontsize (int): Font size of the legend. Default is 14.
        title_fontsize (int): Font size of the plot title. Default is 15.
        tick_fontsize (int): Font size of the axis ticks. Default is 15.

    Returns:
        matplotlib.figure.Figure: The generated figure.

    """
    fig = plt.figure(figsize=figsize)


    labels = df[label_column].unique()
    labels.sort()

    superdiffusive_percent = np.zeros(len(labels))
    brownian_percent = np.zeros(len(labels))
    subdiffusive_percent = np.zeros(len(labels))

    for i, unique_class in enumerate(labels):
        print(unique_class)
        ecm = df[df[label_column] == unique_class]

        directed_df = ecm[ecm['alpha'] > 1.1]
        superdiffusive_percent[i] = (len(directed_df)/len(ecm))
        print(superdiffusive_percent[i])

        normal_df = ecm[(ecm['alpha'] <= 1.1) & (ecm['alpha'] >= 0.9)]
        brownian_percent[i] = (len(normal_df)/len(ecm))
        print(brownian_percent[i])
        
        constrained_df = ecm[(ecm['alpha'] < 0.9)]
        subdiffusive_percent[i] = (len(constrained_df)/len(ecm))
        print(subdiffusive_percent[i])
        print()
        
        #immobilized_df = df[(df['alpha'] <= 0.1)]
        #immobilized_percent[i] = (len(immobilized_df)/len(df))
        
        
    #plt.bar(labels, immobilized_percent, color='r', label='immobilized')
    plt.bar(labels, subdiffusive_percent, label='Subdiffusive', width=bar_width, color=color_subdiffusive)
    plt.bar(labels, brownian_percent, bottom=subdiffusive_percent, color=color_brownian, label='Brownian', width=bar_width)
    plt.bar(labels, superdiffusive_percent, bottom=subdiffusive_percent+brownian_percent, color=color_superdiffusive, label='Superdiffusive', width=bar_width)
    plt.ylim(ylim)
    plt.legend(loc=legend_loc, fontsize=legend_fontsize)
    plt.title(f'Percentage of Diffusion Modes per {label_column}', fontsize=title_fontsize, fontname=title_font, fontweight='bold')
    plt.ylim([0,1])
    plt.xticks(fontsize=tick_fontsize, fontname='Arial', fontweight='bold')
    plt.yticks(fontsize=tick_fontsize, fontname='Arial', fontweight='bold')

    return fig
