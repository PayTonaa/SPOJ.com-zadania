import random

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    left = []
    middle = []
    right = []

    for element in array:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)

    return quicksort(left) + middle + quicksort(right)

def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    array = [random.randint(1, 100) for i in range(10)]
    sorted_array = quicksort(array)

    print("Original array:", array)
    print("Sorted array:", sorted_array)

    value = random.randint(1, 100)
    index = binary_search(sorted_array, value)

    if index == -1:
        print("Value", value, "not found in the array.")
    else:
        print("Value", value, "found at index", index)
