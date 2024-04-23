'''This question is asked in following companies
Amazon
Apple
Barclays
Bloomberg
Facebook
Mathworks
Microsoft
Yahoo
JP Morgan
SAP '''
# Fibonacci numbers are a sequence of numbers where a number F(i) is represented as F(i-1)  F(i-2). 
#The following numbers are the initial numbers of Fibonacci sequence.
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# Here, the Nth Fibonacci number is the Nth number from left in the sequence of Fibonacci numbers. For example, the fourth Fibonacci number is 3.
# Write a program to find the Nth number in the Fibonacci sequence
def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input())
print(Fibonacci(n))
