from math import *
#1
def examine_triangle(a,b,c):
    '''
    Examine whether a,b,c can compose a triangle
    '''
    #value examination
    assert 0<a and 0<b and 0<c , "a,b,c should be bigger than 0"
    if a+b>c and a+c>b and b+c>a:
        return "THAT IS A TRIANGLE!"
    else:
        return "TRY TO THINK OF ANOTHER ONE!"
#print(examine_triangle(1,-2,3))
#print(examine_triangle(5,4,3))
#print(examine_triangle(1,2,3))

#2
def num_of_root(a,b,c):
    '''
    return the number of roots based on a,b,c given.
    '''
    assert a!=0 , "\"a\" should not be zero!"
    det=b**2-4*a*c
    if det>0:
        return 2
    elif det==0:
        return 1
    else:
        return 0
#print(num_of_root(1,2,1))
#print(num_of_root(1,-4,3))

#3
def is_prime(n):
    '''
    Is n a prime number or not?
    '''
    for i in range(2,n):
        if n%i==0:
            return "It does have the factor number of {}".format(i)
    return "A REAL PRIME NUMBER!"
#print([is_prime(i) for i in range(2,10)])    

#4
def is_reversed_year(n):
    '''
    Expecting an integer or string, then determine whether it is a reversed year.
    '''
    n=str(n);length_of_string=len(n)
    for i in range(length_of_string//2):
        if n[i]!=n[length_of_string-i-1]:
            return "{} WRONG!".format(n)
    return "{} YES!".format(n)
#print(is_reversed_year(1991),is_reversed_year(2024))

#5
def f(x):
    if x<-2:
        return x**4
    elif -2<=x<2:
        return sin(x)
    else:
        return 2.718281828**x
#print(f(-3),f(0),f(3))

#6
a=int(input("Numbers?(0 for terminate;-1 for reread a number;or positive number)"))
while a:
    if a>0:
        print(int(str(a)[::-1]))
    a=int(input("Numbers?(0 for terminate;-1 for reread a number;or positive number)"))

#7
def count_end_zero(n):
    n=str(n);length=len(n);cnt=0
    for i in range(length-1,-1,-1):
        if n[i]=="0":
            cnt+=1
        else:
            break
    return cnt
#print(count_end_zero(10000))

#8
def Hamming(a,b):
    return str(int(bin(a)[2::])^int(bin(b)[2::])).count("1")
#print(Hamming(3,7))

#9
#Collatz
#def is_valid(n):
#    return "VALID!"
def is_valid(n):
    while not n==1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
    else:
        return "Valid!"
print(is_valid(1000000))

#10
def solution():
    for i in range(100000+1):
        if i%3==2 and i%5==3 and i%7==2:
            print(i,end=" ")
#solution()

#11
def fractal(n):
    fr=1
    if not n:
        pass
    else:
        for i in range(1,n+1):
            fr*=i
    return fr
def choose(n,k):
    return fractal(n)/(fractal(k)*fractal(n-k))
print(choose(0,0))
def Pascal_triangle(n):
    n+=1
    PASCAL=[[] for i in range(n)]
    length=[i for i in range(n)]#除左右空格外的位置<-length
    for i in range(n):
        for j in range(i+1):
            PASCAL[i].append(int(choose(i,j)))
            length[i]+=len(str(PASCAL[i][j]))
    longest=length[-1]
    for i in range(n):
        indent=(longest-length[i])//2
        print(indent*" ",*PASCAL[i],indent*" ")
Pascal_triangle(13)





