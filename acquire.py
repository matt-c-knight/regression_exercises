from env import host, user, password

import pandas as pd
import numpy as np
import os

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


################ Acquire Mall Customers Data ###################
def new_mall_data():
    '''
    This function reads the mall customer data from the Codeup db into a df, write
    it to a csv file, and returns the df.
    '''
    sql_query = 'SELECT * FROM customers'
    df = pd.read_sql(sql_query, get_connection('mall_customers'))
    df.to_csv('mall_customers_df.csv')
    return df

def get_mall_data(cached=False):
    '''
    This function reads in mall customer data from Codeup database if cached == False
    or if cached == True reads in mall customer df from a csv file, returns df
    '''
    if cached or os.path.isfile('mall_customers_df.csv') == False:
        df = new_mall_data()
    else:
        df = pd.read_csv('mall_customers_df.csv', index_col=0)
    return df
################### 
def new_titanic_data():
    sql_query = 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    df.to_csv('titanic_df.csv')
    return df

def get_titanic_data(cached=False):
    if cached or os.path.isfile('titanic_df.csv') == False:
        df = new_titanic_data()
    else:
        df = pd.read_csv('titanic_df.csv', index_col=0)
    return df

def new_iris_data():
    sql_query = """
                SELECT species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species
                USING(species_id)
                """
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    df.to_csv('iris_df.csv')
    return df

def get_iris_data(cached=False):
    if cached or os.path.isfile('iris_df.csv') == False:
        df = new_iris_data()
    else:
        df = pd.read_csv('iris_df.csv', index_col=0)
    return df

def new_telco_data():
    sql_query = 'SELECT customers.*, contract_types.contract_type, internet_service_types.internet_service_type, payment_types.payment_type FROM customers JOIN contract_types using(contract_type_id) JOIN internet_service_types using(internet_service_type_id) JOIN payment_types using(payment_type_id) '
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco_churn_df.csv')
    return df

def get_telco_data(cached=False):
    if cached or os.path.isfile('telco_churn_df.csv') == False:
        df = new_telco_data()
    else:
        df = pd.read_csv('telco_churn_df.csv', index_col=0)
    return df