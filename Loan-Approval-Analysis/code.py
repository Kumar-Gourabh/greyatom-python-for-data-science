# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=pd.DataFrame(bank_data)


#Code starts here
categorical_var=bank.select_dtypes(include='object')
print('Categorical',categorical_var.head(0))
numerical_var=bank.select_dtypes(include='number')
print('Numerical',numerical_var.head(0))

banks=bank.drop(['Loan_ID'],axis=1)
print('Banks',banks.head(0))
null_sum=banks.isnull().sum()
print('null_sum\n',null_sum)
bank_mode=banks.mode()
print('Banks_mode\n',bank_mode)
for x in banks.columns.values:
        banks[x]=banks[x].fillna(bank_mode[x].iloc[0])
print('New NA Total=',banks.isnull().sum().values.sum())

avg_loan_amount=pd.pivot_table(banks,values='LoanAmount',index=['Gender','Married','Self_Employed'],aggfunc=np.mean)
print(avg_loan_amount)

loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
Loan_Status = 614
percentage_se=(loan_approved_se/Loan_Status)*100
percentage_nse=(loan_approved_nse/Loan_Status)*100
print(percentage_se,2)
print(percentage_nse,2)

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.mean()





