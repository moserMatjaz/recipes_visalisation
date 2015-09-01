import numpy
import csv
import time

start_time = time.time()
myArray = numpy.zeros((57691, 1531), dtype='int32')


def array_filer():
    with open('actual_relationship_file.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ingredient, recipe = row
            myArray[int(recipe), int(ingredient)] = 1
        csvfile.close()


def array_mutilator(the_array):
    new_array = the_array[~numpy.all(the_array == 0, axis=1)]
    new_new_array = new_array[:, numpy.sum(new_array, axis=0) != 0]
    return new_new_array


def calculator(the_array):
    output_file = open("output_file.csv", "a")
    for x in range(0, 11):
        for y in range(0, the_array.shape[0]):
            if y > x:
                mutual_counter = 0
                union = 0
                distance = 0
                RECIPE_1 = []
                RECIPE_2 = []
                for column_1 in range(0, the_array.shape[1]):
                    if 1 == the_array[x, column_1]:
                        RECIPE_1.append(column_1)
                for column_2 in range(0, the_array.shape[1]):
                    if 1 == the_array[y, column_2]:
                        RECIPE_2.append(column_2)
                
                for z in range(0, len(RECIPE_1)):
                    if RECIPE_1[z] in RECIPE_2:
                        mutual_counter += 1
                if mutual_counter > 0:
                    union = len(RECIPE_1) + len(RECIPE_2) - mutual_counter
                    distance = mutual_counter / union
                    output = str(x) + "," + str(y) + "," + str(distance) + "\n"
                    print(output)
                    output_file.write(output)
    output_file.close()

array_filer()
print(myArray.shape)
myArray = array_mutilator(myArray)
print(myArray.shape)
calculator(myArray)
print("--- %s seconds ---" % (time.time() - start_time))