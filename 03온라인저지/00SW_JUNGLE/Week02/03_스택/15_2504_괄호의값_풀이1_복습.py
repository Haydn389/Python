# https://dev-dain.tistory.com/149
s = input()
# s = "(()[[]])([])"
stack = []
temp = 1
res = 0

# for c in s를 하면 안 되고 길이로 돌아야 함
for i in range(len(s)):
    if s[i] == "(":
        temp *= 2
        stack.append(s[i])
    elif s[i] == "[":
        temp *= 3
        stack.append(s[i])
    elif s[i] == ")":
        if len(stack) == 0 or stack[-1] == "[":  # 비어있거나 top 괄호와 짝이 안맞으면
            res = 0
            break
        if s[i-1] == "(":            # 직전에 입력된 괄호와 짝이 맞다면 ()괄호가 닫히면
            res += temp
        temp //= 2
        stack.pop()
    else:  # "]"
        if len(stack) == 0 or stack[-1] == "(":  # 비어있거나 top 괄호와 짝이 안맞으면
            res = 0
            break
        if s[i-1] == "[":  # 직전에 입력된 괄호와 짝이 맞다면, []괄호가 닫히면
            res += temp
        temp //= 3
        stack.pop()
if len(stack) != 0:  # 모든 계산 완료 후 stack이 비어있지 않으면 잘못된 괄호이므로
    res = 0
print(res)
