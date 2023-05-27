def solution(brown, yellow):
    total=brown+yellow
    for i in range(1,total):
        if total%i==0:
            if (i-2)*(total//i-2)==yellow:
                row,col=i,total//i
                break
    if(row<=col):
        row,col=col,row

    return [row,col]    