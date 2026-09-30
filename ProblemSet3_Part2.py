#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
with open(file='data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)

#%% Task 4.2

#Split the headerLineString into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index('mmsi')
name_idx = header_items.index('shipname')
fleet_idx = header_items.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vessel_dict = {}
#Iterate through all lines (except the header) in the data file:
for line in line_list[1:]:
#Split the data into values
    line_string = line.split(',')
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = line_string[mmsi_idx]
#Extract the fleet value
    fleet = line_string[fleet_idx] 
#Adds info to the vesselDict dictionary
    vessel_dict[mmsi] = fleet   

print(len(vessel_dict))
# %% Task 4.4
#assigns mmsi value to vesselID
vesselID = "312887000"
#calls value for vesselID
vessel_fleet = vessel_dict[vesselID]
#prints the fleet and vesselID
print('Vessel # '+ vesselID + " flies the flag of " + vessel_fleet)

# %% Task 5. Scripting task
with open(file='data/raw/loitering_events_20180723.csv',mode='r') as file_obj:
    #Read the entire contents into a list object
    loiter_line_list = file_obj.readlines()

loiter_header = loiter_line_list[0]
header_items = loiter_header.split(',')

mmsi_i      = header_items.index('transshipment_mmsi')
start_lat_i = header_items.index('starting_latitude')
start_lon_i = header_items.index('starting_longitude')
end_lat_i   = header_items.index('ending_latitude')
end_lon_i = header_items.index('ending_longitude')

loitering_vessels = []

for line in loiter_line_list[1:]:
    line_string = line.strip().split(',')
    loiter_mmsi = line_string[mmsi_i]
    starting_lat = float(line_string[start_lat_i])
    ending_lat = float(line_string[end_lat_i])
    starting_lon = float(line_string[start_lon_i])
    ending_lon = float(line_string[end_lon_i])

    equator_crossed = ((starting_lat) * (ending_lat)) < 0 and starting_lat < 0

    starting_lon_inrange = 145 <= float(starting_lon) <= 155
        
    if equator_crossed and starting_lon_inrange:
        loitering_vessels.append(loiter_mmsi)
        print(starting_lat, ending_lat, starting_lon)
    
for i in loitering_vessels:
    vessel_fleet = vessel_dict[i]
    print('Vessel # '+ i + " flies the flag of " + vessel_fleet)



# %%
