#1 Implement an In-Place Version of Quick Sort
def in_place_quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)
        in_place_quick_sort(arr, low, p - 1)
        in_place_quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

test_arr = [64, 34, 25, 12, 22, 11, 90]
in_place_quick_sort(test_arr)
print("In-Place Quick Sort Result:", test_arr)

#2 Modify Bubble Sort to Stop Early
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = optimized_bubble_sort(test_arr.copy())
print("Optimized Bubble Sort Result:", sorted_arr)

#3 Implement a Hybrid Sorting Algorithm
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if high - low < 10:  
        insertion_sort(arr, low, high)
    else:
        if low < high:
            p = partition(arr, low, high)
            hybrid_quick_sort(arr, low, p - 1)
            hybrid_quick_sort(arr, p + 1, high)

test_arr = [64, 34, 25, 12, 22, 11, 90]
hybrid_quick_sort(test_arr)
print("Hybrid Quick Sort Result:", test_arr)

#4 Create a Visualization of Sorting Algorithms
import matplotlib.pyplot as plt
import numpy as np

def visualize_bubble_sort(arr):
    n = len(arr)
    plt.ion()
    fig, ax = plt.subplots()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            ax.clear()
            ax.bar(range(len(arr)), arr, color='blue')
            plt.pause(0.05)
    plt.ioff()
    plt.show()

test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_bubble_sort(test_arr.copy())
