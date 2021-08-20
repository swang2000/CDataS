'''
Stepping Numbers
Show Topic Tags          Amazon
A number is called stepping number if all adjacent digits have an absolute difference of 1, e.g. '321' is a Stepping
Number while 421 is not. Given two integers n and m, find the count of all the stepping numbers in range [n, m].

Examples:

Input : n = 0, m = 21
Output : 13
Stepping no's are 0 1 2 3 4 5 6 7 8 9 10 12 21

Input : n = 10, m = 15
Output : 2
Stepping no's are 10, 12
'''

def stepping(n, m, i):
    q = []
    q.append(i)
    while len(q)>0:
        steps = q.pop(0)
        if steps<= m and (steps>=n):
            print(steps, end= ' ')

        if steps == 0 or (steps> m):
            continue

        lastdig = steps % 10
        stepA = steps*10 + lastdig -1
        stepB = steps*10 + lastdig +1

        if lastdig ==0:
            q.append(stepB)

        elif lastdig ==9:
            q.append(stepA)

        else:
            q.append(stepA)
            q.append(stepB)


def displaysteps(n, m):

    for i in range(0, 10):
        stepping(n, m, i)


displaysteps(0, 21)


