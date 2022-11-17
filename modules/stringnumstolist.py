# example string of nums x="1 17 3 4 9 6 2 7 5 2 5"

def dothething(x): 
    y=x.split(" ") 
    z=set(y) 
    z = sorted(map(int, z)) 
    return z