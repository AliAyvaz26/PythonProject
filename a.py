a = int(input())
b = int(input())
def ekok(c,d):
    while True:
        if c > d:
            d  =  d + b
            if c == d:
                print(c)
                break
        if c < d:
            c  = c + a
            if c == d:
                print(d)
                break
ekok(a,b)