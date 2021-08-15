import math

#insertion
def insertion(array) :
    for i in range(1, len(array)) :
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key :
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

# merge sort
def mergeSort(array, p, r) :
    if p < r :
        q = math.floor((p + r)/2)
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, (p-1), q, r)
    return array

# merge
def merge(array, p, q, r) :
    arrayL = array[p:q]
    arrayR = array[q:r]
    arrayL.append(float('inf'))
    arrayR.append(float('inf'))
    i = 0
    j = 0
    for k in range (p,r) :
        if arrayL[i] <= arrayR[j] :
            array[k] = arrayL[i]
            i = i + 1
        else :
            array[k] = arrayR[j] 
            j = j + 1
    return array

#main
def main() :
    array = [72, 74, 23, 77, 11, 45, 67, 78, 23, 34, 123, 115]
    print("Unsorted array", array)
    print("Insertion sort array", insertion(array))
    print("Merge sort array", mergeSort(array, 1, len(array)))
    
main()