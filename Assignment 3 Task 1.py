n=int(input("Enter a number:"))

def factoral(n):
    if n<2:
        return 1
    else:
        return n*(factoral(n-1))
    
result = factoral (n)

print("Factoral of", n, "is :", result)