
import pandas as pd
import numpy as np
import os
from env import host, user, password

# Acquire Zillow Data

#this url takes you to the zillow database
url = f"mysql+pymysql://{user}:{password}@{host}/zillow"

#this query brings in all the columns necessary to ask the questions posed by the zillow team narrowing down the database to single unit properties with transactions during May-Aug 2017. 
query = """
            
SELECT parcelid, bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, taxamount, assessmentyear, regionidcounty,regionidzip, fips, transactiondate
FROM properties_2017

LEFT JOIN propertylandusetype USING(propertylandusetypeid)

JOIN predictions_2017 USING(parcelid)

WHERE propertylandusedesc IN ("Single Family Residential",                       
                              "Inferred Single Family Residential")
                              AND (transactiondate BETWEEN '2017-05-01' AND '2017-08-31');
                              
                              """

