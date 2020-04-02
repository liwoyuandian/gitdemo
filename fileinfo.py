# filename: fileinfo.py
x=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
def f(x):
    n=((x*a)-b)*c+d
    return n
m=f(x)
print('The cyphertext is {}.'.format(m))