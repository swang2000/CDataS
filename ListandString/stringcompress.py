'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def stringcompress(a):
    rep = 1
    pre = a[0]
    out = a[0]
    flag = False
    for i, current in enumerate(a[1:]):
        if pre == current:
            rep += 1
            if i == len(a[1:])-1:
                out = out + str(rep)
        else:
            out = out + str(rep) + current
            rep = 1
        pre = current
    return out if len(out) < len(a) else a

a= 'aabcccccaaa'
stringcompress(a)



