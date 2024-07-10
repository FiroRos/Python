import csv
import numpy as np

excel_file = "nasa.csv"

#def load_data(excel_file):      #immedietly gives a ndarray without the column's names
#    list = []
#    i = 0
#    with open(excel_file, 'r') as file:
#        reader = csv.reader(file)
#        for row in reader:
#            if i > 0:
#                list.append(row)
#            i += 1
#        list = np.array(list)
#        return list
###########################################################################            

def load_data(excel_file): #סעיף א
    list = []
    with open(excel_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
                list.append(row)
        list = np.array(list)
        return list

###########################################################################

def scoping_data(ndarray): #סעיף ב
     delete_ndarray_names = np.delete(ndarray, 0, 0)
     return delete_ndarray_names

###########################################################################

def mask_data(no_names_ndarray): #סעיף ג
    list = []
    for row in no_names_ndarray:
        date = row[11]
        splitted_date = date.split("-")
        year = int(splitted_date[0])
        if year >= 2000:
             list.append(row)
    list = np.array(list)
    return list

###########################################################################

def data_details(no_names_ndarray): #סעיף ד
    new_array = np.delete(no_names_ndarray, [0, 20, 38] , 1)
    array_dimensions = new_array.shape
    formatted_output = "after deleting the following columns: \"Equinox\", \"Orbiting Body\", \"Neo Refrence\":\nthe array has " + str(array_dimensions[0]) + " columns and " + str(array_dimensions[1]) + " rows"
    return formatted_output

###########################################################################

def max_absolute_magnitude(no_names_ndarray): #סעיף ה
    sorted_array = no_names_ndarray[no_names_ndarray[:, 2].argsort()[::-1]]
    name = sorted_array[0][1]
    proximity = sorted_array[0][2]
    asteroid = (str(name), str(proximity))
    return asteroid

###########################################################################

def closest_to_earth(no_names_ndarray): #סעיף ו
    sorted_array = no_names_ndarray[no_names_ndarray[:, 18].argsort()[::-1]]
    asteroid = sorted_array[0][1]
    return asteroid 

###########################################################################

def common_orbit(no_names_ndarray): #סעיף ז
    temp_list = []
    dictionary = {}
    for row in no_names_ndarray:
        orbit_id = str(row[21])
        temp_list.append(orbit_id)
    no_dupes = list(set(temp_list))
    for i in no_dupes:
        count = 0
        for x in temp_list:
            if x == i:
                count += 1
            dictionary[i] = count  
    return dictionary

###########################################################################

def min_max_diameter(no_names_ndarray):
    iterations = 0
    min_dia_sum = 0
    max_dia_sum  = 0
    for row in no_names_ndarray:
        iterations += 1
        min_dia_sum += float(str(row[3]))
        max_dia_sum += float(str(row[4]))
    min_dia_avg = min_dia_sum / iterations
    max_dia_avg = max_dia_sum / iterations
    tuple = (min_dia_avg, max_dia_avg)
    return tuple




    

     
     


     




ndarray = load_data(excel_file)

no_names_ndarray = scoping_data(ndarray)

Dangerous_asteroids = mask_data(no_names_ndarray)

test = min_max_diameter(no_names_ndarray)
print(test)

print()