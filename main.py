# Sokarak Sıralama Algoritması

def InsertionSort(array):
    i = 0
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            araci = array[j]
            array[j] = array[j - 1]
            array[j - 1] = araci
            j += 1
        i += 1

    print(array)


InsertionSort([1, 5, 3, 8, 0, 4, 8])