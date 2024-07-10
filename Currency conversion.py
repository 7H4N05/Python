def USDtoINR(n):
    return (n*83.42)
def INRtoUSD(n):
    return (n/83.42)
opt=input("\na:USDtoINR\nb:INRtoUSD\nEnter a choice:")
if opt=='a':
    USD=float(input("Enter currency in USD:"))
    r=USDtoINR(USD)
    print("The converted value is: ₹",r)
elif opt=="b":
    INR=float(input("Enter currency in INR:"))
    r=INRtoUSD(INR)
    print("The converted value is: $",r)

else:
    print("Invalid choice")