# This algorithms were created based on the information
# exctracted from the next two links
#   https://en.wikipedia.org/wiki/Big_O_notation 
#   https://en.wikipedia.org/wiki/Time_complexity#Constant_time

import random

# Constant or O(1)
def is_even(num):
    """Determine if a number is even or odd
    Parameters:
        num (int): whatever interger value
    Returns:
        boolean: true if the num is even, false if the num is odd"""
    return (num % 2 == 0)

# lineal or O(n)
def find_element_index_in_unsorted_list(list,element):
    """Given a list and an element from the list returns its position
    Parameters:
        list (list<?>): a sorted list of values
        element (?): whatever element existent in the list
    Returns:
        int: the position in the list or -1 if the item does not exist in the list"""
    index = 0

    while list[index] != element:
        index += 1
        
        if list[index] == element:
            return index
    
    return -1

# Logarithmic or O(log n)
def find_element_index_in_sorted_list(list,element):
    """Given a list of sorted elements and an element from the list returns its position
    Parameters:
        list (list<int>): a sorted list of values
        element (int): whatever element existent in the list
    Returns:
        int: the position in the list or -1 if the item does not exist in the list"""
    max = len(list) - 1
    mid = 0
    min = 0
  
    while min <= max: 
        mid = (max + min)

        if list[mid] < element: # Check if x is present at mid 
            min = mid + 1
        elif list[mid] > element: # If x is greater, ignore left half 
            max = mid - 1
        else: # If x is smaller, ignore right half 
            return mid 
  
    return -1 # If we reach here, then the element was not present

# Quadratic or О(n**2)
def bubble_sort(list):
    """Given a list of unsorted numbers this function sort the list with the Bubble sort algorithm https://en.wikipedia.org/wiki/Bubble_sort
    Parameters:
        list (list<int>): unsorted list of numbers
    Returns:
        list: with sorted elements"""
    list_size = len(list)

    while list_size >= 1:
        last_list_element = 0

        for i in range(1,list_size):

            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
                last_list_element = i
                
        list_size = last_list_element

    return list

# Log lineal or O(n log n)
def merge_sort(list):
    """Given a list of unsorted numbers this function sort the list with the Merge sort algorithm https://en.wikipedia.org/wiki/Merge_sort
    Parameters:
        list (list<int>): unsorted list of numbers
    Returns:
        list: with sorted elements"""
    if len(list) > 1:
        mid = len(list) // 2
        left_side = list[:mid]
        right_side = list[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        # iterators
        i = 0
        j = 0
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list[k] = left_side[i]
                i += 1
            else: 
                list[k] = right_side[j]
                j += 1
            
            k += 1
        
        while i < len(left_side):
            list[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(right_side):
            list[k] = right_side[j]
            j += 1
            k += 1

    return list

def knapsack_problem(size, weights, values, n):
    if n == 0 or size == 0:
        return 0
    
    if weights[n - 1] > size:
        return knapsack_problem(size, weights, values, n -1)
    
    return max(values[n - 1] + knapsack_problem(size - weights[n -1 ],weights, values, n - 1),
                knapsack_problem(size, weights, values, n - 1))

if __name__ == "__main__":
    print(is_even(100))
    print(find_element_index_in_unsorted_list(random.sample(range(0, 100), 100),10))
    print(find_element_index_in_sorted_list(list(range(0,100,2)),4))
    print(bubble_sort(random.sample(range(0, 10), 10)))
    print(merge_sort(random.sample(range(0, 10), 10)))
    size = 30
    values = [60, 100, 120]
    weights = [10, 20, 30]
    n = len(values)
    print(knapsack_problem(size, weights, values, n))