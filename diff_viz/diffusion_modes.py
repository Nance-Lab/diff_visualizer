"""
Functions for plotting diffusion modes of nanoparticle trajecories from MPT data
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_diffusion_modes_single_file(ecm):
    fig = plt.figure(figsize=(1,4))

    labels = ['File']

    directed_percent = ecm[ecm['alpha'] > 1.1].shape[0] / ecm.shape[0]
    normal_percent = ecm[(ecm['alpha'] <= 1.1) & (ecm['alpha'] >= 0.9)].shape[0] / ecm.shape[0]
    constrained_percent = ecm[ecm['alpha'] < 0.9].shape[0] / ecm.shape[0]

    bar_w = 0.01
    plt.bar(labels, constrained_percent, label='Subdiffusive', width=bar_w, color='#b7a57a')
    plt.bar(labels, normal_percent, bottom=constrained_percent, color='#999999', label='Brownian', width=bar_w)
    plt.bar(labels, directed_percent, bottom=constrained_percent+normal_percent, color='#4b2e83', label='Superdiffusive', width=bar_w)
    plt.ylim([0,1])
    plt.legend(loc='lower right', fontsize=8)
    plt.title('Percentage of Diffusion Modes per Age', fontsize=15, fontname='Arial', fontweight='bold')
    plt.ylim([0,1])
    plt.xticks(fontsize=15, fontname='Arial', fontweight='bold')
    plt.yticks(fontsize=15, fontname='Arial', fontweight='bold')
    return fig
