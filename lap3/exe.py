#1 Linear Search
def linear_search_all(arr, target):   #This function finds all the positions (indices) in an array where a target value appears.
    indices = []
    for i in range(len(arr)): 
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all(test_list, 3)
print(f"Linear Search (all indices): Indices of 3 are {result}")

#2 insertion point
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)   #This function finds the position to insert the target in a sorted list while maintaining order.
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid  
    
    return left  

sorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
insertion_point = binary_search_insertion_point(sorted_list, 3)
print(f"Insertion point for 3 is at index {insertion_point}")

#3 counts number of comparisons
comparison_count_linear = 0

def linear_search_count(arr, target): #This function counts the number of comparisons made to find the target using a linear search.
    global comparison_count_linear
    comparison_count_linear = 0
    for i in range(len(arr)):
        comparison_count_linear += 1
        if arr[i] == target:
            return i
    return -1

comparison_count_binary = 0

def binary_search_count(arr, target):
    global comparison_count_binary
    comparison_count_binary = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        comparison_count_binary += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
linear_search_count(arr, 3)
print(f"Linear Search comparisons: {comparison_count_linear}")
binary_search_count(arr, 3)
print(f"Binary Search comparisons: {comparison_count_binary}")

#4jump search
import math

def jump_search(arr, target):  #Jump search allows for faster searching by "jumping" through sections of a sorted array.
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

# Performance Comparison
def compare_all_searches(arr, target):   #Tests and compares the performance of Linear Search, Binary Search, and Jump Search for a specific target.
    print("Searching for:", target)
    linear_index = linear_search_count(arr, target)
    print(f"Linear Search: Index {linear_index}, Comparisons: {comparison_count_linear}")
    
    binary_index = binary_search_count(arr, target)
    print(f"Binary Search: Index {binary_index}, Comparisons: {comparison_count_binary}")
    
    jump_index = jump_search(arr, target)
    print(f"Jump Search: Index {jump_index}")

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
compare_all_searches(sorted_list, 7)