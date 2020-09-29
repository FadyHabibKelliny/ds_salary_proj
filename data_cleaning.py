# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:14:55 2020

@author: Fady_
"""

'''''1-salary parsing'''''
'''''2-company name text only'''''
'''''3-state field'''''
'''''4-age of company'''''
'''''5-parcing of job discreption'''''


import pandas as pd
df = pd.read_csv('Glassdoor_jobs.csv')

# check if the salary estimate column have some of this  ( remove 'per hour' and ' employer salary)
# apply this by adding a new colum contans 1 if yes and 0 if no
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour'in x.lower() else 0)
df['employer salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'Employer  estimate salary' in x.lower() else 0)


#1 
#delete any cell with value of [-1] 
df = df[df['Salary Estimate'] != '-1']

#2
#split the salary cell and remove the second part
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#3
#remove any K or $ from salaries
remove_text = salary.apply(lambda x: x.replace('K',' ').replace('$',' '))

#4
#remove any of 'per hour' or ' employer salary
per_hour = remove_text.apply(lambda x: x.lower().replace('per hour', ''))

#4
#remove any of 'per hour' or ' employer salary
per_hour = remove_text.apply(lambda x: x.lower().replace('per hour', '').replace('employer  estimate salary', ''))

#5
#add new column for the df ( min salary ) - ( max salay)
df['min_salary'] = per_hour.apply(lambda x: x.split('-')[0])
df['max_salary'] = per_hour.apply(lambda x: x.split('-')[1])

# convert to int
df['min_salary'] = df['min_salary'].astype(str).astype(int)
df['max_salary'] = df['max_salary'].astype(str).astype(int)

#make the avg salary column
df['avg_salary'] = (df.min_salary+df.max_salary)/2

## to check data type if needed
#print(df['max_salary'].dtype)
#print(df['min_salary'].dtype)

#7
#company name text only
df['Company_text'] = df.apply(lambda x:x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#8
#state field
df['check_state'] = df['Location'].apply(lambda x: 1 if ','in x.lower() else 0)
df['state1']= df['Location'].apply(lambda x: x.split(',')[1] if ',' in x.lower() else x.split(',')[0])
df.state1.value_counts()

#if neded(if any city have no state we can change it by this line)
#['state1'] = df['state1'].apply(lambda x: x.lower().replace('utah', ' us'))


# if needed(check if the headquartre of the job at the same location)
#df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

#9
#age of company
#age colum is missed but if founded apply this line
#df['age'] =  df['age'].asint()
#df['age'] = df['Founded'].apply(lambda x: x if x <1 else 2020 - x)

#10
#parcing of job discreption
                                           #1 python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()


                                          #2 r studio
df['r_studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df.r_studio.value_counts()

                                          #2 spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()


                                          #2 aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()


                                          #2 excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#finall save the fine as csv
df.to_csv('salary_data_cleard.csv', index = False)


