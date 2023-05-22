def rotate(a):
    return [ list(l) for l in zip(*a[::-1])]

a=[[1,1,0],[0,1,0],[0,0,0]]

print(rotate(a))

