# name = 'belal'
# course_category = 'Python'
# S_id = 7865


# name1 = 'ahmed'
# course_category1 = 'Python'
# S_id1 = 7865

# print('ok')
# print('no')





# def student1():
#     print("Hello Func")

# student1()
# student1()
# student1()
# student1()
# student1()


def student(name, s_id, course_name):
    print(name + ' / ' + s_id + ' / ' + course_name)

# student('Arif', '10912', 'Python Django')
# student('Ahmed', '10913', 'Python Django')
# student('Belal', '10914', 'Python Django')
# student('Arif2', '10915', 'Python Django')


# def teacher(name,designation,salary):
#     return name,designation,salary


# belal = teacher('Belal', 'Developer', 30000)
# print(belal)

# ahmed =teacher('Ahmed', 'Developer', 30000)
# print(ahmed)

# print(teacher('Belal', 'Developer', 30000))


def person(*args):
    # for info in args:
    #     print(info)
    return args

print(person('Ahmed','Belal',3000,4041,'Madaripur'))
print(person(50000))



# def shopkeeper(*args):
#     for total_price in args:
#         total_price += total_price

#     return total_price

# print(shopkeeper(10,10,10,10,10,10))


# def shop(*args):
#     total=0
#     for info in args:
#         total +=info
#     print(total)
# shop(10,10,40)



# def shopkeeper(*args):
#     total = 0
#     for total_price in args:
#         total += total_price
#     return total
# print(shopkeeper(10,10,10,10,10,10,100,10,10,10))



def shop(**kwargs):
    sum = 0
    for price in kwargs:
        sum = sum + kwargs[price]
    return sum
print(shop(chal=60,tel=175,dal=130))

my_dic = {
    'chal':60,
    'tel':175,
    'dal':130
}
sum=0
for price in my_dic:
    sum = sum + my_dic[price]
print(sum) 

# shopdict = {
#   "chal": 60,
#   "dal": 140,
#   "tel": 185
  
# }
# sum=0
# for info in shopdict:
#     sum +=shopdict[info]
# print(sum)



# Decorators in Python

# def uppercase_decorator(f):
#     def change():
#         func = f()
#         make_uppercase = func.upper()  
#         return make_uppercase
#     return change

# @uppercase_decorator
# def say_hi():
#     name = 'belal'
#     return name

# print(say_hi())

# @uppercase_decorator
# def say_hj():
#     return 'hello hello there'

# print(say_hj())

def my_f(a,b):
    return a + b
print(my_f(5, 10))


my_lf = lambda a,b: a+b
print(my_lf(5,15))


# def lam_func(func,a,b):












