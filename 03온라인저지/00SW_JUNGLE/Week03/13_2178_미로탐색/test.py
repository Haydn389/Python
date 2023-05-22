import time
s1=time.process_time()
a=[-1*i for i in range(1,9000000)]
sum=0
for j in a:
    if j<0:
        sum+=(-j)
    else:
        sum+=j
print(sum)
s2=time.process_time()
sum=0
for j in a:
    sum+=abs(j)
s3=time.process_time()

print(s2-s1)
print(s3-s2)
print(s2-s1-s3+s2)