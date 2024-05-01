THE FIRST FUNCTION :

def fact_ iterative(n):
result = 1
for i in range(1, n + 1):
result *=i
return result

THE SECOND FUNCTION: 

def fact_recursive(n):
if n==1 or n==0:
return 1
else:
return n* fact_recursive(n-1)
