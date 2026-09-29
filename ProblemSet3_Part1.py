#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print(mountain + 
", formerly\nknown as", nickname + ',\n' +
"is " + str(elevation) + "'" + ' above sea level.')
#%% Task 2 - Lists and Iteration

data_folder = "W:\\859_data\\triangle"

data_list = ['streams.shp', 'stream_types.csv', 'naip_imagery.tif']

user_item = 'roads.shp'

data_list.append(user_item)

for string in data_list:
    print(data_folder + '\\' + string)

#%% Task 3

user_numbers = []

for i in range(3):
    print('Enter an integer')
    number = int(input())
    user_numbers.append(number)

user_numbers.sort()
print(max(user_numbers))

#%% Task 3 - Challenge

user_numbers = []

for i in range(3):
    print('Enter an integer')
    number = int(input())
    user_numbers.append(number)

user_numbers.sort(reverse=True)
print(user_numbers)

#%% 
