n=int(input("No of students in your class\n"))

new=[]

under_weight=[]

normal_weight=[]

for i in range(n):
    
    roll_no=int(input("Enter students Roll Number.\n"))
    
    name=input("Enter students Name.\n")
    
    weight,height=map(float,input("Enter students weight in kg and Height in meter by space separated\n").split())

    bmi=round((weight/(height**2)),1)
    
    print(f"BMI for {name} having roll no {roll_no} is {bmi}kg/m^2.\n")
    
    new.append([roll_no,name,weight,height,bmi])
    
    if bmi<=29.9 and bmi>=25.0:

        under_weight.append(bmi)
    
    elif bmi>=18.5 and bmi<=24.9:
    
        normal_weight.append(bmi)

print("List of Under_weight student is......\n")

for i in under_weight:

    for j in new:

        if i==j[-1]:

            print(f"{j[0]} , {j[1]} , BMI : {j[-1]}")

            new.remove(j)

            break

        else:

            pass

print("\n")

print("List of Normal_weight student is......\n")

for i in normal_weight:

    for j in new:

        if i==j[4]:

            print(f"{j[0]} , {j[1]} ,BMI : {j[-1]}")

            new.remove(j)

            break

        else:

            pass