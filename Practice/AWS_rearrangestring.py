'''
Rearrange characters
Show Topic Tags           Amazon
Given a string with repeated characters, task is to rearrange characters in a string such that no two adjacent
characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.


Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case contains a single line containing a string of lowercase english alphabets.

Output:
For each test case in a new line print 1 if the generated sting doesn't contains any same adjacent characters, else if
no such string is possible to be made print 0.
Constraints:
1<=T<=100
1<=length of string<=600

Example:
Input:
3
geeksforgeeks
bbbabaaacd
bbbbb

Output:
1
1
0

Prerequisite : priority_queue.

The idea is to put highest frequency character first (a greedy approach). We use a priority queue (Or Binary Max Heap)
and put all characters and ordered by their frequencies (highest frequency character at root). We one by one take
highest frequency character from the heap and add it to result. After we add, we decrease frequency of the character
and we temporarily move this character out of priority queue so that it is not picked next time.

We have to follow the step to solve this problem, they are:
1. Build a Priority_queue or max_heap, pq that stores characters and their frequencies.
…… Priority_queue or max_heap is built on the bases of frequency of character.
2. Create a temporary Key that will used as the previous visited element ( previous element in resultant string.
Initialize it { char = ‘#’ , freq = ‘-1’ }
3. While pq is not empty.
….. Pop an element and add it to result.
….. Decrease frequency of the popped element by ‘1’
….. Push the previous element back into the priority_queue if it’s frequency > ‘0’
….. Make the current element as previous element for the next iteration.
4. If length of resultant string and original, print “not possible”. Else print result.


'''

class PriQueue:

    def __init__(self, v, k):
        self.q = v
        self.k = k



def pq(a):
    a = a.lower()
    n = len(a)
    pq = []
    charlist = 'abcdefghijklmnopqrstuvwsyz'
    count = [0]*26
    for i in range(n):
        if a[i] == charlist[ord(a[i]) -ord('a')]:
            count[ord(a[i]) -ord('a')] += 1
    for i in range(26):
        if count[i] > 0:
            temp = PriQueue(charlist[i], count[i])
            pq.append(temp)

    return pq


a = 'seftthtelk'

def arrangestr(a):
    str = ''
    q = pq(a)
    s = sorted(q, key = lambda x: x.k, reverse = True)
    prev = None
    while len(s) >0:
        temp = s.pop(0)
        str = str + temp.q
        temp.k -= 1

        if temp.k > 0:
            s.append(temp)
    if len(str) == len(a):
        return str
    else:
        return -1


arrangestr(a)











