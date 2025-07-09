n=5
# for x in range(1,2*n):
#     spaces=abs(n-x)
#     stars=2*(n-spaces)-1
#     print(" "*spaces+"*"*stars)

for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)