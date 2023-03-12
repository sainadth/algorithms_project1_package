import csv
import time
import json
import pandas

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

def comp(x, y, col):
    for i in col[1:]:
        if x[i] < y[i]: return False
        elif x[i] >= y[i]: return True
    return False

#############################################################################################################
# Data Filtering
#############################################################################################################
def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    df = pandas.read_csv("imdb_dataset.csv")# Load the imdb_dataset.csv dataset
    # print(df)
    if(num==1):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        df_year = df.loc[df['startYear'].isin([i for i in range(1941, 1956)])]
        #filter(lambda p : yearFilter(p[3]), df)#Store your filtered dataframe here
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)
    if(num==2):
        #NEED TO CODE 
        #Implement your logic here for Filtering data based on genres (genres are either ‘Adventure’ Adventureor ‘Drama’)
        df_genres = df[df['genres'].isin(['Adventure', 'Drama'])]#Store your filtered dataframe here
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
    if(num==3):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primaryProfession (if primaryProfession column contains
        #substrings {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        df_professions = df[df['primaryProfession'].str.contains('|'.join(['assistant_director', 'casting_director', 'art_director', 'cinematographer']))]#Store your filtered dataframe here
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
    if(num==4):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primary Names which start with vowel character.
        df_vowels = df[df['primaryName'].str[0].str.lower().isin(['a', 'e', 'i', 'o', 'u'])]
        #Store your filtered dataframe here
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)


#############################################################################################################
#Quick Sort
#############################################################################################################
def pivot_element(arr):
    #CODE For identifiying the pivot element
    return len(arr)//2
def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the result of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        # An array of 0 or 1 elements is already sorted
        return arr
    else:
        # Choose a pivot element and partition the array around it
        pivot = pivot_element(arr)
        left = []
        right = []
        for i in range(len(arr)):
            if(i == pivot):
                continue
            if(comp(arr[i], arr[pivot], columns)):
                right.append(arr[i])
            else:
                left.append(arr[i])
    
    left_sorted = quicksort(left, columns)
    right_sorted = quicksort(right, columns)

    #NEED TO CODE
    #Implement Quick Sort Algorithm
    #return Sorted array
    return left_sorted + [arr[pivot]] + right_sorted
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    # print(arr)
    for i in range(len(arr)):
        minInd = i
        for j in range(i + 1, len(arr)):
            if(comp(x=arr[j], y=arr[minInd], col=columns)):
                minInd = j
        if(minInd != i):
            temp = arr[i]
            arr[i] = arr[minInd]
            arr[minInd] = temp
    # print(arr)
    #NEED TO CODE
    #Implement Selection Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Heap Sort
#############################################################################################################
def max_heapify(arr, n, i, columns):
    """
    arr: the input array that represents the binary heap
    n: The number of elements in the array
    i: i is the index of the node to be processed
    columns: The columns to be used for comparison

    The max_heapify function is used to maintain the max heap property
    in a binary heap. It takes as input a binary heap stored in an array,
    and an index i in the array, and ensures that the subtree rooted at
    index i is a max heap.
    """
    pass


def build_max_heap(arr, n, i, columns):
    """
    arr: The input array to be transformed into a max heap
    n: The number of elements in the array
    i: The current index in the array being processed
    columns: The columns to be used for comparison

    The build_max_heap function is used to construct a max heap
    from an input array.
    """
     # Find the largest among root, left child and right child
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and comp(arr[left], arr[largest], columns):
        largest = left

    if right < n and comp(arr[right], arr[largest], columns):
        largest = right

    # If the largest is not the root then swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        build_max_heap(arr, n, largest, columns)
    #NEED TO CODE
    #Implement heapify algorithm here

def heap_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    n = len(arr)

    # Build a max heap.
    for i in range(n//2 - 1, -1, -1):
        build_max_heap(arr, n, i, columns)

    # Extract elements from the heap one by one.
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum value) of the heap with the last element of the heap.
        arr[i], arr[0] = arr[0], arr[i]

        # build_max_heap the reduced heap to maintain the heap property.
        build_max_heap(arr, i, 0, columns)
    #NEED TO CODE
    #Implement Heap Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Shell Sort
#############################################################################################################
def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    # Start with a large gap, then reduce the gap until it is 1
    gap = len(arr) // 2
    while gap > 0:
        # Do a gapped insertion sort for this gap size
        for i in range(gap, len(arr)):
            # Add arr[i] to the elements that have been gap sorted
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and comp(arr[j - gap], temp, columns):
                arr[j] = arr[j - gap]
                j -= gap
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        # Calculate the next gap to use
        gap = gap // 2
    #NEED TO CODE
    #Implement Shell Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Merge Sort
#############################################################################################################
def merge(left, right, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """
    i = j = 0
    res = []
    while(i < len(left) and j < len(right)):
        if(comp(left[i], right[j], columns)):
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    
    while(i < len(left)):
        res.append(left[i])
    
    while(j < len(right)):
        res.append(right[j])
    return res
    #NEED TO CODE
    #Implement merge Logic
    #return Sorted array

def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the result of the merge operation as the final sorted 2D array.
    """
    #NEED TO CODE
    if len(data) <= 1:
        return data
    mid = len(data)//2#Mid value
    #Need to Code
    left = merge_sort(data[:mid], columns)
    right = merge_sort(data[mid:], columns)
    #Implement Merge Sort Algorithm
    #return Sorted array
    return merge(left, right, columns)
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):

    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    for i in range(len(arr)):
        j = i
        while(j > 0):
            if(comp(arr[j - 1], arr[j], columns)):
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            j -= 1
    #NEED TO CODE
    #Insertion Sort Implementation
    #Return : List of tconst values which are obtained after sorting the dataset.
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    """
    # file_path: a string representing the path to the CSV file
    # columns: a list of strings representing the columns to sort the 2D array on
    # select: an integer representing the sorting algorithm to be used

    # colum_vals: is a list of integers representing the indices of the specified columns to be sorted.

    # data: is a 2D array of values representing the contents of the CSV file, with each row in
    the array corresponding to a row in the CSV file and each element in a row corresponding to a value
    in a specific column.

    More Detailed Description:

    df= #read imdb_dataset.csv data set using pandas library

    column_vals = #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).
    """
    #NEED TO CODE
    #Read imdb_dataset.csv
    #write code here Inorder to read imdb_dataset
    df = pandas.read_csv("imdb_dataset.csv")
    #read imdb_dataset.csv data set using pandas library

    column_vals = [0] + [column_names.index(i) for i in columns]
    #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = df.values.tolist()
    #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).

#############################################################################################################
# Donot Modify Below Code
#############################################################################################################
    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
