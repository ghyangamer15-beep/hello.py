print("\n")
print("***Calculator by Ghyan****")
print("\n")

num1=float(input("Enter your 1st number here :"))
num2=float(input("Enter your 2nd number here :"))

print(" Enter 1 for 'Addition'\n Enter 2 for 'Subtraction'\n Enter 3 for 'Multiplication'\n Enter 4 for 'Division' ")

Entered_num=int(input("pick a no. from 1 to 4 =="))

if Entered_num==1:
    print("Addition of 1st and 2nd no. is: ",num1+num2)

elif Entered_num==2:
    print("Subtraction of 1st and 2nd no. is:",num1-num2)

elif Entered_num==3:
    print("Multipication of 1st and 2nd no. is:",num1*num2)

elif Entered_num==4:
    if num2== 0:
        print("Error:Division with 0 so not defined")
    else:
        print("Division of 1st and 2nd no. is:",num1/num2)
        
else:
    print("invalid input")    
            