import pandas as pd


def preprocess_titanic(df):
    
    #  Encoding categorical columns for original dataframe
    dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first=[True, True]).astype(int)
    # Concatenate the dummy_df  with df dataframe
    df = pd.concat([df,dummy_df], axis=1)
    # Drop string values that have been replaced with encoded values
    df = df.drop(columns=['sex','embark_town'])
    

    return df





def preprocess_telco(df):
    
    # Encode by using replace()

    df.loc[:, 'is_female'] = df['gender'].replace({'Female': 1, 'Male': 0})
    df=df.drop(columns='gender')

    # encode by using map()
    df.loc[:, 'has_partner'] = df['partner'].map({'Yes': 1, 'No': 0})
    df=df.drop(columns='partner')
    # encode by using get_dummies()
    
    encoded_cols=['dependents','phone_service','multiple_lines','online_security','online_backup',\
                                      'device_protection','tech_support','streaming_tv','streaming_movies',\
                               'paperless_billing','churn','contract_type','internet_service_type','payment_type']

    # Encoding categorical columns for original dataframe
    dummy_train = pd.get_dummies(df[encoded_cols], dummy_na=False, drop_first=[True, True]).astype(int)
    # Concatenate the dummy_df  with df dataframe
    df = pd.concat([df,dummy_train], axis=1)
    # Drop string values that have been replaced with encoded values
    df = df.drop(columns=encoded_cols)

    return df
