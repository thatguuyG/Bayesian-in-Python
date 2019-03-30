'''
Created on 25 Mar 2019

@author: Aizen
'''

import pandas as pd
import numpy as np

# Create a datatable
data = pd.DataFrame()

# Create our target variable
data['Temperature'] = ['Hot', 'Hot', 'Hot', 'Mild', 'cool', 'Cool','cool', 'Mild', 'cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
data['Outlook'] = ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain','Overcast', 'Sunny', 'sunny', 'Rain', 'sunny', 'Overcast', 'Overcast', 'Rain']
data['Humidity'] = ['High', 'High', 'high', 'high', 'Normal', 'Normal','Normal', 'High', 'Normal', 'Normal', 'Normal', 'high', 'Normal', 'High']
data['Wind'] = ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong','Strong', 'Weak', 'Weak', 'Weak', 'strong', 'strong', 'Weak', 'strong']

data['PlayTennis'] = ['No','No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes','Yes', 'Yes', 'No'] #output

# View the data
print(data)
print(   )
print(   )

'''creating a new instance'''
person = pd.DataFrame()
person['Temperature'] = ['Cool']#test instance from which we'll determine its class
person['Outlook'] = ['Sunny']
person['Humidity'] = ['High']
person['Wind'] = ['Strong']

print('New intance')
print(person)
print(   )


n_Yes = data['PlayTennis'][data['PlayTennis'] == 'Yes'].count()#Number of play tennis instances
n_No = data['PlayTennis'][data['PlayTennis'] == 'No'].count()#number of NOT playing tennis instances
total_instances = data['PlayTennis'].count()#total rows

print('Total instances are:')
print(total_instances)



'''Learning phase'''

P_Yes = n_Yes/total_instances#probability of getting yes
P_No = n_No/total_instances#probability of getting no

print('Probability of  playing tennis is:')
print(round(P_Yes,3))

print('Probability of NOT  playing tennis is:')
print(round(P_No,3))
print( )

'''Testing phase'''
#for playing part(prob of the new instances while playing)

P_Sunny = data['Outlook'][data['Outlook'] == 'sunny'].count()#no of sunny days in outlook where tennis is played
P_Sunny_Yes = P_Sunny/n_Yes

P_Cool = data['Temperature'][data['Temperature'] == 'cool'].count()#no of cool days where tennis is played
P_Cool_Yes = P_Cool/n_Yes

P_High = data['Humidity'][data['Humidity'] == 'high'].count()#no of high humidity days  where tennis is played
P_High_Yes = P_High/n_Yes

P_Strong = data['Wind'][data['Wind'] == 'strong'].count()#no of strong wind days  where tennis is played
P_Strong_Yes = P_Strong/n_Yes
P_Yes

P_Yes_Final = P_Sunny_Yes*P_Cool_Yes*P_High_Yes*P_Strong_Yes*P_Yes
print("Decision Making with the MAP rule")
print("Probability of playing tennis with the new instances is;")
print(round(P_Yes_Final,4))




#for  NOT playing part(prob of the new instances while  NOT playing)
P_Sunny = data['Outlook'][data['Outlook'] == 'Sunny'].count()#no of  sunny days in outlook where tennis is  NOT played
P_Sunny_No = P_Sunny/n_No

P_Cool = data['Temperature'][data['Temperature'] == 'Cool'].count()#no of  cool days where tennis is  NOT played
P_Cool_No = P_Cool/n_No

P_High = data['Humidity'][data['Humidity'] == 'High'].count()#no of high humidity days  where tennis is NOT played
P_High_No = P_High/n_No

P_Strong = data['Wind'][data['Wind'] == 'Strong'].count()#no of strong wind days  where tennis is  NOT played
P_Strong_No = P_Strong/n_No
P_No

P_No_Final = P_Sunny_No*P_Cool_No*P_High_No*P_Strong_No*P_No

print("Probability of  NOT playing tennis with the new instances is;")
print(round(P_No_Final, 4))
print(   )

if P_Yes_Final>P_No_Final:
    print("We label the new instance to be Yes to Playing Tennis")
    print(round(P_Yes_Final,4))
 
else:
    print("We label the new instance to be No to playing Tennis")
    print(round(P_No_Final, 4))
  
 





















