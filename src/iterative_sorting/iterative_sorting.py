# TO-DO: Complete the selection_sort() function below
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


testArr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 1818, 1231, 2, 3, 5]
print("\n\n______________________________\n\n", selection_sort(testArr),
      "\n\n______________________________\n\n")
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
