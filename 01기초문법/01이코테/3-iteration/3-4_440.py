sc=[90,85,77,65,97]
set={2,4}
for i in range(5):
    if i+1 in set:
        continue
    if sc[i]>=80:
        print(i+1, "번 학생은 합격입니다.")
