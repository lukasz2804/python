'''
ciag fibbonachiego
'''

def fib(a):
    x,y=1,0
    for z in range(a -1):

        if(z%2!=0):
            x = x + y
            print x
        else:
            y = x + y
            print y
        if z==0:
            y=1
fib(16)