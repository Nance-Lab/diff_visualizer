import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def feature_violin_plot(df, feature_to_plot, label_column):
    df = df[df[feature_to_plot]<10] #temporary fix for outliers
    fig = plt.figure(figsize=(2,2))
    sns.violinplot(x=label_column, y=feature_to_plot, data=df)
    return fig
