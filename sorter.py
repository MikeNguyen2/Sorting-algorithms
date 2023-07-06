import numpy as np

def sort(unsorted_array):
    sorted_array = np.sort(unsorted_array)
    return sorted_array

def bubble_sort(unsorted_array): 
    while True:
        temp = -1
        for j in range(len(unsorted_array)-1):
            sorted_array = unsorted_array.copy()
            if sorted_array[j] > sorted_array[j+1]:
                temp = sorted_array[j]
                sorted_array[j] = sorted_array[j+1]
                sorted_array[j+1] = temp
        if temp == -1:
            break
    return unsorted_array

def bubble_sort_step(unsorted_array): 
    temp = -1
    for j in range(len(unsorted_array)-1):
        if unsorted_array[j] > unsorted_array[j+1]:
            temp = unsorted_array[j]
            unsorted_array[j] = unsorted_array[j+1]
            unsorted_array[j+1] = temp
    return unsorted_array, temp > 0

def merge(left_array, right_array):
    i,j=0,0
    sorted_array = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j += 1

    while i < len(left_array):
        sorted_array.append(left_array[i])
        i += 1

    while j < len(right_array):
        sorted_array.append(right_array[j])
        j += 1

    return sorted_array

def merge_sort(unsorted_array):
    length = len(unsorted_array)
    if(length == 1):
        return unsorted_array
    else:
        left = merge_sort(unsorted_array[:length//2])
        right = merge_sort(unsorted_array[length//2:])
        sorted_array = merge(left, right)
        return sorted_array

def quick_sort_pivot(unsorted_array, lower, upper):
    sorted_array = unsorted_array.copy()
    counter = lower-1
    pivot_value = sorted_array[upper]
    for i in range(lower, upper):
        if sorted_array[i] <= pivot_value:
            counter += 1
            sorted_array[counter], sorted_array[i] = sorted_array[i], sorted_array[counter]
    sorted_array[counter+1], sorted_array[upper] = sorted_array[upper], sorted_array[counter+1]
    return sorted_array, counter+1

def  quick_sort_loop(unsorted_array, lower, upper):
    if lower < upper: 
        sorted_array, pivot = quick_sort_pivot(unsorted_array, lower, upper)
        sorted_array_left = quick_sort_loop(sorted_array, lower, pivot-1)
        sorted_array_right = quick_sort_loop(sorted_array, pivot+1, upper)
        #print(sorted_array_left[:pivot] ,sorted_array_right[pivot:], pivot)
        return [*sorted_array_left[:pivot], *sorted_array_right[pivot:]]
    return unsorted_array

def quick_sort(unsorted_array):
    print(unsorted_array)
    sorted_array = quick_sort_loop(unsorted_array, 0, len(unsorted_array)-1)
    return sorted_array

def counting_sort(unsorted_array, digit):
    count_array = [0]*10
    for i in range(len(unsorted_array)):
        value = int((unsorted_array[i] // (10**digit)) % 10)
        count_array[value] += 1

    for i in range(1,10):
        count_array[i] += count_array[i-1]

    sorted_array = unsorted_array.copy()
    for i in range(len(unsorted_array)):
        j = len(unsorted_array) - i - 1
        value = unsorted_array[j]
        place = int((unsorted_array[j] // (10**digit)) % 10)
        count_array[place]-= 1
        new_place = count_array[place]
        sorted_array[new_place] = value
    
    return sorted_array

def radix_sort(unsorted_array): 
    max_value = max(unsorted_array)
    digit = 0
    sorted_array = unsorted_array.copy()
    while max_value > 0:
        sorted_array = counting_sort(sorted_array, digit)
        digit += 1
        max_value /= 10
       
    return sorted_array

if __name__ == "__main__":
    unsorted_array = np.random.randint(1,100,100)
    #unsorted_array = [7,9,1,3,2,4,0,6,5,8,8,8,88,8,888,9,8,88,]
    sorted_array = quick_sort(unsorted_array)
    print(sorted_array)