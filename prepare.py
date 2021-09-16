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

def prep_work(df):
    """ This function, drops nulls, renames the columns to something more clear to understand, corrects datatypes, get's rid of 
    unneeded decimals, reassigns proper dataypes, and drops duplicates."""
    #dropping null values
    df = df.dropna()
    # now lets rename columns
    df = df.rename(columns={
                            'parcelid': 'parcel_id',
                            'calculatedfinishedsquarefeet': 'sqft',
                            'bathroomcnt': 'baths',
                            'bedroomcnt': 'beds',
                            'assessmentyear': 'assessment_year',
                            'regionidcounty': 'county',
                            'regionidzip': 'zipcode',
                            'transactiondate': 'tranaction_date',
                            'taxvaluedollarcnt':'tax_value'})
    # change datatypes to int beds,tax_value 
    df['beds'] = df['beds'].astype(int)
    # calculate the tax rate and make a new column/feature 
    df['tax_rate']= df['taxamount']/df['tax_value']
    # let's get rid of the unnecessary decimal point
    df['beds','sqft','tax_value','assessment_year','county','zipcode'] =          df['beds','sqft','tax_value','assessment_year','county','zipcode'].astype(str).apply(lambda x: x.replace('.0',''))
    df['sqft'] = df['sqft'].astype(str).apply(lambda x: x.replace('.0',''))
    df['tax_value'] = df['tax_value'].astype(str).apply(lambda x: x.replace('.0',''))
    df['assessment_year'] = df['assessment_year'].astype(str).apply(lambda x: x.replace('.0',''))
    df['county'] = df['county'].astype(str).apply(lambda x: x.replace('.0',''))
    df['zipcode'] = df['zipcode'].astype(str).apply(lambda x: x.replace('.0',''))
    # now lets convert these back to the correct datatype
    df.parcel_id = df.parcel_id.astype(object)
    df.beds = df.beds.astype(int)
    df.taxamount = df.taxamount.astype(int)
    df.sqft = df.sqft.astype(float, copy=False)
    # dropping ALL duplicate values
    df.drop_duplicates(subset ="parcel_id",keep = False, inplace = True)
    return df

def train_validate_test(df, target):
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
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

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


# def remove_outlier(df):
#     '''
#     This function will remove values that are 3 standard deviations above or below the mean for sqft, baths, beds, and tax_value.         (Our MVP values)
#     '''
#     new_df = df[(np.abs(stats.zscore(df['sqft'])) < 3)]
#     new_df = df[(np.abs(stats.zscore(df['baths'])) < 3)]
#     new_df = df[(np.abs(stats.zscore(df['beds'])) < 3)]
#     new_df = df[(np.abs(stats.zscore(df['tax_value'])) < 3)]
#     return new_df




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
# plt.hist(x_train, bins=25, ec='black')
# plt.title('Original')
# plt.subplot(122)
# plt.hist(x_train_scaled, bins=25, ec='black')
# plt.title('Scaled')