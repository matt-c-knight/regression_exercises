import pandas as pd
import numpy as np

import wrangle
import env
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler


def split_my_data(df):
   train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123,
                                        stratify= df.tenure)
   train, validate = train_test_split(train_validate, test_size=.3,
                                        random_state=123,
                                        stratify= train_validate.tenure)
   
   return train, validate, test

def standard_scaler(x):
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True)\
            .fit(x)
    return scaler

# def scale_inverse():

def uniform_scaler(train, test):
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled

def gaussian_scaler(train, test):
    scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, test_scaled

def min_max_scaler(train, test):
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, test_scaled

# def iqr_robust_scaler():

