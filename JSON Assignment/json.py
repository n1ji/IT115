import json
from datetime import datetime

specific_date = datetime(2002, 6, 19, 6, 40)
current_date = datetime.now()
time_difference = current_date - specific_date

dataOne = {
    'name':'Myra',
    'ageInYears': "22",
    'city':'Sunnyside, NY',
    'interests':['Headphones','Technology','Programming','Rock Climbing','Photography'],
    'isStudent': False
}

#
with open('dataOne.json', 'w') as json_file:
    #Dump the data dictionary to a JSON file
    json.dump(dataOne,json_file,indent=4)

#Confirmation message that writes to the terminal to let us know the program has run successfully
print('Data has been written to dataOne.json')

#
with open ('dataOne.json','r') as json_file:
    #Load data from json file
    loadedData = json.load(json_file)

print('Successfully read dataOne.json')
print(loadedData)

#Change age and add another interest to the list
loadedData['ageInYears'] = 22.40657
loadedData['interests'].append('Webfishing')

#Add and remove an interest
loadedData['interests'].append('R6S')
loadedData['interests'].remove('R6S')

with open('dataOne.json', 'w') as json_file:
    #Dump the data dictionary to a JSON file
    json.dump(loadedData,json_file,indent=4)

#Confirmation message that writes to the terminal to let us know the program has run successfully
print('Data has been re-written to dataOne.json')