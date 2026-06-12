name=input("enter a name")
cl=input("Enter class ")
marks1=float(input("Enter marks for Subject 1"))
marks2=float(input("Enter marks for Subject 2"))
marks3=float(input("Enter marks for Subject 3"))
marks4=float(input("Enter marks for Subject 4"))
total= marks1 + marks2 + marks3 + marks4
percentage=(total/400 )*100 
print("\n----- Student Result -----")
print("Name:", name)
print("Class:",cl )
print("Total Marks:", total)
print("Percentage:", percentage, "%")


#2questions
str="this is python"
print(str.upper())

str="my name is maya"
print(str.lower())

str="my name is maya"
print(str.title())

str="my name is maya sharma"
print(str.swapcase())

str="my name is maya"
print(str.capitalize())

str="my name is maya"
print(str.casefold())

str="my name is maya"
print(str.center(60)) 

str="my name is maya"
print(str.count("is"))

str="my name is maya"
print(str.endswith("is"))

str="my name is maya"
print(str.find("is"))

str="my name is maya"
print(str.isalnum()) 

str="my name is maya"
print(str.isdigit())

str="my name is maya"
print(str.isnumeric())

str="my name is maya"
print(str.isspace())

str="my name is maya"
print(str.replace("maya","shiv"))
