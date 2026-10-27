'''
Python tuân theo quy tắc LEGB khi tìm kiếm tên biến và tìm kiếm chúng theo thứ tự này:
Cục bộ - Bên trong hàm hiện tại
Bao bọc - Các chức năng bao bọc bên trong (từ trong ra ngoài)
Toàn cầu - Ở cấp độ cao nhất của mô-đun
Tích hợp sẵn - Trong không gian tên tích hợp sẵn của Python
'''
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

def my_function():
  return (10, 20)       #trả về 1c tuple

#còn /, và *, =>tự học thêm

#==================đối số====================================
def func1(*args) :    #cho phep chap nhan nhieu tham so truyen vao
  print("type :",type(args) )
  print("all args :",args)
#neu su dung tham so thong thuong thi tham so do phai dung trc tham so dac biet nay
def func2(**kid):   #tham so dac biet nay se dc dung tuong tu dict
  print("His last name is " + kid["lname"])
#============================phạm vi====================================================
def func3():
  global x    #với global là từ khóa giúp x trở thành biến toàn cục

def func5():
  x=10
  def func4():
    nonlocal x    #x sẽ trở thành biến của hàm bao quanh nó chứ k thuộc về hàm chứa nó
    x = 20
  func4()
  print(x)
#======================================decorator====================================================
def decor1(dfunc):
  return dfunc.upper
def func6(name):
  return "hello" + name

'''///////////////////////////////////////////////////////////////////'''

#print(fahrenheit_to_celsius(77))

#my_fruits = ["apple", "banana", "cherry"]
#my_function(my_fruits)

#my_person = {"name": "Emil", "age": 25}
#my_function(my_person)

#func1("Emil", "Tobias", "Linus")

#func2(fname = "Tobias", lname = "Refsnes")