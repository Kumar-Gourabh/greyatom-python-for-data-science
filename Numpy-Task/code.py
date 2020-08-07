# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate([data,new_record])
print(data.shape)
print(census.shape)
age=census[:,0]
max_age = np.max(age)
print(max_age)
min_age= np.min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)
race=census[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)
len_race=np.array([len_0,len_1,len_2,len_3,len_4])
min_race=np.min(len_race)
minority_race_index=np.where(len_race==min_race)
minority_race=minority_race_index[0][0]
print("Minority Race=",minority_race)

senior_citizens=age[age>60]
working_hours=census[:,6][age>60]
working_hours_sum=np.sum(working_hours)
print(working_hours_sum)
senior_citizens_len=senior_citizens.size
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

edu_num=census[:,1]
high=edu_num[edu_num>10]
low=edu_num[edu_num<=10]
avg_pay_high=np.mean(census[:,7][edu_num>10])
avg_pay_low=np.mean(census[:,7][edu_num<=10])
print(avg_pay_high)
print(avg_pay_low)
if(avg_pay_high>avg_pay_low):
    print("Parents were right")
else:
    print("Parents were wrong!")


