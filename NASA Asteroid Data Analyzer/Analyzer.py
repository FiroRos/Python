import csv
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import os

########################################################################### Variables

excel_file = "nasa.csv"
names = ["absolute magnitude", "name", "Close Approach Date", "est dia in KM(max)", "miss Dist.(Astronomical)"]
quit = False

########################################################################### 1          

def load_data(excel_file): #section A
    list = []
    with open(excel_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
                list.append(row)
        list = np.array(list)
        return list

########################################################################### 2

def no_names_row(): #help function
    delete_ndarray_names = np.delete(load_data(excel_file), 0, 0)
    return delete_ndarray_names

def clear_screen_os(): #clears terminal
    if os.name == "nt":  #nt == windows
        _ = os.system("cls")
    else: #mac & linux
        _ = os.system("clear")

########################################################################### 3

def scopiong_data(names): #section B
    col = 0
    cols_to_delete = []
    for title in load_data(excel_file)[0]:
        for name in names:
            if name.lower() == title.lower():
                cols_to_delete.append(col)
        col +=1
    new_array = np.delete(load_data(excel_file), [cols_to_delete], axis=1)
    return new_array

########################################################################### 4

def mask_data(): #section C
    list = []
    for row in no_names_row():
        date = row[11]
        splitted_date = date.split("-")
        year = int(splitted_date[0])
        if year >= 2000:
             list.append(row)
    list = np.array(list)
    return list

########################################################################### 5

def data_details(): #section D
    new_array = np.delete(no_names_row(), [0, 20, 38] , 1)
    array_dimensions = new_array.shape
    formatted_output = "after deleting the following columns: \"Equinox\", \"Orbiting Body\", \"Neo Refrence\":\nthe array has " + str(array_dimensions[0]) + " columns and " + str(array_dimensions[1]) + " rows"
    return formatted_output

########################################################################### 6

def max_absolute_magnitude(): #section E
    no_names_ndarray = no_names_row()
    sorted_array = no_names_ndarray[no_names_ndarray[:, 2].argsort()[::-1]]
    name = sorted_array[0][1]
    proximity = sorted_array[0][2]
    asteroid = (str(name), str(proximity))
    return asteroid
 
########################################################################### 7

def closest_to_earth(): #section F
    no_names_ndarray = no_names_row()
    sorted_array = no_names_ndarray[no_names_ndarray[:, 18].argsort()[::-1]]
    closest_to_earth_list = sorted_array[0][1]
    return closest_to_earth_list 

########################################################################### 8

def common_orbit(): #section G
    temp_list = []
    dictionary = {}
    for row in no_names_row():
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

########################################################################### 9

def min_max_diameter(): #returns the smallest and biggest average diameter PER ASTEROID section H
    list = []
    for row in no_names_row():
        min_dia = float(str(row[3]))
        max_dia = float(str(row[4]))
        avg_diameter = (min_dia + max_dia)/2
        list.append(avg_diameter)
    list = sorted(list)
    tuple = (list[0], list[-1])
    return tuple

def average_diameter_list(): #returns the list of average diameters of all asteroids
    list = []
    for row in no_names_row():
        min_dia = float(str(row[3]))
        max_dia = float(str(row[4]))
        avg_diameter = (min_dia + max_dia)/2
        list.append(avg_diameter)
    list = sorted(list)
    return list

########################################################################### 10


def plt_hist_diameter(): #section I
    min_max_dia = min_max_diameter()
    range_list_bar_names = []
    asteroid_number_list = []
    range_list = []
    log_space = np.logspace(np.log10(min_max_dia[0]), np.log10(min_max_dia[1]), num=11) #logrithmic divison of the range (10 ranges)
    for i in range(len(log_space) - 1): 
        range_list.append(float(log_space[i])) #defines the ranges
        range_list.append(float(log_space[i+1]))
        range_list_bar_names.append(str(log_space[i]) + "-\n" + str(log_space[i+1])) #creates the names of the bars

    min = 0
    max = 1
    for i in range(len(range_list_bar_names)):
        asteroid_count = 0
        for asteroid_dia in average_diameter_list():
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
    plt.xlabel("Average Diameter Range") 
    plt.ylabel("Number Of Asteroids")   
    plt.title("Asteroids Per Diameter Range")
    plt.show()

########################################################################### 11

def plt_hist_common_orbit():
    orbit_range = []
    orbit_range_list_bar_names = []
    asteroid_number_per_orbit = []
    orbit_list = list(map(int, list(common_orbit().keys())))
    orbit_list_sorted = sorted(orbit_list)
    log_space = np.logspace(np.log10(orbit_list_sorted[0]), np.log10(orbit_list_sorted[-1]), num=7) #logrithmic divison of the range (6 ranges)
    orbit_range = [math.ceil(i) for i in log_space]
    for i in range(6):
        orbit_range_list_bar_names.append(str(orbit_range[i]) + "-" + str(orbit_range[i+1])) #creates the names of the bars
    min = 0
    max = 1
    for i in range(6):
        asteroid_count = 0
        for asteroid in common_orbit().keys():
            if int(asteroid) >= orbit_range[min] and int(asteroid) <= orbit_range[max]:
                asteroid_count += common_orbit()[asteroid]
        min += 1
        max += 1
        asteroid_number_per_orbit.append(asteroid_count)

    #building the graph
    plt.figure(figsize=(15, 6))
    plt.xticks(fontsize=16)
    bars = plt.bar(orbit_range_list_bar_names, asteroid_number_per_orbit)
    for bar in bars: #adds the number of asteroids above the bar to make the graph easier to understand
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 1), ha='center', va='bottom', fontsize=10)
    plt.xlabel("Orbit Range") 
    plt.ylabel("Number Of Asteroids")   
    plt.title("Asteroids Per Orbit Range")
    plt.show()

########################################################################### 13

def plt_pie_hazard():
    hazardous = 0
    non_hazardous = 0
    for row in no_names_row():
        if row[39] == "True":
            hazardous += 1
        elif row[39] == "False":
            non_hazardous += 1
    sizes = [hazardous, non_hazardous]
    labels = ["Hazardous", "Non-Hazrdous"]
    def absolute_value(val):
        total = sum(sizes)
        value = int(val / 100 * total)
        return f'{value}' 
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct=absolute_value)
    plt.show()

###########################################################################

def plt_linear_motion_magnitude():
    abs_mag = []
    mph = []
    for row in no_names_row():
        abs_mag.append(float(str(row[2])))
        mph.append(float(str(row[15])))

    coef = np.polyfit(abs_mag, mph, 1)
    poly1d_fn = np.poly1d(coef) 
    plt.plot(abs_mag, mph, 'yo', label='Data Points')  # Yellow circles for the data points
    plt.plot(abs_mag, poly1d_fn(abs_mag), '--k', label='Linear Fit')  # Blackline for the fit
    plt.xlim(min(abs_mag) - 1, max(abs_mag) + 1)
    plt.ylim(min(mph) - 1, max(mph) + 1)
    plt.xlabel('Absolute Magnitude')
    plt.ylabel('Miles Per Hour')
    plt.title('Linear Regression of Between Absolute Magnitude and Miles Per Hour')
    plt.legend()
    plt.show()
    

    
###########################################################################

print("Welcome! This project is about proccessing data extracted from an Excell file!")
time.sleep(1.5)
while quit == False:
    user_input = input("What would you like to see (1-4)? (type H to show available options and Q to quit): ")
    if user_input in ["1", "2", "3", "4", "h", "H", "q", "Q"]:
        if user_input.lower() == "h":
            print("The available options are:\n(1)   A histogram graph that shows the number of asteroids per diameter range\n(2)   A histogram graph that shows the number of asteroids per orbit range\n(3)   A pie chart displaying the number of hazardous and non-hazardous asteroids\n(4)   A linear regression graph that shows the correlation between the speed of the asteroid and its magnitude\n \n ")
        elif user_input.lower() == "q":
            print("Terminating program... :(")
            time.sleep(1)
            clear_screen_os()
            quit = True
        elif user_input == "1":
            print("Crunching the numbers...\nPlease standby...")
            plt_hist_diameter()
            clear_screen_os()
        elif user_input == "2":
            print("Crunching the numbers...\nPlease standby...")
            plt_hist_common_orbit()
            clear_screen_os()
        elif user_input == "3":
            print("Crunching the numbers...\nPlease standby...")
            plt_pie_hazard()
            clear_screen_os()
        elif user_input == "4":
            print("Crunching the numbers...\nPlease standby...")
            plt_linear_motion_magnitude()
            clear_screen_os()




    else:
        print("Not a valid input! type H for the list of available inputs!")

     
     


