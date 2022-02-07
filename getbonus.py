salary=int(input("Enter salary:"))
years=int(input("Enter years of service"))
if years>10:
 bonus=salary*0.1
print(bonus) 
if years>=6 and years <=10:
    bonus =salary*0.08
    print(bonus)
    if years<6:
        bonus=salary*0.05
        print(bonus)
    