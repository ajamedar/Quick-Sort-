def quicksort(x, n):
    if n==0:
        return 1
    elif x==0:
        return 10
  
    return x*quicksort(x, n-1)

x = 6
n = 3

print(x,' to the power of ','',n,'  = ', quicksort(x,n))