

####
# BASIC
# https://www.youtube.com/watch?v=TqPzwenhMj0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=5
####


10/5
10//5

'navin' + 'naviri' + 'navro' *10

print("navin's laptop")
print('navin\'s "laptop"')

print("c:\sumit\nPython\3.7")
print('c:\sumit\nPython\3.7')
print(r'c:\sumit\nPython\3.7')
print(r"c:\sumit\nPython\3.7")

##########
#
#
############

2+3
x=9
x+3
y=1
## x is 9 still
x+y

x ## is 9 still

name = 'youtube'
name + ' rocks'

res = _

_


name[0] + name[8] ##collection/ array / item of array

name[0] + name[1] ##collection/ array / item of array

name[0] + name[-1] + name[-2] + name [-3]

name[0:3]
name[1:] ## 1 inclusive
name[:]  ## full

name[0:3] = 'my' ## String is immutable PYTHON
'my ' + name[3:]

myname = 'N R M K SCHOOL'

len(myname)


##############
# LIST in Python
##############

nums = [25,10,1,552,00,-5,1,2] 
nums
nums[0]
nums [3]
nums[0:3]

nums = ["name ", "shah ", "sum ", "CIA ", "BOA "]
nums
nums[5]
nums[2:]
nums[-1:]

nums1= [ "sumit", 5.0, 2222, '234', '!@#$@']
numTotal  = nums, nums1
numTotal =0
numTotal
numTotal  = [nums, nums1] ## both diff
numTotal


numTotal.append[0]
numTotal.append(0)
numTotal.append([0])
numTotal.insert(0,-111)   ## insert (index, value)
### Insert not working in ^ Tupple(numTotal)
numTotal
nums
nums1
nums.insert(0,-555)   ## insert (indeX, value)
nums

## append --> ALWAYS adds at the end--
## add --> addd in between as required--

nums.remove(-555) ## pass Value NOT index
nums.pop() ## by default last element -1
nums


## LIST == mutable <--Python
del nums
nums = ["name ", "shah ", "sum ", "CIA ", "BOA "]
nums

del nums[0:2]
nums.extend([299,3999,4444,5585])
nums

## This is LIST - usecase- sort()
numericNum = [1,18,2,484,51,848,6,0,5]
min(numericNum)
max(numericNum)
sorted(numericNum)

numericNum.sort()
numericNum
numericNum[0] = 0

####################
## LIST[]  = mutable 
## tupple() = immutable
####################

tappu = (22,21,21,5,54,56,78) # cant change
tappu 
tappu[2]
tappu(2) # = 9  ...you CANT ReAssign ## error

#################
## SET = Collection of unique elements
## set is auto arranged in order
## set = hash = speeedup search
## set store value in HASH
## set = no index support
## set = can update value YES  
##################

s = {25,5,15,8484,545}
s
s = {324,5,65,23,7,4,2,5,7}
s

s = {1,1}  ## NO duplicate
s
s = { "ds", "sdf", 'df'}
s

s[2] # this cant work because order is not maintained

###########################
### id(obj/Var) to find memory address
###
###########################

id(s)
id(nums)
id("Sumit")

# pointing same memory
colli1 = 5
colli2 = 5
id(colli1)
id(colli2)

id(0)
tz1 =10
id(tz1)
tz1 =9
id(tz1)


## no constant but show big letter intention- of not changing.
AA = 99
AA
AA = 88
AA

###########################
## Null = None = Python
## Data types
##
#######################

type(s)
type(tz1)
type(name)
type(tappu)
tz2 = 6+9
type(tz2)
tz2 =6+9j   ## j--> ^(-1) = complex
type(tz2)


AA = 88
BB = float(AA)
BB
BB = complex(AA)
BB
BB = complex(AA, AA)
BB

BB = str(AA)
BB

AA = 88
BB = 77
chk = AA < BB
chk

type(chk)
type(bool)

int(True) # =1
int(False) # =0

range(0,100,2) # range(start,stop,step)
list(range(0,100,7))

list(range(10))

type(list)
type(range)

type(range(10))
type(list(range(10)))

####################
##  Dictionary
##  K : V
#################### 
d = {'sumit' : 'emma', 'mis' : 'try', 'k' : 'value'}
d
d.keys()
d.values()
d['mis']
d.get('mis')

####################
##  O
##   
####################


tz1 =5
tz2 =2

tz1 = tz1+2
tz1 
tz1 = +2 # ReAssignment -->2 
tz1 == +2  # true / false
tz1
tz1 +=2 # add 2 --> tz1
tz1 *2
tz1 *=2 # *2 --> tz1
tz1

tz1, tz2 = 1,3
tz1, tz2

-tz1
tz1
tz1 = -tz1
tz1 <= tz2
tz1 != tz2


tz1 ==0 or tz1 > 0
tz1 >0 and tz2 >2

not tz1

bin(25) # ---->0b11001 "0b" =--> binary
oct(25) # ---->0o31 "0o" =--> octoal
int(0b11001) 
hex(25) # ----> 0x19 '0x' ---> hexa

0xf # --> '0x' ==hexa, 'f' = 15

##################
## swap
##
##################
tz1, tz2 = 1,3

temp = tz2
tz2= tz1
tz1 = temp

tz1,tz2
########### swap no temp Var.

a, b = 1,3
a = a + b
b = a - b
a = a - b
a, b


a,b = b,a # ROT_TWO s

########
1100
0b1100
~12

12 & 13 # bitwise operation 12->bit 13->bit
12 | 13 # bitwise operation


#        XOR
#  INPUT 	  OUTPUT
# 0 	0 	   0
# 0 	1 	   1
# 1 	0 	   1
# 1 	1 	   0  
# https://www.youtube.com/watch?v=PyfKCvHALj8&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=17
12 ^ 13 # ^ = XOR 12--> bit XOR 13--bit

5>>2
0b0101 == 5
print(0b00000101 >> 2 )

bin(1)

5 >> 2 << 2 

import math
print(math.sqrt(25))
x= (math.sqrt(25))
x

print(math.floor(2.9911))
print(math.ceil(2.001))

2**6 # power of

print(float(math.pow(2,6)))
print(math.e)

import math as m # alias

print(m.log(1))
sqrt(25) 

from math import sqrt
sqrt(225)

help(math) # all math funtions


## below cmd run only in 3.7.py
## below cmd work nly click RUN/play button
## below cmd run only in bash shell (ubuntu windows) python3 then line by line

ch= input('enter your character to disp:')
print(ch)
print(ch[0])

ch= input('enter your character to disp:')[0]
print(ch)

ch= input('enter your character to disp:')[0]
## enter your character to disp:1+1-1
ch # ans is 1

##########################
## this EVAL() can do only MATH operation
##########################

result1 = eval(input('enter an expr ')) 
print(result1)

##########################
## python.py file
## how to pass 2 arg with file name
## >>> test.py arg1 arg2
##########################
import sys

x = (sys.argv[1])
y = (sys.argv[2])
z = int(x)+int(y)
print(z)


##########################
## 
## 
##########################

x = 2
r = x % 2

if r==0:
    print("in true section")

########################


x = 2
if (r==0):
    print("this is zero")

print("part-1-always..this will get printed")

if(r==31):
    print("1--in")

print("Bye... The Program has completed!")

############################
#       IF...else
############################
r=2
if(r ==0):
    print("this is zero")
else:
    print("not zero")

print("This will always get printed..!!")

############################
#       Nested IF + If..else
############################
r=22
print("r is:", r)
if(r>0):
    print("r is pos(+)")
    if ( r>0 & r<5 ):
        print("r is between 0-5")
    else:
        print("r is 5++")
else:
    print("r is neg(+)")
    
print("forever print this-Bye!")

##########################
#  this will check all the condition of if
#  even your x=1 (1st condition, still will go next)
##########################
x =1
if (x==1):
    print("its 1")
if (x==2):
    print("its 2")
if (x==3):
    print("its 3")
if (x==4):
    print("its 4")

############################
#       elIF (use debugger to understand)
# It ignores all IFs below after getting 1 IF correct
############################

x = 6 # int(input("x : ")) # x=1 assume that
if (x==1):
    print("its 1")
elif (x==2):           # bcos x=1, it will not eval below all elIF
    print("its 2")
elif (x ==3):
    print("its 3")
elif (x == 4):
    print("its 4")
elif (x == 5):
    print("its 5")
else:
    print("wrong I/P")
    print("its 5++")
print("Bye")


###############
## while loop
###############

i=0
while (i!=5):
    print("Summit", i)
    print("M.")
    print("---")
    i=i+1

###############

i=0
j=0
while (i!=5):
    print("Summit", i, end="")
    j=0
    while (j<3):
        print("---> Rocks", end="") # this dont go new line
        j=j+1
    print(" M.", end="")
    print(" ---")
    i=i+1

###############
## for.. loop
###############

nums = ["name ", 12, 00, "shah ", "sum ", 55, "CIA ", "BOA "]
nums
for i in nums:
    print(i)
###########################
nums = 'sumit'
nums
for i in nums:
    print(i, end=" ")

##########################

num=10,454,548,3

for i in num:
    print(i)
    i= i+1

for j in range(0,110,20):
    print(j)

for k in [2,45,68,777,2.5,-1]: #list
    print(j)

for l in {12,447,8,'t','rg'}: #set
    print(l, end=" ")
    print(id(l), end=" ")
    print(type(l))


for l in {12,447,8,'t','rg'}: #set
    t1 = str(id(l))
    if(t1[0] =='2'): # 1st digit of mem location==2
        print("there we 2 go", l)

##############################
##      NESTED for.. loop
##############################

x= int(input("enter candy(ies): "))
i=1
while (i<=x):
    print("candy")
    i=i+1

for i in range(0,x,1):
    print("candicandi")
    i=i+1

################

x= int(input("enter candy(ies): "))
i=1
while (i<=x):
    if(x>10):
        print("OUTSIDE of requirement/range")
        break

    print('kandy b')
    i=i+1
print("bye")

################
# skip values for % 3 and % divisible by 5

for i in range(1,51):
    # print(i, end=" ")
    if (i % 3 ==0 or i%5==0):
        continue # it SKIP # go back to loop (for i(now i=4) in range)
    print(i)

print("bye")


######### skip odd number
for i in range(1,51):
    # print(i, end=" ")
    if (i % 2 != 0):
        continue # it SKIP # go back to loop (for i(now i=4) in range)
        # pass
    else:
        print(i , "its even")
print("bye")

#########
for i in range(5):

    if i==3:
        break
    print("Hellieo", i)

#########
for i in range(5):

    if i == 3:
        continue  # 0,1,2,4  # skip = continue
    print("Hellieo", i)

#########
for i in range(5):

    if i == 3:
        pass # 0,1,2,3,4  # pass used when you wanna keep empty condition
    print("Hellieo", i)

#########
for i in range(5):
    print("Hellieo", i) # 0,1,2,3,4

# # # # 
# # # # 
# # # # 
# # # # 
for i in range(4):
    for j in range (4):
        print("# ", end="")
    print() ## for new line
    print() ## for new line

#
# #  
# # # 
# # # # 
for i in range(4):
    for j in range(i+1):
        print("* ", end="")

    print() ## for new line

# # # #
# # # 
# #
#

for i in range(4):
    for j in range(4-i):
        print("# ", end = "")

    print() ## new line

##########
# check num[] divisible % 5
nums = [12,15,18,19,24,25]

for i in nums:
    if (i%5==0):
        print("yeah ", i)

##########
nums = [12,156,18,19,24,256]

for i in nums:
    if (i%5==0):
        print("yeah ", i)
        break
    else:
        print("nahi")
        break

##########
####   for...else....
nums = [12,15,18,19,24,25]

for i in nums:
    if (i%5==0):
        print("yeah ", i)
        break
else:
    print("nahi")

############
#   isPrime check
############
num = 111 # int(input("Enter integer :"))
for i in range(2, num):

    if (num%i == 0):
        print("i can not be prime because from 2 to num=16, 2.3.4.5.6.7.8.9.10.11.12.13.14.15",
              "any of 2 <---to----> 15 number division is giving %==0...eg: 16%2==0, 16%8=0...so 16 cant be PRIME")
        break
    else:
        print("I am prime bcos anyone/any number division is not giving % ==0 for me, as I unique", num)





#######
# understand "_" value in variable
# on a trailing side
######

this_is_a_long_variable =5
print(this_is_a_long_variable)

class Wiz:
    _wizz = []
    wizz = []

    def access_privcy_Wiz():
        return Wiz._wizz

print(Wiz.access_privcy_Wiz())
print(Wiz.wizz)










##########################
## 
## 
##########################















##########################
## 
## 
##########################
