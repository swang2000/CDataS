'''
Program to validate an IP address
2.7
Write a program to Validate an IPv4 Address.

According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four
decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1
1. split by '.'
2. check if the length of the list is 4;
3. check each element if it is digit;
4. check each element if it is >=0 and <= 255

'''




def chkipaddress(a):
    b = a.split('.')
    if len(b)!= 4:
        return False
    for i in b:
        if i.isdigit() is not True:
            return False
        if int(i)< 0 or (int(i)>255):
            return False
    return True

a ='172.16.254.x'
chkipaddress(a)

