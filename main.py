def merge(arr, start, mid, end):
    start2 = mid + 1
    if (arr[mid] <= arr[start2]):
        return
    while (start <= mid and start2 <= end):
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value
            start += 1
            mid += 1
            start2 += 1

def mergesort(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr
import random

def create_random_array(length, range_max):
    return [random.randint(0, range_max) for _ in range(length)]

maxvalue = 20000
length = 10000


print(mergesort(create_random_array(length, maxvalue), 0, length - 1))