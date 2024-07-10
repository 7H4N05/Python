list1=[1,2,3,4,5,6,7,8,9,0]
def show(l,i):
    if i==len(l):
        return ()
    return (list1[i],)+show(l,i+1)
call = show(list1,0)
print(call)    