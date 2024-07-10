#     if num!=",":
#         if int(num)%2==0:
#             count+=1
#             print(count)
            
# fun()
def fun():
    count=0
    num=""
    with open("text2","w") as f:
        f.write("12,2,31,43,5,64,78,812,90")
    with open("text2","r") as f:   
        data=f.read()
        i=0
        for i in range(len(data)):
            if(data[i] == ',' ):
                N=(int(num))
                if N%2==0:
                    count+=1
                    # print(N)
                num=''
            else:
                num+=data[i]
        print("There are",count,"even numbers")         
fun()   
