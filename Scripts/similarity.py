import numpy
import csv
import time

start_time = time.time()
def data_partition():  # partition the dataset according to cuisines
    with open('dataset_final.csv', 'r', ) as csvfile:
        reader = csv.reader(csvfile)
        cuisines_array = []
        for row in reader:
            file_name = ""
            recipe, ingredient, cuisine = row
            if file_name != cuisine:
                file_name = "cuisine_" + str(cuisine) + ".csv"
                with open(file_name, 'a') as csvfile_2:
                    csvfile_2.write(recipe + "," +  ingredient + ","+  cuisine + "\n")
                if cuisine not in cuisines_array:
                    cuisines_array.append(cuisine)
    csvfile_2.close()
    csvfile.close()
    print(cuisines_array)
    print(len(cuisines_array))
    return cuisines_array

def array_mutilator(the_array):
    new_array = the_array[~numpy.all(the_array == 0, axis=1)] 
    return new_array

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

def calculator(RECIPE_INDEXES_ARRAY_CUISINE_1, ALL_RECIPES_ARRAY_CUISINE_1, RECIPE_INDEXES_ARRAY_CUISINE_2, ALL_RECIPES_ARRAY_CUISINE_2, cuisine_1, cuisine_2):
    if cuisine_1 != cuisine_2:
        output_file = open('cuisines_distances_final_run.txt', 'a')
        
        RECIPE_INDEXES_ARRAY_CUISINE_1.remove(0)
        RECIPE_INDEXES_ARRAY_CUISINE_2.remove(0)
        
        total_cuisine_distance = 0
        total_distance = 0
        for x in range(0,len(RECIPE_INDEXES_ARRAY_CUISINE_1)):
            comparisson_recipe_1 = ALL_RECIPES_ARRAY_CUISINE_1[x]
            
            for y in range(0,len(RECIPE_INDEXES_ARRAY_CUISINE_2)):
                comparisson_recipe_2 = ALL_RECIPES_ARRAY_CUISINE_2[y]
                
                mutual_counter = 0
                distance = 0
                
                for k in range(0,len(comparisson_recipe_1)):
                    if comparisson_recipe_1[k] in comparisson_recipe_2:
                        mutual_counter += 1
        
                distance = mutual_counter / (len(comparisson_recipe_1) + len(comparisson_recipe_2) - mutual_counter)
                total_distance += distance
                total_cuisine_distance = total_distance / ((len(RECIPE_INDEXES_ARRAY_CUISINE_1)) * (len(RECIPE_INDEXES_ARRAY_CUISINE_2)))
        output = cuisine_1 + "," + cuisine_2 + "," + str(total_cuisine_distance)
        print(output)
        output_file.write(output + "\n")
        output_file.close()
    
cuisines_array = data_partition()

for x in range(0, len(cuisines_array)):
    for y in range(0, len(cuisines_array)):
        file_name_1 = "cuisine_" + str(cuisines_array[x]) + ".csv"
        file_name_2 = "cuisine_" + str(cuisines_array[y]) + ".csv"
        with open(file_name_1, 'r', ) as csvfile_1:
            with open(file_name_2, 'r', ) as csvfile_2:
                myCuisine_1 = numpy.zeros((57691, 1530), dtype='int')  # fill the array with zeros
                myCuisine_2 = numpy.zeros((57691, 1530), dtype='int')  # fill the array with zeros
                reader_1 = csv.reader(csvfile_1)
                reader_2 = csv.reader(csvfile_2)
                for row in reader_1:
                    recipe, ingredient, cuisine = row
                    myCuisine_1[int(recipe), int(ingredient)] = 1
                    for row in reader_2:
                        recipe, ingredient, cuisine = row
                        myCuisine_2[int(recipe), int(ingredient)] = 1

        myCuisine_1 = array_mutilator(myCuisine_1)
        myCuisine_2 = array_mutilator(myCuisine_2)

        RECIPE_INDEXES_ARRAY_CUISINE_1, ALL_RECIPES_ARRAY_CUISINE_1 = indexer(myCuisine_1)
        RECIPE_INDEXES_ARRAY_CUISINE_2, ALL_RECIPES_ARRAY_CUISINE_2 = indexer(myCuisine_2)
        
        if (cuisines_array[x] != cuisines_array[y]):
            calculator(RECIPE_INDEXES_ARRAY_CUISINE_1, ALL_RECIPES_ARRAY_CUISINE_1, RECIPE_INDEXES_ARRAY_CUISINE_2, ALL_RECIPES_ARRAY_CUISINE_2, cuisines_array[x], cuisines_array[y])
        csvfile_2.close()
        csvfile_1.close()
print("--- %s seconds ---" % (time.time() - start_time))