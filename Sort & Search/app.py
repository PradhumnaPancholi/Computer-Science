# Linear search
employees = ['oscar', 'jim', 'dwight', 'phyllis', 'angela', 'andy', 'kevin', 'erin', 'toby', 'stanley', 'creed']

def linear_search(list=[], tar=str):
    for i in range(len(list)):
        if list[i] == tar:
            print('Linear Search: '+ tar + ' found')
            return True
        else:
            i = i + 1
    print('Linear Search: ' + tar + ' not found')
    return False

linear_search(employees, 'kevin')

# ===============================================================================================================================

# Binary search - performed on simple list of int as binary search algorithms can only be ran against sorted list
sorted_list = [1, 2, 3, 4, 5, 7, 10, 14, 17, 18, 20, 23, 25, 28, 31, 32, 34, 37, 38, 39, 42, 54, 55, 56, 57, 64, 74]

def binary_search(list=[], tar=int):
    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if(list[mid] == tar):
            print('Binary Search:  found at index ' + str(mid))
            return True
        else:
            # verify which bound needs to be modified
            if list[mid] < tar:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

    # if not present in array
    print('Binary Search: not found in array')
    return False


binary_search(sorted_list, 25)

# ===============================================================================================================================


# Insertion Sort: better than bubble sort but not very efficient as un able to scale for larger data sets.

unsorted_list = [4, -5,  7, 6, 8, 9, 556, -254, 45, 5, 6, 56, 5, 6, 34, 36, 43, 76, 65]

def insertion_sort(list=[]):
    for i in range(len(list)):
        while list[i - 1] > list[i] and i > 0:  # i > 0 will make it crash while checking first item
            # don't get confused, just optimized syntax to swap values
            list[i], list[i-1] = list[i-1], list[i]
            i = i-1  # important to check with previous item

    return list

print(insertion_sort(unsorted_list))

# ===============================================================================================================================

# Merge Sort: scalable, recursive, uses divide and conquer approach

def merge_sort(list= []):
    if len(list) > 1:  # recursive until array contains only one item.
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        i = 0  # for index of left_list
        j = 0  # for index of right_list
        k = 0  # for index of original list

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list[k] = right_list[j]
                j = j + 1
                k = k + 1

        while i < len(left_list):
            list[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
            list[k] = right_list[j]
            j = j + 1
            k = k + 1
    return list


print(merge_sort(unsorted_list))