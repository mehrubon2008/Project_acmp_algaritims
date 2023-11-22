s1 = input()
s2 = input()
s3 = input()
st = min(len(s1), len(s2), len(s3))
f = 0
k = 0
for i in range(st):
    if s1[i] == s2[i] and s2[i] == s3[i]:
        f = 1
    else:
        k = i
        break
if f == 0:
    print(-1)
else:
    print( max(len(s1), len(s2), len(s3)) - st)