
#[sol1과 sol2 차이점]
#sol2의 경우 전역변수 plus, minus, mul, div에 직접 접근하여 oper갯수 상태를 계속해서 update하기 때문에
#이전 depth에서 다음 depth의 재귀함수 호출 후 basecase를 만나고 반환되어 돌아옴과 동시에 원래상태로 돌려줘야 한다.
#따라서 매번 재귀함수 호출이후에 +=연산을 수행한다.

#반면 sol2의 경우 매개변수로 현재상태의 연산자 갯수를 넘겨주기 때문에 재귀함수가 호출될 때마다
#해당 depth의 oper 갯수 상태를 가지고 있다. 따라서 base case를 만나고 반환된 이후 원래 호출된 자리로 돌아와도
#직전 depth의 oper 갯수 상태가 그대로 보존되어 있기 때문에 sol1처럼 

#sol2가 더 빠르다
import sys
n = int(sys.stdin.readline()) 
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, mul, div): 
    global maximum, minimum
    if depth == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return 
    
    if plus != 0:
        dfs(depth+1, total + A[depth] , plus - 1, minus, mul, div)
    if minus != 0:
        dfs(depth+1, total - A[depth], plus, minus -1, mul, div)
    if mul != 0:
        dfs(depth+1, total * A[depth], plus, minus, mul-1, div)
    if div != 0:
        dfs(depth+1, int(total/A[depth]) ,plus , minus, mul, div-1)

dfs(1, A[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)