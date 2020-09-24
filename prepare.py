import pandas as pd
import numpy as np
import sklearn
from acquire import get_titanic_data



from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def iris_split(df):

    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123,
                                        stratify=df.species)
    train, validate = train_test_split(train_validate, test_size=.3,
                                        random_state=123,
                                        stratify=train_validate.species)
    return train, validate, test


def titanic_split(df):

    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123,
                                        stratify=df.survived)
    train, validate = train_test_split(train_validate, test_size=.3,
                                        random_state=123,
                                        stratify=train_validate.survived)
    return train, validate, test

def impute_mean_age(train, validate, test):

    imputer = SimpleImputer(strategy = 'mean')

    train['age'] = imputer.fit_transform(train[['age']])

    validate['age'] = imputer.transform(validate[['age']])

    test['age'] = imputer.transform(test[['age']])

    return train, validate, test

def prep_titanic(cached=True):
    df = get_titanic_data(cached)
    df = df[~df.embarked.isnull()]
    titanic_dummies = pd.get_dummies(df.embarked, drop_first=True)
    df = pd.concat([df, titanic_dummies], axis=1)
    df = df.drop(columns='deck')

    train, validate, test = titanic_split(df)

    train, validate, test = impute_mean_age(train, validate, test)

    return train, validate, test