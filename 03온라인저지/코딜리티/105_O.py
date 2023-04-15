import sys
input = sys.stdin.readline

def largest_square_tile_side_length(m, n):
    # Calculate the maximum number of 2*2 tiles that can be used to form a square
    new_n=m//4+n
    maxlen1=int(new_n**(1/2))*2
    new_m=m%4+(new_n-(maxlen1//2)**2)*4
    if new_m>= maxlen1*2+1:
        maxlen1+=1
    return maxlen1

M,N=map(int,input().split())

print(largest_square_tile_side_length(M,N))