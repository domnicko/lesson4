sub1=int(input("Enter MATHEMATICS: "))
sub2=int(input("Enter   CHEMESTRY: "))
sub3=int(input("Enter     ENGLISH: "))
sub4=int(input("Enter     PHYSICS: "))
sub5=int(input("Enter     BIOLOGY: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=70 and avg<100):
    print("Grade: A")
elif(avg>=60 and avg<69):
    print("Grade: B")
elif(avg>=50 and avg<59):
    print("Grade: C")
elif(avg>=40 and avg<49):
    print("Grade: D")
elif(avg>=0 and avg<39):
    print("Grade: FAIL")
    
else:
    print("Grade: NULL")