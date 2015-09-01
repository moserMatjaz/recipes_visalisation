import numpy
import csv
import time

start_time = time.time()
def array_filer():  # function for reading the file and filling the array with propper values
    with open('actual_relationship_file.csv', 'r', ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ingredient, recipe = row
            myArray[int(recipe), int(ingredient)] = 1
        csvfile.close()
        print("Array filler:")
        print(myArray.shape)


def array_mutilator(the_array):
    new_array = the_array[~numpy.all(the_array == 0, axis=1)]
    new_new_array = new_array[:, numpy.sum(new_array, axis=0) != 0]
    return new_new_array


def indexer(the_array):
    ALL_RECIPES_ARRAY = []
    RECIPE_INDEXES_ARRAY = [0]
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
    
    output_file = open('output_file_mutual_method_2.txt', 'w')
    dense_array = numpy.zeros(57691)
    for x in range(0,len(dense_array)):
        dense_array[x] = -1;
        
    for x in range(0, len(RECIPE_INDEXES_ARRAY)):
        comparisson_recipe_1 = ALL_RECIPES_ARRAY[x]
        xsize = RECIPE_INDEXES_ARRAY[x+1] - RECIPE_INDEXES_ARRAY[x]
        output = str(x) + ":"
    
        for k in range(0,len(comparisson_recipe_1)):
            dense_array[comparisson_recipe_1[k]] = x;

        for z in range(x + 1, len(RECIPE_INDEXES_ARRAY) - 1):
            comparisson_recipe_2 = ALL_RECIPES_ARRAY[z]
            zsize = RECIPE_INDEXES_ARRAY[z+1] - RECIPE_INDEXES_ARRAY[z]

            mutual_counter = 0 
            for k in range(0,len(comparisson_recipe_2)):
                if dense_array[comparisson_recipe_2[k]] == x:
                    mutual_counter += 1
                    
            union = xsize + zsize - mutual_counter
            distance = mutual_counter / union
            output = output + " " + str("%.4f" % distance)
        
        output = output + "\n"
        output_file.write(output)
    output_file.close()
    
myArray = numpy.zeros((57691, 1531), dtype='int32')  # initialized array of size ( recipes, ingredients) with all zeros
array_filer()
myArray = array_mutilator(myArray)
RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY = indexer(myArray)
myArray = []
calculator(RECIPE_INDEXES_ARRAY, ALL_RECIPES_ARRAY)
print("--- %s seconds ---" % (time.time() - start_time))