
import pandas as pd
import numpy as np
import os
from env import host, user, password

###################### Acquire Titanic Data ######################

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
def get_db():
    df = pd.read_sql('''SELECT *
    FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id);''', get_connection("telco_churn"))
    return df