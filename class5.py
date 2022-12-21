# class Person:
#     def my_f(self,a,b,y):
#         return a+b-y
# person_obj = Person()

# print(person_obj.my_f(4,5,3))

# class Calculator:
#     def addition(s,value1,value2):
#         total = value1+value2
#         return total

#     def substraction(self,value1,value2):
#         substract = value2-value1
#         return substract

#     def multiply(self,value1,value2):
#         result = value1*value2
#         return result

#     def division(self,value1,value2):
#         result = value2/value1
#         return result
    
# calculator_obj= Calculator()
# print('addition : ',calculator_obj.addition(10,20))   
# print(calculator_obj.substraction(10,20)) 
# print(calculator_obj.multiply(10,20)) 
# print(int(calculator_obj.division(10,25)))


# class CalculatorX:
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2

#     def addition(self):
#         return self.value1 + self.value2

#     def substraction(self):
#         return self.value1 - self.value2

#     def multiply(self):
#         return self.value1 * self.value2

#     def division(self):
#         return self.value1 / self.value2
    
# calculator_obj= CalculatorX(54,30)

# print('addition : ',calculator_obj.addition())   
# print(calculator_obj.substraction()) 
# print(calculator_obj.multiply()) 
# print(calculator_obj.division())


# calculator_obj2= CalculatorX(64,30)

# print('addition : ',calculator_obj2.addition())   
# print(calculator_obj2.substraction()) 
# print(calculator_obj2.multiply()) 
# print(calculator_obj2.division())


# class Admission:
#     def __init__(self, Std1, Std2):
#         self.Student1 =  Std1
#         self.Student2 =  Std2

#     def add(self):
#         return self.Student1 + self.Student1
#     def mini(self):
#         return self.Student1 - self.Student1
#     def into(self):
#         return self.Student1 * self.Student1
#     def div(self):
#         return self.Student1 / self.Student1
#     def much(self):
#         return self.Student1 % self.Student1
    
# Admission_obj= Admission(40,5)
# print(Admission_obj.add())
# print(Admission_obj.mini())
# print(Admission_obj.into())
# print(int(Admission_obj.div()))


# class EngBook:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b 

#     def english_book(self):
#         return self.a + self.b
            
#     def farshi_book(self):
#         return self.a - self.b       

# books = EngBook(20,10)
# mobile1 = books.english_book(), books.farshi_book()

# print(mobile1)


# print(english_book.english_book())
# print(farshi_book.farshi_book())


# class Person:
#     def information(self,name,age,mobile,address):
#         return name,age,mobile,address

# person_obj = Person()

# print(person_obj.information("Belal", 24, 8801704870490, 'Madaripur'))

# class Student(Person):
#     def s_info(self,s_id,department):
#         return s_id,department

# student_obj = Student()
# student_information = student_obj.information("ahmed", 23, 8803284734, 'Madaripur'),student_obj.s_info(7, 'cse')

# print(student_information)


class Person:
    def information(self,name,age,mobile,address):
        return name,age,mobile,address










