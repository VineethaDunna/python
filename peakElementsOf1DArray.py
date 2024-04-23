''' This question is asked in following companies
Amazon
Apple
Bloomberg
Facebook
Google
Microsoft
Quora
Uber'''
jhg

# DESCRIPTION OF PROGRAM
# Peak elements of an array are the elements that are greater than their adjacent elements.
# The adjacent elements of an element at index are elements at index  i-1 and i+1.  For corner elements A[0] or A[N-1], there is onlyone adjacent element, i.e. either at index i+1 or i-1
# Given an array A of N elements, write a program to print the indices of all peak elements in A in increasing order
# SOLUTION
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
