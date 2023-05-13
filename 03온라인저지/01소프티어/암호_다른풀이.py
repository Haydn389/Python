import sys

msg = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

board = []
for k in key:
    if k not in board:
        board.append(k)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for alpha in alphabet:
    if alpha not in board:
        board.append(alpha)

nboard = []
while board:
    arr = []
    for i in range(5):
        arr.append(board.pop(0))
    nboard.append(arr)

while True:
    flag = True
    msg_arr = [msg[i:i+2] for i in range(0, len(msg), 2)]
    for i in range(0, len(msg), 2):
        m = msg[i:i+2]
        if len(m) == 2 and m[0] == m[1]:
            flag = False
            if m[0] != 'X':
                msg = msg[:i+1] + 'X' + msg[i+1:]
            else:
                msg = msg[:i+1] + 'Q' + msg[i+1:]
            break
    if flag: 
        break
if len(msg) % 2 != 0: 
    msg += 'X'

nmsg_arr = [msg[i:i+2] for i in range(0, len(msg)-1, 2)]
answer = ''
for m in nmsg_arr:
    step1, step2 = False, False
    for b in nboard:
        if m[0] in b and m[1] in b:
            idx1, idx2 = b.index(m[0]), b.index(m[1])
            answer += b[(idx1+1)%5] + b[(idx2+1)%5]
            step1 = True
    if not step1:
        for j in range(5):
            arr = [nboard[i][j] for i in range(5)]
            if m[0] in arr and m[1] in arr:
                idx1, idx2 = arr.index(m[0]), arr.index(m[1])
                answer += arr[(idx1+1)%5] + arr[(idx2+1)%5]
                step2 = True
    if not step1 and not step2:
        first, second = None, None
        for i in range(5):
            for j in range(5):
                if nboard[i][j] == m[0]:
                    first = (i, j)
                elif nboard[i][j] == m[1]:
                    second = (i, j)
        answer += nboard[first[0]][second[1]] + nboard[second[0]][first[1]]
print(answer)