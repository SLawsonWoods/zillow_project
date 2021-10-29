# zillow_project

A project determining drivers of home value in 2017.


Project Summary

____________________________________________________________________________________
**Project Objectives**
Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
Answer the questions posed by the team in my notebook and in the slide deck.
Create modules (acquire.py, prepare.py) that make your process repeateable.
Construct a model to predict home value for single unit properties with a transaction date of May-August 2017 using regression techniques.
Deliver a 5 minute presentation consisting of a slide-deck with my target audience being the Zillow data science team.

____________________________________________________________________________________
**Business Goals**
Find drivers for housing prices in Los Angeles, Ventura and Orange County during the months May through August 2017. What elements are driving the price?
Construct a ML regression model that performs better than the baseline model.
Document the process well enough to be presented or read like a report.

____________________________________________________________________________________
**Audience**

The Zillow data science team.

____________________________________________________________________________________
**Project Deliverables**

A presentation supported by slides.
A gihub repo containing my work
A .py file for aquiring and preparing the data.
A .env file
A README.md file
Project PlanningDoc: https://docs.google.com/document/d/1hjgosd8O4rzJlSBqq0HhEKQgg98yRmq0P9Cne1cWMc4/edit?usp=sharing

____________________________________________________________________________________
**Project Context**

The dataset I am using comes from the Codeup database.

____________________________________________________________________________________
**Data Dictionary

Feature                             Description

'assessmentyear':                   The year of the property tax assessment 
'bathroomcnt':                      Number of bathrooms in home including fractional bathrooms
'bedroomcnt':                       Number of bedrooms in home 
'calculatedfinishedsquarefeet':     Calculated total finished living area of the home 
'parcelid':                         Unique identifier for parcels (lots) 
'regionidcounty':                   County in which the property is located
'regionidzip':                      Zip code in which the property is located
'taxamount':                        The total property tax assessed for that assessment year
'taxvaluedollarcnt':                The total tax assessed value of the parcel

**Data Dictionary**




| Feature               | Datatype               | Description                                   |
|:----------------------|:-----------------------|:----------------------------------------------|
| Loan_ID               | 1311 non-null: int64   | Unique Loan ID                                |
| Gender                | 1311 non-null: object  | Male/ Female                                  |
| Married               | 1304 non-null: object  | Applicant married (Y/N)                       |
| Dependents            | 1310 non-null: object  | Number of dependents                          |
| Education             | 955 non-null: object   | Applicant Education (Graduate/ Under-Graduate)|
| Self_Employed         | 270 non-null: object   | Applicant income                              |
| ApplicantIncome       | 311 non-null: int64    | Mill where the beans were processed           |       | CoapplicantIncome     | 1311 non-null: int64   | Coapplicant income                            |
| Credit History        | 1165 non-null: object  | Credit history meets guidelines               |
| LoanAmount            | 1311 non-null: int64   | Loan amount in thousands                      |
| Loan_Amount_Term      | 1311 non-null: int64   | Term of loan in months                        |       
| Property_Area         | 1088 non-null: object  | Urban/ Semi Urban/ Rural                      |
| Loan_Status           | 1254 non-null: object  | Loan approved (Y/N)                           |

____________________________________________________________________________________
**Initial Hypotheses

Hypothesis 1: Let's see if there is a relationship between sqft and tax_value.
alpha = .05
$H_0$: There is no relationship between sqft and tax_value, they are independent. 
$H_a$: There is a relationship between sqft and tax_value, they are dependent on each other

Based on my correlation coefficient and my p-value, I reject my Null hypothesis 1 that there is no correlation 
between sqft and tax_value.

Hypothesis 2: Let's see if there is a relationship between baths and tax_value.
alpha = .05
$H_0$: There is no relationship between baths and tax_value, they are independent. 
$H_a$: There is a relationship between baths and tax_value, they are dependent on each other.

Based on my correlation coefficient and my p-value, I reject my Null hypothesis 2 that there is no correlation 
between baths and tax_value.

____________________________________________________________________________________
**Executive Summary - Conclusions & Next Steps**

I found that of the regression models I created Logistic Regression and Lasso Lars, both models outperformed the baseline model at predicting housing price. 

I chose the Logistic Regression model because it reduced the MSE or error in prediction by 9 cents more than the Lasso Lars model did on train and and reduced the error by $5.02 on validate when predicting housing price, my target value.   

With more time I would like to investigate how homes with pools drive the tax_value as this seems to be an element that could be a driver.

____________________________________________________________________________________
**Key takeaways and Recommendations**

Since we now know bathroom count and square footage have a strong linear relationship with the value of a home, we can expect homes with more bathrooms and/or more square feet will correlate with higher tax valued homes in the three counties we focused on.

____________________________________________________________________________________
**Reproduce My Project**

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

 Read this README.md
 Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
 Add your own env file to your directory. (user, password, host)
 Run the zillow_final_notebook.
 
____________________________________________________________________________________


