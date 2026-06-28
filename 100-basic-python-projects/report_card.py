name = input("enter your name : ")

maths = int(input("Enter Marks of Maths : "))
science = int(input("Enter Marks of science : "))
english = int(input("Enter Marks of English : "))
java = int(input("Enter Marks of java : "))
python = int(input("Enter Marks of python : "))

total = maths + science + english + java + python 
avg = total / 5 
percent = round((total/500) * 100 , 2 ) 
print("-----------------------------")
print("MSQ REPORT CARD")
print("-----------------------------")
print("Name     : ",name)
print("maths    : " , maths)
print("Science  : " ,science)
print("English  : " , english)
print("Java     : " , java)
print("Python   : " , python)

print("-----------------------------")

print( "Total       :" ,total)
print(f"Average : {avg:.2f}")
print(f"Percentage : {percent:.2f}%")


print("-----------------------------")
