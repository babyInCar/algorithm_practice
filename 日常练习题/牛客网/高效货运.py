"""

"""

wa, wb, wt, pa, pb = map(int, input().split())
ans = 0

for i in range(1, wt):
    a = wa * i
    if a >= wt:
        break
    if (wt-a)%wb == 0:
        j = (wt-a) // wb
        ans = max(ans, i*pa + j*pb)
print(ans)