from asyncio import base_tasks
from itertools import count
import math
import time
import random
import matplotlib.pyplot as plt

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, b, arr):
    k = math.ceil(math.log(univsize, 2) / math.log(b, 2))
    for elt in arr:
        elt[1] = [elt[1], BC(elt[0], b, k)]

    for i in range(k):
        for j in range(len(arr)):
            arr[j][0] = arr[j][1][1][i]
        arr = countSort(b, arr)

    for i in range(len(arr)):
        sum = 0
        for j in range(k):
            sum += arr[i][1][1][j] * (b ** j)
        arr[i][0] = sum
        arr[i][1] = arr[i][1][0]
    
    return arr

def generate(length, univ):
    arr = []
    for i in range(2 ** length):
        arr.append([random.randint(0, 2 ** univ - 1), 0])
    return arr

def experiment():
    for length in range(1, 3):
        merge_arr = []
        count_arr = []
        radix_arr = []
        min_arr = []
        color_arr = []

        for univ in range(1, 21):

            merge_total = 0
            for i in range(10):
                test_arr = generate(length, univ)
                start = time.time()
                mergeSort(test_arr)
                merge_total += time.time() - start

            merge_arr.append(merge_total / 10)

            count_total = 0
            for i in range(10):
                test_arr = generate(length, univ)
                start = time.time()
                countSort(2 ** univ, test_arr)
                count_total += time.time() - start

            count_arr.append(count_total / 10)

            radix_total = 0
            for i in range(10):
                test_arr = generate(length, univ)
                start = time.time()
                radixSort(2 ** univ, 10, test_arr)
                radix_total += time.time() - start

            radix_arr.append(radix_total / 10)
            
            small = min(merge_total, count_total, radix_total)

            min_arr.append(small / 10)
            
            if small == merge_total:
                color_arr.append("red")
            elif small == count_total:
                color_arr.append("blue")
            else:
                color_arr.append("green")

        plt.figure(1)
        figure, axis = plt.subplots(2, 2)
        axis[0, 0].plot(range(1, 21), merge_arr, color="red")
        axis[0, 0].set_title("Merge Sort")

        axis[0, 1].plot(range(1, 21), count_arr, color="blue")
        axis[0, 1].set_title("Count Sort")

        axis[1, 0].plot(range(1, 21), radix_arr, color="green")
        axis[1, 0].set_title("Radix Sort")

        for i in range(1, 21):
            axis[1, 1].scatter(i, min_arr[i - 1], color=color_arr[i - 1])
        axis[1, 1].set_title("Minimum Sorts")

        plt.setp(axis[-1, :], xlabel='Logarithm Base 2, Universe Size')
        plt.setp(axis[:, 0], ylabel='Runtime (s)')

        left  = 0.15  # the left side of the subplots of the figure
        right = 0.975    # the right side of the subplots of the figure
        bottom = 0.1   # the bottom of the subplots of the figure
        top = 0.9      # the top of the subplots of the figure
        wspace = 0.4   # the amount of width reserved for blank space between subplots
        hspace = 0.5   # the amount of height reserved for white space between subplots
        plt.subplots_adjust(left, bottom, right, top, wspace, hspace)


        plt.savefig('sort' + str(length) + '.png')


# Diagram Creation
experiment()


# Correctness Check
# x = generate(4, 6)
# print("array: ")
# print(x)
# print("merge: ")
# print(mergeSort(x))
# print("count: ")
# print(countSort(2 ** 6, x))
# print("radix: ")
# print(radixSort(2 ** 6, 10, x))