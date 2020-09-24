import pandas as pd
import numpy as np
import sklearn
import acquire
import prepare
from acquire import get_titanic_data
from acquire import get_telco_data


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def wrangle_telco():
    df = prepare.prep_telco()
    df = df[['monthly_charges','tenure','Two year']]
    df = df[df['Two year'] == 1]
    df['total_charges'] = df['monthly_charges'] * df['tenure']
    
    return df