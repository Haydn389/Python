from heapq import heappush,heappop,heapify
def make_max(heap):
    res=[]
    for i in heap:
        heappush(res,h)
        
def make_min(heap):
    res=[]
    for i in heap:
        heappush(res,h)
        

def solution(operations):
    h=[]
    for c in operations:
        oper=c.split()[0]
        num=int(c.split()[1])
        if oper=="I":
            heappush(h,num)    
        else:
            if h:
                if num==1:#최댓값 삭제
                    # res=h[:]
                    # res.sort(reverse=True)
                    # h=res[1:]
                    # heapify(h)
                    h.pop()
                else:#최솟값 삭제
                    heappop(h)
    
    if h:
        answer= [max(h),min(h)]
        # answer= [h.pop(),heappop(h)]
    else:
        answer=[0,0]
    return answer