student_name = [13,45,36,"Lipi","Saba","Nur"]
#to access the first 3 items
for x in range(3):
    print(student_name[x])
#to print the full list we need no loops
print(student_name)
#to change a value we can access by indexing
student_name[0] = 1
print(student_name)   
#to find number of elements in the list
print("The number of elements are: "+str(len(student_name)))
#append and insert function
student_name.append("Rani")
student_name.append("Nur")
student_name.insert(3,50)
student_name.insert(4,18)
print(student_name)
#count method
print(student_name.count("Nur"))
#extend method
student_name.extend(["Asha","Lily"])
student_name = student_name + ["Lyra","Rimi"]
student_name.insert(5,16)
student_name.insert(6,20)
student_name.insert(7,22)
student_name.insert(8,5)
print(student_name)
#delete element from list
fruits = ["apple","orange","pear","grape","peach","blueberry"]
print(fruits)
fruits.remove("pear")
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.clear()
print(fruits)
del fruits