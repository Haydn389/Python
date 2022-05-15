import sys
data0 = input().split()   #str
data1 = sys.stdin.readline().split() #str

# data0 = int(input().split()) #안됨
# data1 = int(sys.stdin.readline().split()) #안됨

data2 = list(map(int,input().split()))    #int
data3 = list(map(int,sys.stdin.readline().split()))   #int


print(data0)
print(data1)
print(data2)
print(data3)