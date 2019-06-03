# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print("index i", i)
        # TO-DO: find next smallest element
        smallest_element = arr[i]
        # (hint, can do in 3 loc)
        # TO-DO: swap
        for j in range(i, len(arr)):
            if arr[j] < smallest_element:
                print("Smallest Element Before", smallest_element)
                smallest_element = arr[j]
                print("Smallest Element After", smallest_element)
        x = arr[smallest_element]
        print("x", x)
        arr[smallest_element] = arr[i]
        print("smallest_element", arr[smallest_element])
        arr[i] = x
        print("print arr", arr)

    return arr


print("\n\n______________________________\n\n", selection_sort(
    [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]), "\n\n______________________________\n\n")
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
