light = input("LIGHT : ")
if(light == "red"):
   print(" stop! ")
elif(light == "yellow"):
   print(" wait! ")
elif(light == "green"):
   print(" go! ")
else:
   print(" light is broken ")


#marks
marks = int(input("mark : "))
if(marks >= 90):
   print(" topper! ")
elif(marks >= 70 and marks < 90):
   print(" good! ")
elif(marks >= 40 and marks < 70):
   print(" pass! ")
else:
   print(" fail-_- ")

# by using ternary opreators
#finding missinng people
name = input("Name of the Person you found = ")
print("you found him!")if name == "Rohan" or name == "Thomas" else print("sorry-_-")

#voting rights
age = int(input("your Age = "))
vote = ("you have a right","no you don't have right")[age < 18]
