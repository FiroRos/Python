import csv
import numpy as np
import matplotlib.pyplot as plt

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

def min_max_diameter1(no_names_ndarray): #סעיף ח' שתי פונקציות כי המשימה לא ברורה
    iterations = 0                       #returns the average of all min diameters and the average of all max diameters
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

def min_max_diameter2(no_names_ndarray): #returns the smallest and biggest average diameter PER ASTEROID
    list = []
    for row in no_names_ndarray:
        min_dia = float(str(row[3]))
        max_dia = float(str(row[4]))
        avg_diameter = (min_dia + max_dia)/2
        list.append(avg_diameter)
    list = sorted(list)
    tuple = (list[0], list[-1])
    return tuple

def average_diameter_list(no_names_ndarray): #returns the smallest and biggest average diameter PER ASTEROID
    list = []
    for row in no_names_ndarray:
        min_dia = float(str(row[3]))
        max_dia = float(str(row[4]))
        avg_diameter = (min_dia + max_dia)/2
        list.append(avg_diameter)
    list = sorted(list)
    return list

###########################################################################


def plt_hist_diameter(no_names_ndarray, min_max_dia):
    list = []
    asteroid_per_range = []
    hist_x = []
    list_lentgh = len(min_max_dia)
    list_part_length_remainder = list_lentgh % 10 #7
    list_part_length = list_lentgh//10 #468
    list_split_start = 0
    list_split_end = list_part_length
    for i in range(10):
        if i == 9:
            list_split_end += list_part_length_remainder
        list.append(min_max_dia[list_split_start:list_split_end])
        list_split_start = list_split_end
        list_split_end += list_part_length

    for i in list:
        hist_x.append([str(i[0]) + "-" + str(i[-1])])
    
    for i in list:
        asteroid_count = 0
        for asteroid in i:
            asteroid_count += 1
        asteroid_per_range.append(asteroid_count)
             
    return asteroid_per_range
    






    

     
     


     




ndarray = load_data(excel_file)

no_names_ndarray = scoping_data(ndarray)

Dangerous_asteroids = mask_data(no_names_ndarray)

min_max_dia = average_diameter_list(no_names_ndarray)
#print(min_max_dia)


print((plt_hist_diameter(no_names_ndarray, min_max_dia)))
#test = plt_hist_diameter(no_names_ndarray, min_max_dia)
#print(len(test[0]))