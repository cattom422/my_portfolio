#lab03
from math import *

#1
##	连续从控制台(console)读入三个数，将它们分别
##a)	转换为int
##b)	转换为float
##然后在一行中输出这三个数。

triangle=[]
for i in range(3):
    ipy=input("Please type in a number: ")
    print("No. "+str(i+1)+" is {}, and its float form is {}".format(ipy,float(ipy)))
    triangle.append(int(ipy))

#2
a,b,c=triangle
def triangle_area(a,b,c):
    '''
    计算三角形面积
    '''
    p=(a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
print("The triangle's area is "+str(round(triangle_area(a,b,c),3))+".")

def angle_C(a,b,c):
    '''
    计算C的弧度值
    '''
    cosine=(a*a+b*b-c*c)/(2*a*b)
    return acos(cosine)
print("The three angle value of the triangle is {}, {} and {}.".format(round(angle(a,b,c),3),round(angle(a,c,b),3),round(angle(b,c,a),3)))

def out_radius(a,b,c):
    '''
    三角形外接圆半径
    '''
    return c/sin(angle(a,b,c))/2
print("The radius is "+str(round(out_radius(a,b,c),3))+".")

def circle_area(radius):
    '''
    计算圆的面积
    '''
    return pi*radius*radius
print("The circle area is "+str(round(circle_area(out_radius(a,b,c)),3))+".")

def in_radius(a,b,c):
    '''
    三角形内接圆半径
    '''
    return triangle_area(a,b,c)*2/(a+b+c)
print("内接圆半径为{}，它的面积为{}".format(round(in_radius(a,b,c),3),round(circle_area(in_radius(a,b,c)),3)))

#3
#从控制台读入任意一个数学表达式，计算这个表达式的值
expr=input("Please type in an expression: ")
print(expr+"="+str(eval(expr)))

#4
#从控制台读入两个数，交换它们的值，输出 第一个数与第二个数的差
num1=int(input("Please typr in number 1: "))
num2=int(input("Please typr in number 2: "))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1-num2)

#5
#添加注释

#6
#才看到6用函数实现
#现定义如下
area=triangle_area
def angle(a,b,c):
    return angle_C(a,b,c),angle_C(a,c,b),angle_C(b.c.a)
circumangle=out_radius
incircle=in_radius

#7
def f(x1, y1, r1,  x2, y2, r2):
    heart_distance=sqrt((x1-x2)**2+(y1-y2)**2)
    sub_radius=abs(r1-r2)
    sum_radius=r1+r2
    if heart_distance>sum_radius or heart_distance<sub_radius:
        return 0
    elif sum_radius==heart_distance or heart_distance==sub_radius:
        return 1
    else sub_radius<heart_distance<sum_radius:
        return 2
