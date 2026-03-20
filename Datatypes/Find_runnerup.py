n=int(input())
a=list(map(int,input().split()))
max_score=max(a)
while max_score in a:
    a.remove(max_score)
print(max(a))