import sys
input=sys.stdin.readline

def find(x:int)->int:
    global p
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def union(a:int,b:int)->None:
    global p
    a=find(a)
    b=find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

if __name__=="__main__":
    v,e=map(int,input().split())

    p=[*range(1+v)]
    res=0
    edges=[]
    for _ in range(e):
        a,b,cost=map(int,input().split())
        
        edges.append((a,b,cost))

    edges.sort(key=lambda x:x[2])

    for edge in edges:
        a,b,cost=edge
        if find(a)!=find(b):
            union(a,b)
            res+=cost

    print(res)