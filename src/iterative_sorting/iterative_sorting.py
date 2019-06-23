# TO-DO: Complete the selection_sort() function below

# Selection Sort = Looping through the array to find the lowest value

# Loop through array and find lowest value
# Move that value to the beginning of the array
# Loop through again excluding what has been sorted already
# place the next value at the next position from the start of the array

# arr[0:10]
# arr[1:10]
# arr[2:10] etc...


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element

        cur_index = i
        smallest_index = cur_index

        # (hint, can do in 3 loc)
        # TO-DO: swap
        # print(cur_index, smallest_index)

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

                # print("smallest index", smallest_index)

        x = arr[smallest_index]
        # print("x", x)

        arr[smallest_index] = arr[i]
        arr[i] = x

    return arr


testArr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 8]
# print("\n\n______________________________\n\n", selection_sort(testArr),
#   "\n\n______________________________\n\n")

# TO-DO:  implement the Bubble Sort function below

# Bubble Sort =  Iterates through the array Swapping adjacent elements that are out of order

# Loop through the array
# Check from your current index if the next index is smaller
# If it is smaller then swap the value of the current index with the next index.


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            # print(i, j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort(testArr))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
