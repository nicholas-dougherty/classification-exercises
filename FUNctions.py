def describe_data(df):
    print('The first three rows are: ')
    print('----------------------------------------------------------')
    print(df.head(3))
    print('----------------------------------------------------------')
    print("The data frame's shape is: ")
    print('-------------------------')
    print(df.shape)
    print('-------------------------')   
    print('The data types and column names are: ')
    print(sorted(df))
    print(df.info())
    print('----------------------------------------------------------')   
    print('The summary statistics are as follows: ')
    print('----------------------------------------------------------')
    print(df.describe())
    print('----------------------------------------------------------')      
    print(f'The number of NA\'s is:')
    print('-------------------------')
    print(df.isna().sum())
    print('-------------------------')
    print('----------------------------------------------------------')  
    print('Unique Values for the Columns:')
    print('-------------------------')
    limit = 10
    for col in df.columns:
        if df[col].nunique() < limit:
            print(f'Column: {col}')
            print(f'Unique Values: {df[col].unique()}')
        else: 
            print(f'Column: {col}')
            print(f'Range of Values: [{df[col].min()} - {df[col].max()}]')
        print('-----------------------')
    print('-------Done-zo-------------')

##############################################################################################

def display_uniques(df, n_unique_limit=10):
    '''
    This function takes in a dataframe and displays the unique values for each column in the form of a pandas 
    dataframe. Intended to display unique values for categorical variables. 
    
    n_unique_limit - default 10 - establishes the max number contained in the columns we want to display
    '''
    # create empty df
    newdf = pd.DataFrame()
    
    # for each column in the df
    for col in df.columns:
        # create a column in the new df that contains only the unique values from that column in the original df
        newdf[col] = pd.Series(df[col].unique())
    
    # drop all columns that have a number of unique values that is greater than our established limit
    newdf = newdf.drop(columns=newdf.columns[newdf.count() > n_unique_limit])
    
    # truncate the dataframe to the appropriate number of rows
    newdf = newdf.head(newdf.count().max())
    
    # fill nulls with empty strings for a cleaner display
    newdf = newdf.fillna('')
    
    return newdf