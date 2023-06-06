import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def feature_violin_plot(df, feature_to_plot, label_column):
    """_summary_

    Args:
        df (_type_): _description_
        feature_to_plot (_type_): _description_
        label_column (_type_): _description_

    Returns:
        _type_: _description_
    """
    df = df[df[feature_to_plot]<10] #temporary fix for outliers
    fig = plt.figure(figsize=(2,2))
    sns.violinplot(x=label_column, y=feature_to_plot, data=df)
    return fig
