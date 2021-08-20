'''
The algorithms were coded by Victor Wang on Oct 2017 to practise the algorithms
three major search algorithms was programmed as binary, linear, and interpolation

'''

def binarysearch(collection, item):
    '''

    :param collection: must be the sorted collection
    :param item: item inside the collection
    :return: Either index of collection or False if not found
    '''
    n = len(collection)
    left = 0
    right = n-1
    while left <= right:
        midpoint = (left + right) // 2
        if collection[midpoint] == item:
            return midpoint
        elif item > collection[midpoint]:
            left = midpoint +1
        else:
            right = midpoint - 1
    return None

#binarysearch([1,3,5,6,9,10], 6)


def interpolationsearch(collection, item):

    n = len(collection)
    left = 0
    right = n-1

    while (left <= right):
        point = left + (item-collection[left]) * (right - left)/ (collection[right] - collection[left])
        if point <0 or point >= n:
            return None
        else:
            if item == collection[point]:
                return point
            elif item > collection[point]:
                left = point + 1
            else:
                right = point - 1
    return None



interpolationsearch([1,3,5,6,9,10], 6)


