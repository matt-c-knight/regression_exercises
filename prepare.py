import pandas as pd
import numpy as np
import sklearn
import acquire
from acquire import get_titanic_data
from acquire import get_telco_data


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

############ Mall data #####################

def prep_mall_data(df):
    df['is_female'] = (df.gender == 'Female').astype('int')
    train_and_validate, test = train_test_split(df, test_size=.15, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size=.15, random_state=123)
    return train, test, validate

    ##################################

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

def telco_split(df):

    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123,
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3,
                                        random_state=123,
                                        stratify=train_validate.churn)
    return train, validate, test


def prep_telco(cached=True):

    df = get_telco_data(cached)
    df = df.drop(columns=['customer_id', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'internet_service_type_id', 'contract_type_id', 'payment_type_id', 'partner', 'dependents', 'multiple_lines', 'streaming_tv', 'streaming_movies', 'total_charges'])
    df_dummies = pd.get_dummies(df.contract_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='contract_type')
    df_dummies = pd.get_dummies(df.internet_service_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='internet_service_type')
    df_dummies = pd.get_dummies(df.payment_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='payment_type')
    df.loc[df['phone_service'] == 'No', 'phone_service'] = 0
    df.loc[df['phone_service'] == 'Yes', 'phone_service'] = 1
    df.loc[df['paperless_billing'] == 'No', 'paperless_billing'] = 0
    df.loc[df['paperless_billing'] == 'Yes', 'paperless_billing'] = 1
    df.loc[df['churn'] == 'No', 'churn'] = 0
    df.loc[df['churn'] == 'Yes', 'churn'] = 1
    df_dummies = pd.get_dummies(df.gender)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='gender')
    df['phone_service'] = df.phone_service.astype('int')
    df['paperless_billing'] = df.paperless_billing.astype('int')
    df['churn'] = df.churn.astype('int')
    
    return df