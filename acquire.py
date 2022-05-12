#               _        ___      ____      _  _     __     ___       ____                #
#              /.\     ,"___".   F __ ]    FJ  L]    FJ    F _ ",    F ___J               #
#             //_\\    FJ---L]  J |--| L  J |  | L  J  L  J `-'(|   J |___:               #
#            / ___ \  J |   LJ  | | _| |  | |  | |  |  |  |  _  L   | _____|              #
#           / L___J \ | \___--. F L_F  J  F L__J J  F  J  F |_\  L  F L____:              #
#          J__L   J__LJ\_____/FJ\_____  \J\______/FJ____LJ__| \\__LJ________L             #
#          |__L   J__| J_____F  J_____\J] J______F |____||__|  J__||________|             #  
#|---------------------------------------------------------------------------------------|#                     #|---------------------------------------------------------------------------------------|#
#  IMPORTS
from env import host, username, password, get_db_url
import os
import pandas as pd 
#|---------------------------------------------------------------------------------------|#
#|---------------------------------------------------------------------------------------|#
# 1.) Make a function named get_titanic_data that returns the titanic data from the codeup
# data science database as a pandas data frame.

def get_titanic_data(use_cache=True):
    '''
    INSPECTS OPERATING SYSTEM TO FIND CSV OF TITANIC DATA
    IF UNDETECTED, READS A QUERY THROUGH UDF AND READ_SQL
    CREATES CSV AND RETURNS THE DATAFRAME
    '''
    # check if the indicated csv string exists
    if os.path.exists('titanic.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('titanic.csv')
    print('Acquiring data from SQL database')    
    # read the SQL query into a dataframe
    df = pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))
    # Write that dataframe to disk for later; Called "caching".
    df.to_csv('titanic.csv', index=False)
    # Return the dataframe to the calling code
    return df  
#|---------------------------------------------------------------------------------------|#
# 2.) Make a function named get_iris_data that returns the data from the iris_db on the
# codeup data science database as a pandas data frame. The returned data frame should
# include the actual name of the species in addition to the species_ids.

def get_iris_data(use_cache=True):
    '''
    INSPECTS OPERATING SYSTEM TO FIND CSV OF IRIS DATA
    IF UNDETECTED, READS A QUERY THROUGH UDF AND READ_SQL
    CREATES CSV AND RETURNS THE DATAFRAME
    '''
    if os.path.exists('iris.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('iris.csv')
    print('Acquiring data from SQL database')
    # read the SQL query into a dataframe
    df = pd.read_sql('''
                    SELECT *
                    FROM measurements
                    JOIN species USING(species_id)
                    '''
            , get_db_url('iris_db'))

    # Cache the Dataframe
    df.to_csv('iris.csv', index=False)

    # Return the dataframe to the calling code
    return df  
#|---------------------------------------------------------------------------------------|#
# 3.) Make a function named get_telco_data that returns the data from the telco_churn
#.    database in SQL. In your SQL, be sure to join all 4 tables together, so that the
#.    resulting dataframe contains all the contract, payment, & internet service options.

def get_telco_data(use_cache=True):
    '''
    INSPECTS OPERATING SYSTEM TO FIND CSV OF TELCO DATA
    IF UNDETECTED, READS A QUERY THROUGH UDF AND READ_SQL
    CREATES CSV AND RETURNS THE DATAFRAME
    '''
    if os.path.exists('telco.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('telco.csv')
    print('Acquiring data from SQL database')
    df = pd.read_sql('''   
                    SELECT * 
                        FROM customers
                        JOIN contract_types USING(contract_type_id)
                        JOIN internet_service_types USING(internet_service_type_id)
                        JOIN payment_types USING(payment_type_id)
                    '''
            , get_db_url('telco_churn'))
    
    df.to_csv('telco.csv', index=False)
    
    return df
#|---------------------------------------------------------------------------------------|#
#|---------------------------------------------------------------------------------------|#