import sys
input=sys.stdin.readline
n,m=map(int,input().split())
find=[]
for _ in range(n):
    find.append(input().rstrip())
use={}
for _ in range(m):
    a,b,c=input().split()
    if a in use:
        use[a].append((int(b),int(c)))
    else:
        use[a]=[(int(b),int(c))]

find.sort()
# print(find)
# print(use)
for i in range(n):
    if find[i] not in use:
        print (f"Room {find[i]}:")
        print ("1 available:")
        print ("09-18")
        if i!=n-1:
            print("-----")
        continue
    temp=sorted(use[find[i]])
    # print(temp)
    ans=[]
    begin=9
    last=18
    # print(temp)
    for j in range(len(temp)):
        s,e=temp[j][0],temp[j][1]
        if begin!=s:
            ans.append((begin,s))
        if j==len(temp)-1:
            if e!=18:
                ans.append((e,18))
        begin=e
    # print(ans)
    if len(ans)==0:
        print (f"Room {find[i]}:")
        print ("Not available:")
        if i!=n-1:
            print("-----")
        continue
    print (f"Room {find[i]}:")
    print (f"{len(ans)} available:")
    for x in ans:
        print(f"{x[0]:02d}-{x[1]}")
    if i!=n-1:
        print("-----")