from scipy import stats
import pandas as pd

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

 #########################################################################

def get_metrics_binary(clf):
     
    #get_metrics_binary takes in a confusion matrix (cnf) for a binary classifier and prints out metrics based on
    #values in variables named X_train, y_train, and y_pred.
    
    #return: a classification report as a transposed DataFrame
    
    accuracy = clf.score(X_train, y_train)
    class_report = pd.DataFrame(classification_report(y_train, y_pred, output_dict=True)).T
    conf = confusion_matrix(y_train, y_pred)
    tpr = conf[1][1] / conf[1].sum()
    fpr = conf[0][1] / conf[0].sum()
    tnr = conf[0][0] / conf[0].sum()
    fnr = conf[1][0] / conf[1].sum()
    print(f'''
    The accuracy for our model is {accuracy:.4}
    The True Positive Rate is {tpr:.3}, The False Positive Rate is {fpr:.3},
    The True Negative Rate is {tnr:.3}, and the False Negative Rate is {fnr:.3}
    ''')
    return class_report

#remove currency 
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)


## CHI-SQUARED TEST FUNCTION

def chi2_test(data_for_category1, data_for_category2, alpha=.05):

    '''
    Given two subgroups from a dataset, conducts a chi-squared test for independence and outputs 
    the relevant information to the console. 
    Utilizes the method provided in the Codeup curriculum for conducting chi-squared test using
    scipy and pandas. 
    '''
    
    # create dataframe of observed values
    observed = pd.crosstab(data_for_category1, data_for_category2)
    
    # conduct test using scipy.stats.chi2_contingency() test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # round the expected values
    expected = expected.round(1)
    
    # output
    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    
    # evaluate the hypothesis against the established alpha value
    evaluate_hypothesis(p, alpha)

# PEARSONR CORRELATION TEST FUNCTION

def correlation_test(data_for_category1, data_for_category2, alpha = 0.05):
    '''
    Given two subgroups from a dataset, conducts a correlation test for linear relationship and outputs 
    the relevant information to the console. 
    Utilizes the method provided in the Codeup curriculum for conducting correlation test using
    scipy and pandas. 
    '''

    # conduct test using scipy.stats.peasonr() test
    r, p = stats.pearsonr(data_for_category1, data_for_category2)

    # output
    print(f'r = {r:.4f}')
    print(f'p = {p:.4f}')

    # evaluate the hypothesis against the established alpha value
    evaluate_hypothesis(p, alpha)

def equal_var_test(*args, alpha: float = 0.05) -> bool:
    '''
    Given two or more subgroups from a dataset, conducts a test of equal variance and returns whether or
    not p is less than alpha.
    '''

    f, p = stats.levene(*args)
    return evaluate_hypothesis(p, alpha, output = False)

def central_limit_theorem_test(*args, n_clt: int = 30) -> bool:
    '''
    Given two or more subgroups from a dataset, determines whether or not we have large enough sample
    sizes to use the central limit theorem to assume normal distribution.
    '''

    sample_sizes = [arg.size for arg in args]
    return min(sample_sizes) >= n_clt