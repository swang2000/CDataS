##  Check if a string has all unique characters.

def str_unique(str):
    if len(str) > 128:
        return False
    else:
        for i in range(len(str)):
            for j in range(i + 1, len(str)):
                if str[i] == str[j]:
                    return False
        return True


str = 'Iloveyou'
str_unique(str)


# Check if two strings are the permutation of each other

def check_permutation(str1, str2):
    Blist = [False] * len(str1)
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if Blist[i] == False:
                    Blist[i] = True
    if sum(Blist) == len(Blist):
        return True
    else:
        return False



check_permutation('lovely', 'lovley')


# Replace any space with %20 in a string

def replacespace(str, n):
    charstr = list(str[:n])
    for i in range(n):
        if charstr[i] == ' ':
            charstr[i] = '%20'
    return ''.join(charstr)

str = 'Mr John Smith  '
replacespace(str, 13)

# One way: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def editcheck(str1, str2):

    if len(str1) == len(str2) + 1:
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                if str1[i+1] != str2[i]:
                    return False
        return True

    elif len(str1) == len(str2) - 1:
        for i in range(len(str1)):
            if str2[i] != str1[i]:
                if str1[i] != str2[i+1]:
                    return False
        return True

    elif len(str1) == len(str2):
        j = 0
        for i in range(len(str1)):
            if str2[i] != str1[i]:
                j += 1
        if j==1 or j==0:
            return True
        else:
            return False

    else:
        return False


str1, str2 = 'Pale', 'Pale'
editcheck(str1, str2)


#  Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#  column are set to 0.
import numpy as np
def setmatrixzero(m1):
    bm2 = (m1 ==0)
    col = (bm2.sum(axis=0) >0)
    row =  (bm2.sum(axis=1) >0)
    m1[np.array(row), :] = 0
    m1[:, np.array(col),] = 0
    return m1

m1 = np.array([[0,1,2],[3,4,5]])
setmatrixzero(m1)


# String Rotation: Assume you have a method i5Substring which checks ifone word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to isSubstring (e.g., Uwaterbottleuis a rotation ofuerbottlewatU ).

import re

def rotation_check(str, rstr):
    ss = rstr+rstr
    if (len(str) == len(rstr)) & (bool(re.search(str, ss))):
        return True
    else:
        return False

str='Iloveyou'
rstr = 'ouIlovey'
rotation_check(str,rstr)

# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# pg94

import CdataS.Linkedlist as Llist


def removeDup(llist):
    n = llist.root
    set1 = set([llist.root.data])
    while (n is not None) & (n.next_node is not None):
        p = n
        n = p.next_node
        if n.data in set1:
            p.next_node = n.next_node
            llist.size -= 1
        else:
            set1.add(n.data)
    return llist


llist = Llist.LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(2)
llist.add(4)
llist.add(5)
llist.size
removeDup(llist).size



# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Solution 1
import CdataS.Linkedlist as Llist
def PrintKtoLast(llist, k):
    if llist == None:
        return 0

    index = PrintKtoLast(llist.next_node,k) + 1
    if index == k:
        print('The '+str(k) +'th element to the last is '+str(llist.data))

    return index


llist = Llist.LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(2)
llist.add(4)
llist.add(5)

PrintKtoLast(llist.root, 3)



# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
# Hints: #


# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

import CdataS.Linkedlist as Llist
def partition(llist, k):
    if llist == None:
        return llist
    n = llist.root
    L = Llist.LinkedList()
    R = Llist.LinkedList()
    while n.next_node:
        if n.data < k:
            L.add(n.data)
        else:
            R.add(n.data)
        n = n.next_node
    Llast = L.root
    while Llast.next_node:
        Llast = Llast.next_node
    Llast.next_node = R.root
    return L


llist = Llist.LinkedList()
llist.add(1)
llist.add(2)
llist.add(6)
llist.add(8)
llist.add(4)
llist.add(5)

myList = partition(llist, 5)
myList.printL()

# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
import CdataS.Linkedlist as Llist

def addR(list1, list2, llist=Llist.LinkedList(), floor=0):

    if (len(list1) == 0) & (len(list2) == 0):
        if floor == 0:
            return llist
        else:
            llist.append(floor)
            return llist
    elif (len(list1) > 0) & (len(list2) > 0):
        digit = list1.pop() + list2.pop()
        remainder = digit % 10
        llist.append(remainder + floor)
        floor = digit // 10
        return addR(list1, list2, llist, floor)
    elif (len(list1) > 0) & (len(list2) == 0):
        digit = list1.pop()
        remainder = digit % 10
        llist.append(remainder + floor)
        floor = 0
        return addR(list1, list2, llist, floor)
    elif (len(list1) == 0) & (len(list2) > 0):
        digit = list2.pop()
        remainder = digit % 10
        llist.append(remainder + floor)
        floor = 0
        return addR(list1, list2, llist, floor)


def addllist(l1, l2):
    stack1 = []
    stack2 = []
    p_l1 = l1.root
    p_l2 = l2.root
    while p_l1.data:
        stack1.append(p_l1.data)
        if p_l1.next_node:
            p_l1 = p_l1.next_node
        else:
            break
    while p_l2.data:
        stack2.append(p_l2.data)
        if p_l2.next_node:
            p_l2 = p_l2.next_node
        else:
            break
    myList = Llist.LinkedList()
    llist = addR(stack1, stack2, myList)
    return llist


l1 = Llist.LinkedList()
l2 = Llist.LinkedList()
l1.add(6)
l1.add(9)
l1.add(5)

l2.add(2)
l2.add(1)
l2.add(8)
# list1 = stack1
# list2 = stack2


myL = addllist(l1, l2)


def add_test(data=5):
    if data == 0:
        return data
    else:
        return data + add_test(data-1)

add_test()

# Palindrome: Implement a function to check if a linked list is a palindrome.

def check_palindrone(l):
    n = l.size
    res = ispalindrone(l.root, n)
    return res[1]





def ispalindrone(node, n):
    if (n==0) or (node is None):
        return [node, True]
    if n == 1:
        return [node.next_node, True]
    res = ispalindrone(node.next_node, n-2)
    pa = node.data == res[0].data
    if res[1] & pa:
        return [res.next_node, True]
    else:
        return res







