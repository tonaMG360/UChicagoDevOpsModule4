#Reference Code for DEVOPS CODE 
#Tona Mercado 
#University of Chicago
#Module 4 Assignment 

end = False

print (""" ************ 
            Calulator 
            **********

            Menu 

            1) sum
            2) Subtraction
            3) Mutiply
            4) Divide 
            5) exit """)

while not (end):
    option= int (input("Select an Option"))
    if (option==1):
        value1=int(input("First number"))
        value2=int(input("Second number"))
        print("The result is:", value1+value2)

    elif (option==2):
        value1=int(input("First number"))
        value2=int(input("Second number"))
        print("The result is:", value1-value2)

    elif (option ==3):
        value1=int(input("First number"))
        value2=int(input("Second number"))
        print("The result is:", value1*value2)
    
    elif (option==4):
        value1=int(input("First number"))
        value2=int(input("Second number"))
        print("The result is:", value1/value2)
    
    else:
        print("Exiting the calculator")
        end= True


