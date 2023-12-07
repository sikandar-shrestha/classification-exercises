import pandas as pd



def preprocess_titanic(train_df, val_df, test_df):
    '''
    preprocess_titanic will take in three pandas dataframes
    of our titanic data, expected as cleaned versions of this 
    titanic data set (see documentation on acquire.py and prepare.py)
    
    output:
    encoded, ML-ready versions of our clean data, with 
    columns sex and embark_town encoded in the one-hot fashion
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
    # with a looping structure:
    # for df in [train_df, val_df, test_df]:
    #     df.drop(blah blah blah)
    #     df['pclass'] = df['pclass'].astype(int)
    train_df = train_df.drop(columns='passenger_id')
    train_df['pclass'] = train_df['pclass'].astype(int)
    val_df = val_df.drop(columns='passenger_id')
    val_df['pclass'] = val_df['pclass'].astype(int)
    test_df = test_df.drop(columns='passenger_id')
    test_df['pclass'] = test_df['pclass'].astype(int)
    encoding_var = ['sex', 'embark_town']
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(df[['embark_town', 'sex']],drop_first=True).astype(int)
        encoded_dfs.append(pd.concat([df,df_encoded_cats],axis=1).drop(columns=['sex', 'embark_town']))
    
    return encoded_dfs




def preprocess_telco(train_df, val_df, test_df):
    '''
    preprocess_telco will take in three pandas dataframes
    of an acquired and prepared telco data set that has also been split into train, validate, and test.
    
    output:
    encoded, ML-ready versions of train, validate, and test with 
    object type colummncs encoded in the one-hot fashion
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
     
    encoding_vars = []
    # loop through the columns to fill encoded_vars with appropriate datatype 
    for col in train_df.columns:
        if train_df[col].dtype == 'O':
            encoding_vars.append(col)
    # initialize an empty list to hold our encoded dataframes:
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(df[encoding_vars],drop_first=True).astype(int)
        encoded_dfs.append(pd.concat([df,df_encoded_cats],axis=1).drop(columns=encoding_vars))
    return encoded_dfs





  ############################################ for only one input (either train or validate or test df ################

#def preprocess_titanic(df):
    
    #  Encoding categorical columns for original dataframe
 #   dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first=[True, True]).astype(int)
    # Concatenate the dummy_df  with df dataframe
  #  df = pd.concat([df,dummy_df], axis=1)
    # Drop string values that have been replaced with encoded values
   # df = df.drop(columns=['sex','embark_town'])
    

    #return df





#def preprocess_telco(df):
    
    # drop customer_id
    #df=df.drop(columns='customer_id')
    
    # Encode by using replace()

#    df.loc[:, 'is_female'] = df['gender'].replace({'Female': 1, 'Male': 0})
#    df=df.drop(columns='gender')

    # encode by using map()
#    df.loc[:, 'has_partner'] = df['partner'].map({'Yes': 1, 'No': 0})
 #   df=df.drop(columns='partner')
    # encode by using get_dummies()
    
 #   encoded_cols=['dependents','phone_service','multiple_lines','online_security','online_backup',\
 #                                     'device_protection','tech_support','streaming_tv','streaming_movies',\
  #                             'paperless_billing','churn','contract_type','internet_service_type','payment_type']

    # Encoding categorical columns for original dataframe
 #   dummy_train = pd.get_dummies(df[encoded_cols], dummy_na=False, drop_first=[True, True]).astype(int)
    # Concatenate the dummy_df  with df dataframe
  #  df = pd.concat([df,dummy_train], axis=1)
    # Drop string values that have been replaced with encoded values
  #  df = df.drop(columns=encoded_cols)

 #   return df
    
   
