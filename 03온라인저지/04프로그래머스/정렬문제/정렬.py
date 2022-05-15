def solution(array, commands):
    l=len(commands)
    answer = []
    for i in range(l):
        s=commands[i][0]-1
        e=commands[i][1]
        k=commands[i][2]
        new=array[s:e]
        new.sort()
        answer.append(new[k-1])
    

    return answer