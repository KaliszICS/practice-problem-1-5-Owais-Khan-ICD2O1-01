'''
    Lesson: Typecasting
    Author: Owais Ali Khan
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''

def q1():
  integer = input("Input an integer: ")
  integer = int(integer)
  print(integer + 3)

def q2():
  num1 = (input("Input a number: "))
  num1 = float(str(num1)+"4")+ 2
  print(num1)



def q3():
  num2 = input("Input a radius: ")
  num2 = float(num2)
  area = num2* num2 * 3.14
  print(area)

def q4():
  num3 = input("Input a number: ")
  num3 = float(num3)
  num3 = num3*12
  num3 = int(num3)
  print (num3)


def q5():
  var = input("Input an integer: ")
  var = int(var)
  var = var + 5
  print(f"Your number + 5 is {var}")

#Comment this code out when running tests
#Do not comment this out when running your program normally
'''
q1()
q2()
q3()
q4()
q5()
'''
 
