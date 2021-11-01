import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
from scipy import stats
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import env
np.random.seed(123)

def prep_zillow_data(df):
    ''' This function preps the data by dropping rows with nulls, correcting datatypes, renaming the columns for better understanding,, 
    drops rows with erroneous entries, drops duplicates, and creates a tax_rate column
     '''
    # Compared to the row count we have more than enough to drop these
    df = df.dropna()
    # Next we can correct data types that are wrong
    df.parcelid = df.parcelid.astype('object')
    df.regionidcounty = df.regionidcounty.astype('object')
    df.regionidzip = df.regionidzip.astype('object')
    df.fips = df.fips.astype('object')
    df.taxvaluedollarcnt, df.assessmentyear = df.taxvaluedollarcnt.astype('int64'), df.assessmentyear.astype('int64')   
    # Next I will rename the columns to be more recognizable
    df = df.rename(columns={"bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms","calculatedfinishedsquarefeet": "area","taxamount": "tax_amount", "taxvaluedollarcnt": "tax_value", "fips": "zipcode", "regionidcounty": "county_id","assessmentyear": "assessment_year", "transactiondate":"transaction_date" })
    # Here I check for erroneous entries and drop them
    df.drop(df[df['bedrooms'] < 1].index, inplace = True)
    df.drop(df[df['bathrooms'] < 1].index, inplace = True)
    df.drop(df[df['area'] < 200].index, inplace = True)
    # calculate the tax rate and make a new column/feature 
    df['tax_rate']= df['tax_amount']/df['tax_value']
    # time to check for duplicates and remove them
    # dropping ALL duplicate values
    df.drop_duplicates(subset ="parcelid",
                         keep = False, inplace = True)
    # calculate the tax rate and make a new column/feature 
    df['tax_rate']= df['tax_amount']/df['tax_value']
    return df

def train_validate_test(df2, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns train, validate, test sets and also another 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df2, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test


def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

# def scale_dataset(train, validate, test):
#     #applying the robust scaler
#     scaler = sklearn.preprocessing.RobustScaler()
#     # Note that we only call .fit with the training data,
#     # but we use .transform to apply the scaling to all the data splits.
#     scaler.fit(x_train)

#     x_train_scaled = scaler.transform(x_train)
#     x_validate_scaled = scaler.transform(x_validate)
#     x_test_scaled = scaler.transform(x_test)
#     return x_train_scaled, x_validate_scaled, x_test_scaled

# plt.figure(figsize=(13, 6))
# plt.subplot(121)
# plt.hist(X_train, bins=25, ec='black')
# plt.title('Original')
# plt.subplot(122)
# plt.hist(X_train_scaled, bins=25, ec='black')
# plt.title('Scaled')