#1
def sum_and_mul(l):
    s=0
    m=1
    for i in l:
        s+=i
        m*=i
    return s,m
# print("sum is {} and mul is {}.".format(*sum_and_mul([1,2,3,4])))

#2
def compare_list(lst1,lst2):
    if len(lst1)<len(lst2):
        lst1,lst2=lst2,lst1
    for i in lst2:
        if i not in lst1:
            return False
    else:
        return True,lst1
# print(compare_list([1,2],[1,2,3]))

#3
def print_even():
    print(*[i for i in range(1000,3001) if i%10%2==0 and i//10%10%2==0 and i//100%10%2==0 and i//1000%10%2==0],sep=',')
# print_even()

#4
def non_duplicate(l):
    l.sort()
    l1=[l[0]]
    for i in l:
        if i!=l1[-1]:
            l1.append(i)
    return l1
#print(non_duplicate([1,4,7,2,1,3,2,3,5,5,7,5,6]))

#5
def rev_positive(n):
    l=list(str(n))[::-1]
    n1=0
    for i in l:
        n1=n1*10+int(i)
    return n1
# print(rev_positive(386423))

#6
def intersection(l1,l2):
    l1.sort()
    l2.sort()
    l=[]
    i=0;j=0
    while i<len(l1):
        while j<len(l2) and l1[i]>l2[j]:
            j+=1
        if  j>=len(l2):
            break
        elif l1[i]==l2[j]:
            l.append(l1[i])
        i+=1
    return l
# print(intersection([1,3,2,-3,9],[2,4,3,-9,-3]))

#7
def star(n):
    for i in range(n-1):
        print("*"*(i+1))
    print("*"*n)
    for i in range(n-1):
        print("*"*(n-i-1))
# star(5)

#8
def count_digits(n):
    s=[0 for i in range(10)]
    while n!=0:
        cur=n%10
        n=n//10
        s[cur]+=1
    return s
#print(count_digits(12333219))

#9
def sum_of_two(n):
    if n==0:
        return 0
    else:
        return sum_of_two(n-1)+int("2"*n)
# print(sum_of_two(3))

#10
def matrix_and_tranpose(n):
    m=[[i+1 for i in range(10)] for j in range(n)]
    t=[[i+1 for j in range(n)] for i in range(10)]
    return m,t

def print_matrix(m):
    for i in m:
        print(*i)
# mt=matrix_and_tranpose(3)
# print("original matrix:")
# print_matrix(mt[0])
# print("transpose:")
# print_matrix(mt[1])

#11
def find_min(lst):
    # i=0
    # while i<=len(lst)-1:
    #     while i<len(lst)-1 and lst[i+1]>lst[i]:
    #         i+=1
    #     if i==len(lst)-1:
    #         return i
    #     else:#i>=i+1
    #         for j in range(i+2,len(lst)):
    #             if lst[j]>lst[j-1]:
    #                 break
    #         else:
    #             return i
    #     i+=1
    #version2
    j=len(lst)-1
    while j>0 and lst[j-1]>=lst[j]:
        j-=1
    return j
# print(find_min([1,2,2,2,3,3,3,3,4,3,3,2,1]))

#12
#Sieve of Eratosthenes
def is_prime(n):
    prime=[True for i in range(n+1)]
    i=2;j=2
    while i<n:
        if not prime[i]:
            i+=1
            continue
        while j*i<=n:
            prime[i*j]=False
            j+=1
        i+=1
    return prime[n]
# print(is_prime(6341))
def prime_list(n):
    prime=[True for i in range(n+1)]
    prime_ans=[]
    i=2
    while i<n:
        j=2
        if not prime[i]:
            i+=1
            continue
        while j*i<=n:
            prime[i*j]=False
            j+=1
        i+=1
    for i in range(2,n+1):
        if prime[i]:
            prime_ans.append(i)
    return prime_ans
# print(prime_list(10000))


