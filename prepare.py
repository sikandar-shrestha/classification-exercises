
from sklearn.model_selection import train_test_split

def prep_iris(df):
    """
    this function will clean the iris Data whether it acquired from
    sql database or cvs file from your local drive of the machine.
    
    """
    # Clean up the column names - replace the period 
    # with an underscore and lowercase.


    df.columns=df.columns.str.replace('.','_').str.lower()
    
    # Drop the species_id and measurement_id columns.
    df=df.drop(columns=['species_id','measurement_id'])
    
    # Rename the species_name column to just species.
    df=df.rename(columns={'species_name':'species'})
    
    return df  






def prep_titanic(df):
    """
    This is a function that accepts the acquired titanic data, and returns the data with the transformations
    by cleaning data.
    
    """
    #drop unncessary columns
    df = df.drop(columns=['embarked', 'age','deck', 'class'])
    
    #made this a string so its categorical
    df.pclass = df.pclass.astype(object)
    
    #filled NaN with the mode
    df.embark_town = df.embark_town.fillna('Southampton')
    
    return df
    
    
    

    
    
def prep_telco(df):
    
    
    """
    function named prep_telco that accepts the raw telco data, 
    and returns the data with the transformations.

    """
    # Drop any unnecessary, unhelpful, or duplicated columns.
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    df['total_charges']=df['total_charges'].astype('float')
    return df


    

    
def splitting_data(df,target):

            # 1st split
            #this is return two dataframes
            train,validate_test=train_test_split(df, #send in initial df
                 train_size=0.60, #size of the train df, and the test size will default to 1-train_size
                random_state=123, #set any number here for consistency
                 stratify=df[target] #need to stratify on target variable
                ) 
            
            
            
            # 2nd split
            validate,test=train_test_split(validate_test,
                                           train_size=0.5,
                                           random_state=123,
                                           stratify=validate_test[target]
                                          )
            
            
            return train, validate, test
        
        
        
        
        
        
        
        
        