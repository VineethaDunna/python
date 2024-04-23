n=int(input())
list_1=list(map(int,input().split()))


out_list=""

for i in range(n):
    if (i==0):
        if (list_1[i]>list_1[i+1]):
            out_list+=str(i)+" "
    elif (i==n-1):
        if (list_1[i-1]<list_1[i]):
            out_list+=str(i)+" "
    else:
        if (list_1[i-1]<list_1[i] and list_1[i]>list_1[i+1]):
            out_list+=str(i)+" "
if (out_list==""):
    print("-1")
else:
    print(out_list)
