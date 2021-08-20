def bubblesort(collection):
    '''
    Two loops: one is in i [len(collection)-1, -1, -1]; another is in [0, i]
    put the largest in the [i+1]
    :param collection:
    :return: sorted collection
    '''
    n = len(collection)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if collection[j] > collection[j+1]:
                collection[j+1], collection[j] = collection[j], collection[j+1]
    return collection


def selectionsort(collection):
    '''
    two loops: one is in i [0, length-1]; another is in j [i+1, length-1]
    put the smallest in the position [i]
    :param collection: mutable collection
    :return: sorted collection
    '''

    n = len(collection)
    for i in range(n):
        least = i
        for j in range(i+1, n, 1):
            if collection[j] <collection[least]:
                least =j
        collection[i], collection[least] = collection[least], collection[i]
    return collection


def insertsort(collection):
    '''
    Two loops: one is in i [1, length-1]; another is in j [0,i-1]
    insert the value of i index into j position and move every element one index up
    :param collection: mutable collection
    :return: sorted collection
    '''

    n = len(collection)
    for i in range(1,n):
        temp  = None
        for j in range(i):
            if temp is None and collection[i] < collection[j]:
                temp = collection[i]
                collection[(j + 1):(i+1)] = collection[(j):(i)]
                collection[j] = temp
                break

    return collection



def quicksort(collection):
    '''
    Use the last element of a list as key constantly split the data into two lists: the first is smaller
    than the key and the second is larger than the key until one element.  Merge the the first, key and second together
    under three scenarios
    :param collection:
    :return:
    '''


    def splitdata(collection):
        key = collection[-1]
        firstlist, lastlist = [], []
        length = len(collection)
        for i in range(length-1):
            if collection[i] < key:
                firstlist.append(collection[i])
            else:
                lastlist.append(collection[i])
        return firstlist, key, lastlist

    n = len(collection)
    if n==1:        return list(collection)
    elif n ==0:
        return print('List is empty')
    else:
        firstlist, key, lastlist = splitdata(collection)
        if len(firstlist) == 0:
            return [key] + quicksort(lastlist)
        if len(lastlist) == 0:
            return quicksort(firstlist) + [key]
        else:
            return quicksort(firstlist) + [key] + quicksort(lastlist)




def mergesort(collection):
    '''
    Constantly split in the midpoint of a list until one element
    Then join two sorted lists together
    :param collection:
    :return:
    '''

    n = len(collection)

    if n > 1:
        midpoint =n // 2
        firsthalf = mergesort(collection[:midpoint])
        secondhalf = mergesort(collection[midpoint:])

        fn = len(firsthalf)
        sn = len(secondhalf)
        if firsthalf[fn-1] <= secondhalf[0]:
            return firsthalf+secondhalf
        else:
            i = j = k = 0

            while i<fn and j <sn:
                if firsthalf[i] < secondhalf[j]:
                    collection[k] = firsthalf[i]
                    i += 1
                else:
                    collection[k] = secondhalf[j]
                    j += 1
                k += 1
            while i < fn:
                collection[k] = firsthalf[i]
                i += 1
                k += 1
            while j < sn:
                collection[k] = secondhalf[j]
                j += 1
                k += 1

    return collection


def maxheap(collection, i, heapsize):
    left = 2*i +1
    right = 2*i +2
    largest = i
    if left< heapsize and collection[left]>collection[largest]:
        largest = left
    if right< heapsize and collection[right]>collection[largest]:
        largest = right
    if largest != i:
        collection[i], collection[largest] = collection[largest], collection[i]
        return maxheap(collection, largest, heapsize)


def heapsort(collection):
    '''
    Idea:
    1. Build a max(min) heap function;
    2. Run max-heap function
    3. Run a cycle until the list is empty. In each cycle, build a max heap and extact the maximum
    :param collection:
    :return:
    '''


    n = len(collection)
    for i in range((n//2)-1, -1, -1):
        maxheap(collection, i, n)

    for j in range(n-1, 0, -1):
        collection[j], collection[0] = collection[0], collection[j]
        maxheap(collection, 0, j)

    return collection





#l1 = insertsort([3,5,2,1,4,3.5, 8])
#l2 = mergesort([3,5,2,1,4,3.5, 8])
l3 = heapsort([3,5,2,1,4,3.5, 8])


