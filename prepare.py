import pandas as pd
import numpy as np

def prep_iris(df):
    df = df.drop(columns='species_id').rename(columns={'species_name': 'species'})
    #species_as_dummies = pd.get_dummies(df.species, drop_first=True)
    #df = pd.concat([df, species_as_dummies], axis=1)
    return df

def prep_titanic(df):
    '''
    takes in a dataframe of the titanic dataset as it is acquired and returns a cleaned dataframe
    arguments: df: a pandas DataFrame with the expected feature names and columns
    return: clean_df: a dataframe with the cleaning operations performed on it
    '''
    # drop any duplicate rows
    df = df.drop_duplicates()
    # drop columns we want to remove
    df = df.drop(columns=['deck', 'embarked', 'class', 'age', 'passenger_id'])
    # fill missing values
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    # encode categorical variables
    df_dummies = pd.get_dummies(df[['embark_town', 'sex']], dummy_na=False, drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.rename(columns={'embark_town_Queenstown': 'Queenstown', 'embark_town_Southampton': 'Southampton', 'sex_male': 'male'})
    # df = df.drop(columns=['sex', 'embark_town'])
    return df.drop(columns=['sex', 'embark_town'])


def prep_telco(df):
    # drop unnecessary, unhelpful, or duplicate columns. 
    df = df.drop(columns=['customer_id', 'payment_type_id', 'internet_service_type_id',
                                'contract_type_id', 'total_charges', 'tech_support', 'streaming_tv',
                                'streaming_movies', 'online_backup', 'online_security'])
    # Encode the categorical variables. 
    df['is_male'] = np.where(df.gender == 'Male', 1, 0)
    df['has_partner'] = np.where(df.partner == 'Yes', 1, 0)
    df['has_dependent'] = np.where(df.dependents == 'Yes', 1, 0)
    df['has_phone'] = np.where(df.phone_service == 'Yes', 1, 0)
    df['multiple_lines'] = np.where(df.multiple_lines == 'Yes', 1, 0)
    df['has_internet'] = np.where(df.internet_service_type == "None", 0, 1)
    df['fiber'] = np.where(df.internet_service_type == "Fiber optic", 1, 0)
    df['no_contract'] = np.where(df.contract_type == "Month-to-month", 1, 0)
    df['electronic_check'] = np.where(df.payment_type == "Electronic check", 1, 0)
    df['paperless_billing'] = np.where(df.paperless_billing == 'Yes', 1, 0)
    df['autopay'] = np.where(df.payment_type.str.contains('automatic') == True, 1, 0)
    df['churn'] = np.where(df.churn == 'Yes', 1, 0)
    # drop redundant, categorical variables. 
    df = df.drop(columns=['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines',
                                'internet_service_type', 'contract_type', 'payment_type', 'paperless_billing',
                                'churn', 'device_protection'])
    return df 