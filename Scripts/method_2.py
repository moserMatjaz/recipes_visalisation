import numpy
import csv
import time

start_time = time.time()
myArray = numpy.zeros((57691, 1531), dtype='int32')

def array_filer():  # function for reading the file and filling the array with propper values
    with open('actual_relationship_file.csv', 'r', ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ingredient, recipe = row
            myArray[int(recipe), int(ingredient)] = 1
        csvfile.close()
    
def array_mutilator(the_array):
    new_array = the_array[~numpy.all(the_array == 0, axis=1)]
    new_new_array = new_array[:, numpy.sum(new_array, axis=0) != 0]
    return new_new_array

def indexer(the_array):
    ALL_RECIPES_ARRAY = []
    RECIPE_INDEXES_ARRAY = []
    next_recipe_index = 0
    for recipe in range(0, the_array.shape[0]):

        CURRENT_RECIPE_ARRAY = []
        value = 1

        for column in range(0, the_array.shape[1]):
            if value == the_array[recipe, column]:
                CURRENT_RECIPE_ARRAY.append(column)
                
        next_recipe_index += len(CURRENT_RECIPE_ARRAY)
        RECIPE_INDEXES_ARRAY.append(next_recipe_index)
        ALL_RECIPES_ARRAY.append(CURRENT_RECIPE_ARRAY)
            
    return RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY


def calculator(RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY):
    output_file = open('output_file.txt', 'a')
    for x in range(0, len(RECIPE_INDEXES_ARRAY)):
        for z in range(x + 1, len(RECIPE_INDEXES_ARRAY)- 1):
            mutual_counter = 0
            index_1 = RECIPE_INDEXES_ARRAY.index(RECIPE_INDEXES_ARRAY[x])
            index_2 = RECIPE_INDEXES_ARRAY.index(RECIPE_INDEXES_ARRAY[z])
            index_3 = index_2 + 1

            comparisson_recipe_1 = ALL_RECIPES_ARRAY[slice(index_1, index_2)]
            comparisson_recipe_2 = ALL_RECIPES_ARRAY[slice(index_2, index_3)]
 
            for y in range(0, len(comparisson_recipe_1[0])):
                if comparisson_recipe_1[0][y] in comparisson_recipe_2[0]:
                    mutual_counter += 1

            if mutual_counter > 0:
                union = len(comparisson_recipe_1[0]) + len(comparisson_recipe_2[0]) - mutual_counter
                float(mutual_counter)
                float(union)
                distance = mutual_counter / union
                float(distance)
                
                output = str(x) + ',' + str(z) + ","+ str(distance) + '\n'
                print(output)
                output_file.write(output)
    output_file.close()
    
print(myArray.shape)
array_filer()
myArray = array_mutilator(myArray)
print(myArray.shape)
RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY = indexer(myArray)
myArray = []
calculator(RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY)

print("--- %s seconds ---" % (time.time() - start_time))