"""
Functions for plotting diffusion modes of nanoparticle trajecories from MPT data
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_diffusion_modes(ecm, target):
    fig = plt.figure(figsize=(4,8))

    labels = ecm[target].unique()
    labels.sort()

    alpha = ecm['alpha']
    directed_percent = ((alpha > 1.1).groupby(ecm[target]).mean())
    normal_percent = (((alpha <= 1.1) & (alpha >= 0.9)).groupby(ecm[target]).mean())
    constrained_percent = ((alpha < 0.9).groupby(ecm[target]).mean())

    bar_w = 0.5
    plt.bar(labels, constrained_percent, label='Subdiffusive', width=bar_w, color='#b7a57a')
    plt.bar(labels, normal_percent, bottom=constrained_percent, color='#999999', label='Brownian', width=bar_w)
    plt.bar(labels, directed_percent, bottom=constrained_percent+normal_percent, color='#4b2e83', label='Superdiffusive', width=bar_w)
    plt.ylim([0,1])
    plt.legend(loc='lower right', fontsize=14)
    plt.title('Percentage of Diffusion Modes per Age', fontsize=15, fontname='Arial', fontweight='bold')
    plt.ylim([0,1])
    plt.xticks(fontsize=15, fontname='Arial', fontweight='bold')
    plt.yticks(fontsize=15, fontname='Arial', fontweight='bold')
