v1=[1, 10, 6, 5, 6, 9]
v2=[3, 7, 2, 8, 7, 3]
num=[3, 4, 5, 1, 8, 7, 9, 2]
amount=	[10, 5, 6, -6, -8, 2, -2, 5]

# team=[[]*2 for _ in range(len(v2))]
# for i in range(len(v1)):
#     team[i]=[v1[i],v2[i]]

team=[]
for i in range(len(v1)):
    if v1[i]>=v2[i]:
        team.append([v2[i],v1[i]])
    else: 
        team.append([v1[i],v2[i]])
print(team)
team.sort(key=lambda x : x[0])
print(team)

# new=[[]*10 for _ in range(10)]
new=[]
for j in range(len(team)):
    a,b=team[j][0],team[j][1]
    print(a,b)
    for k in range(j+1,len(team)):
        # print("team[k][0], [k][1]=",team[k][0],team[k][1])
        if a==team[k][0] or a==team[k][1]  or b==team[k][0]or b==team[k][0]:
            new.append(team[j]+team[k])

print(new)