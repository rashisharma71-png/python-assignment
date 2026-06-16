name = input("Enter student name ")
cl = input("Enter class ")
m1 = float(input("Enter marks of Subject 1") )
m2 = float(input("Enter marks of Subject 2"))
m3 = float(input("Enter marks of Subject 3"))
m4 = float(input("Enter marks of Subject 4"))
total = m1 + m2 + m3 + m4 
percentage = (total / 400) * 100
if percentage >= 60:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"
print("\n----- Result -----")
print("Name:", name)
print("Class:", cl)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)









