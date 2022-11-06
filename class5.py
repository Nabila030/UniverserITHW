#object oriented
# class Person:
#     def my_func(self,a,b,y):
#       return a+b-y
# person_obj = Person()
# print(person_obj.my_func(4,5,3))

# #calculator implementation
# class Operation:
#     def add(self,a,b):
#         return a+b
#     def subs(self,a,b):
#         return a-b
#     def mult(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# ope = Operation()
# print(ope.add(8,4))
# print(ope.subs(8,4))
# print(ope.mult(8,4))
# print(ope.div(8,4))

class CalculatorX:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
    def add(self):
        return self.value1 + self.value2
    def sub(self):
        return self.value1 - self.value2
    def mult(self):
        return self.value1 * self.value2
    def div(self):
        return self.value1 / self.value2
cal_obj = CalculatorX(54,6)
print(cal_obj.add())
print(cal_obj.sub())
print(cal_obj.mult())
print(cal_obj.div())

#homework take inputs for calculator app
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
another_cal_obj = CalculatorX(x,y)

print(another_cal_obj.add())
print(another_cal_obj.sub())
print(another_cal_obj.mult())
print(another_cal_obj.div())

# #by participants
# class Books:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b 

#     def english_book(self):
#         return self.a+self.b
            
#     def farshi_book(self):
#         return self.a-self.b
            

# english_book = Books(20,10)
# farshi_book = Books(20,10)

# print(english_book.english_book())
# print(farshi_book.farshi_book())

#inheritence
# class Person:
#     def info(self,name,age,mobile_no,address):
#         return name, age, mobile_no, address
# person_obj = Person()
# print(person_obj.info("Nur",20,8809143432,"Dhaka"))

# class Student(Person):
#    def s_info(self,s_id,dept):
#     return s_id,dept
# st_obj = Student()
# print(st_obj.info("Lily",20,99034647,"Texas"))
# print(st_obj.s_info(7,"CS"))

# #method overriding
# class Teacher(Person):
#     def info(self, name, age, mobile_no, address,dept,salary):
#        return name, age, mobile_no, address,dept,salary
# teach_obj = Teacher()
# print(teach_obj.info("Bill",30,3593285,"Chicago","CS",10000))

