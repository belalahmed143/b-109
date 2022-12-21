from class5 import Person

class Teacher(Person):
    def information(self,name,age,mobile,address,department,salary):
        return name,age,mobile,address,department,salary

t_obj = Teacher()
print(t_obj.information('Belal', 34, 9387442, 'Madaripur', 'CSE', 23000))