import sys

# k=sys.stdin.readline().strip()
# n,m=map(int,sys.stdin.readline().split())

# array=list(map(int,sys.stdin.readline().split()))

# k=k.strip('"')
# m=list(map(int,k))
# print(sum(m))

student_tuples = [
    ('john', '10', 15),
    ('jane', '10', 12),
    ('dave', '10', 10),
]
student_tuples=sorted(student_tuples, key=lambda x:x[2])

print(student_tuples)