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

def no_names_row(ndarray): #help function
    delete_ndarray_names = np.delete(ndarray, 0, 0)
    return delete_ndarray_names

###########################################################################

def scopiong_data(ndarray, names):
    col = 0
    cols_to_delete = []
    for title in ndarray[0]:
        for name in names:
            if name.lower() == title.lower():
                cols_to_delete.append(col)
        col +=1
    new_array = np.delete(ndarray, [cols_to_delete], axis=1)
    return new_array

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

def min_max_diameter_range(no_names_ndarray): #returns the smallest and biggest average diameter PER ASTEROID
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


def plt_hist_diameter(average_dia_list, min_max_dia):
    range_list_bar_names = []
    asteroid_number_list = []
    range_list = []
    log_space = np.logspace(np.log10(min_max_dia[0]), np.log10(min_max_dia[1]), num=11) #logrithmic divison of the range (10 ranges)
    print(log_space)
    for i in range(len(log_space) - 1): 
        range_list.append(float(log_space[i])) #defines the ranges
        range_list.append(float(log_space[i+1]))
        range_list_bar_names.append(str(log_space[i]) + "-\n" + str(log_space[i+1])) #creates the names of the bars

    min = 0
    max = 1
    for i in range(len(range_list_bar_names)):
        asteroid_count = 0
        for asteroid_dia in average_dia_list:
            if asteroid_dia >= range_list[min] and asteroid_dia <= range_list[max]:
                asteroid_count +=1
        min += 2
        max += 2
        asteroid_number_list.append(asteroid_count)
    #building the graph
    plt.figure(figsize=(15, 6))
    plt.xticks(fontsize=5)
    bars = plt.bar(range_list_bar_names, asteroid_number_list)
    for bar in bars: #adds the number of asteroids above the bar to make the graph easier to understand
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 1), ha='center', va='bottom', fontsize=10)
    plt.xlabel("Average Diameter") 
    plt.ylabel("Number Of Asteroids")   
    plt.title("Asteroids Per Diameter")
    plt.show()
    print(asteroid_number_list)

    
#f"Range {i+1}: {log_space[i]} to {log_space[i+1]}")





    

     
     


     
names = ["absolute magnitude", "name", "Close Approach Date", "est dia in KM(max)", "miss Dist.(Astronomical)"]



ndarray = load_data(excel_file)

no_names_ndarray = no_names_row(ndarray)

min_max_dia = min_max_diameter_range(no_names_ndarray)

average_dia_list = average_diameter_list(no_names_ndarray)



plt_hist_diameter(average_dia_list, min_max_dia)
