def show(n):
    print(n)
    if n==1:
        return
    else:
         show(n-1)
    # if n==1:
    #     break
    # else:
    #     show(n)
show(10)