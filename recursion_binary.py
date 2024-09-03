def bin(n):
    if(n==0):
        return
    bin(n//2)
    print(n%2)

bin(13)