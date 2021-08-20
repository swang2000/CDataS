'''
Write you own Power without using multiplication(*) and division(/) operators
2.5
Method 1 (Using Nested Loops)

We can calculate power by using repeated addition.

For example to calculate 5^6.
1) First 5 times add 5, we get 25. (5^2)
2) Then 5 times add 25, we get 125. (5^3)
3) Then 5 time add 125, we get 625 (5^4)
4) Then 5 times add 625, we get 3125 (5^5)
5) Then 5 times add 3125, we get 15625 (5^6)
'''

def powercal(a, b, n=0):
    if b ==1:
        return n
    else:
        if n==0:
            c = a
            n = a
        else:
            c = n
        for i in range(a-1):
            n += c
        return powercal(a, b-1, n)


powercal(5, 6)
