
# Merge Sort Notes - O(n log n) time
# -divide input array into 2 parts
# -sort each part
# -merge the parts back together when the size is 1



# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print("arrA",arrA,"arrB",arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    a = 0
    b = 0

    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b+=1

    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)>1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[:len(arr) // 2:])
        # print("left",left,"right", right)
        arr = merge(left,right) 
        print("arr",arr)
    return arr



arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

















# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


