print("----------FUUAST MARKSHEET----------")
name = input("Enter Your Name               ")
print("Your Name is                 ",name)
rn = input("Enter your Roll No.             ")
print("Your Roll No is                ",rn)
dt = input("Enter Data Mining Marks         ")
ds = input("Enter Data Science Marks        ")
ai = input("Enter AI Marks                  ")
total = int(dt) + int(ds) + int(ai)
print("Your total Marks are            ",total)
per = total/300*100
print("Your % is",per)
if per >= 80 :
    print("You got A+ Grade")
elif per >= 70 :
    print("You got A Grade")
elif per >= 60 :
    print("You got B Grade")
elif per >= 50 :
    print("You got C Grade")
else:
    print("You are fail")