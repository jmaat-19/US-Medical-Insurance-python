#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[20]:


import os
import csv

# figure out how to access my csv file by pwd
print(os.getcwd())

# opening up my file of interest
with open('/Users/jonathanmaat/data_science/insurance.csv') as insurance_data:
    
    # using Dictreader to write data as a dictionary data type
    insurance_dict = csv.DictReader(insurance_data)
    
    # looking at all newly created dictionaries
#     for row in insurance_dict:
#         print(row)
    
    
    # turning full set of dictionaries into a string
    insurance_list = list(insurance_dict)
#     print(insurance_list)
        
    
    print(insurance_list[0].keys())
    print(insurance_list[0].values())
    
    insurance_data.close()

# numerical: age,bmi,children,charges
# categorical: sex,smoker,region
# no missing data


# # Find out the average age of the patients in the dataset.

# In[70]:


# opening up my file of interest
with open('/Users/jonathanmaat/data_science/insurance.csv') as insurance_data:
    insurance_dict = csv.DictReader(insurance_data)
    total_age = 0
    counter = 0
    print(insurance_dict)
    for row in insurance_dict:
        counter += 1
        total_age += int(row['age'])
    
    average_age = total_age/counter
    average_age = round(average_age, 1)
    print('The average age is: {} for the dataset'.format(average_age))
    
    insurance_data.close()


# # Analyze where a majority of the individuals are from.
# 

# In[67]:


# this time we are going to use function to make this analysis look a little bit cleaner
def dictionary_counter(dictionary,key):
    total_number_of_people = 0
    dict_count = {}
    for row in dictionary:
        total_number_of_people += 1
        if row[key] not in dict_count:
            dict_count[row[key]]= 1
        else:
            dict_count[row[key]] += 1
    return dict_count, total_number_of_people
        

with open('/Users/jonathanmaat/data_science/insurance.csv') as insurance_data:
    insurance_dict = csv.DictReader(insurance_data)
    dict_counter = dictionary_counter(insurance_dict, 'region')
    #print(dict_counter)
    
    sw_per = round(dict_counter[0]['southwest']/dict_counter[1]*100,1)
    se_per = round(dict_counter[0]['southeast']/dict_counter[1]*100,1)
    nw_per = round(dict_counter[0]['northwest']/dict_counter[1]*100,1)
    ne_per = round(dict_counter[0]['northeast']/dict_counter[1]*100,1)
   
    print('Percentage breakdown: southwest = {}, southeast = {}, northwest = {}, northeast {}'.format(sw_per, se_per, nw_per, ne_per))
    print('The largest proportion of individuals come from the southeast.')
    
    insurance_data.close()
    
    
    


# # Look at the different number of smokers vs. non-smokers.
# 

# In[80]:


with open('/Users/jonathanmaat/data_science/insurance.csv') as insurance_data:
    insurance_dict = csv.DictReader(insurance_data)
    dict_counter = dictionary_counter(insurance_dict, 'smoker')
    print(dict_counter)
    
    print('There is a larger propertion of non-smokers contained in this dataset.')
    
    insurance_data.close()
   

