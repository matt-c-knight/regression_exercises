import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import env
import wrangle
import split_scale


def plot_variable_pairs(df):
    g = sns.PairGrid(df)
    g.map_diag(sns.distplot)
    g.map_offdiag(sns.regplot)

def months_to_years(tenure_months, df):
    df['tenure_years'] = tenure_months / 12
    return df

def plot_categorical_and_continuous_vars(categorical_var, continuous_var, df):
        plt.rc('figure', figsize=(20, 12))
       
        sns.boxplot(data=df, y=continuous_var, x=categorical_var)
        plt.show()
        sns.barplot(data=df, y=continuous_var, x=categorical_var)
        plt.show()
        sns.swarmplot(data=df, y=continuous_var, x=categorical_var)
        plt.show()
