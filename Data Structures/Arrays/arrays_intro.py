# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
T=int(input())
#N,D=int(str(input())).split()
   
for k in range(T):
    arr=[]
    N,D= map(int, input().split())
    
    i=0
    j=0
    k=0
    temp=0
    arr=[int(x) for x in input("Enter integers: ").split()]
    print(arr, sep =" ")
    for j in range(D):
        #arr1=func_rotate(arr)
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=temp
    for x in range(len(arr)):
        print(arr[x])
    del arr[:]

T=int(input())
for i in range(T):
    try:
        N=int(input())
        A=[int(x) for x in input(" ").split()]
        K=int(input())
        print(A.index(K))
    except:
        print(-1)

######### Alternative Sorting ##########
arr=[7, 1, 2, 3, 4, 5, 6]
arr.sort()
n=len(arr)
i=0
j=n-1
arr2=[]
while(i<j):
    print(arr[j],end=" ")
    j-=1
    print(arr[i],end=" ")
    i+=1
    
if(n%2 != 0):
    print(arr[j])
  
####### LC - Rotate array #####
k=3
nums=[1,2,3,4,5,6,7]

for j in range(k):
    temp=nums[-1]
    for i in range(len(nums)):
        nums[i],temp=temp,nums[i]
print(nums)

while(k > 0):
    nums.insert(0, nums.pop())
    k -= 1
print(nums)

####### Monotonic array #######
A=[1,3,2]
for i in range(len(A)-1):
    if(A[i]<=A[i+1]):
        pass
    else:
        pass
print("True")

######## squares of sorted array #########  

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A1=[]
        for i in range(len(A)):
             A1.append(A[i]*A[i])
        A1.sort()
        return A1

########   Coins ###########

n=8
for i in range(1,n+1):
    if(i<=n):
        print("value of i is : ",i)
        n-=i
        print("value of n is : ",n)
        print(i)

        
####### Elements disappeared in an array ########3
nums=[1,1]
nums.sort()
arr=[]
for i in range(1,len(nums)+1):
    if i not in nums:
        arr.append(i)
print(arr)

###### Non-decreasing array ##########
nums = [4,2,1,3]
for i in range(len(nums)-1):
    if(nums[i]<=nums[i+1]):
        nums[i],nums[i+1]=nums[i+1],nums[i]
print(nums)
nums=nums[:]
nums.append(1)
print(nums)

############### Find `PIVOT ELEMENT ###############

nums = [-1,-1,0,1,1,0]
S = sum(nums)
leftsum = 0
for i,x in enumerate(nums): 
    if (leftsum == S-nums[i]-x):
        print(i)
    leftsum += x
  
############## Largest Number At Least Twice of Others ##########3

nums = [3, 6, 1, 0]
max_value = 0
for i,value in enumerate(nums):
    if value > max_value:
        max_value = value
        
for i,value in enumerate(nums):
        if value*2 == max_value:
            print(i)
       
##########  Plus One ########

digits = [1334,3,2,1]
for i in range(len(digits)):
    if len(str(digits[i])) == 1:
        tail = digits[-1] + 1
        digits.pop()
        digits.append(tail)
print(digits)
print(len(str(digits[0])))

##########  Running Sum of 1d Array ########

nums = [3,1,2,10,1]
arr1 = []
value = 0
arr1.append(nums[0])
for i in range(len(nums)-1):
  #  arr1.append(nums[i])
    value = arr1[i] + nums[i+1]
    arr1.append(value)
print(arr1)

#######  Maximum Product of Two Elements in an Array  ######

nums =  [1,5,4,5]
nums.sort()
arr1= []
for i in range(len(nums)-1):
    value = (nums[i]-1)*(nums[i+1]-1)
    arr1.append(value)
print(max(arr1))

#######  Convert Integer to the Sum of Two No-Zero Integers  #######

def getNoZeroIntegers(self, n: int) -> List[int]:
       for i in range(n):
           if "0" not in str(i) and "0" not in str(n-i):
               return [i,n-i]

########## Destination City ##########

def destCity(self, paths: List[List[str]]) -> str:
       m = []
       n = []
       for i in paths:
           m.append(i[0])
           n.append(i[1])
       for i in range(len(m)):
           if n[i] not in m:
               return n[i]               

########## Find Numbers with Even Number of Digits ########

nums = [12,345,2,6,7896]
count = 0
for i in range(len(nums)):
    i = str(nums[i])
    if len(i)%2 == 0:
        count+=1
print(count)

###########  Defanging an IP Address  ###########

def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

############  Make Two Arrays Equal by Reversing Sub-arrays  ############    

target = [0,7,9]
arr = [3,7,11]
def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    target.sort()
    arr.sort()
    return target == arr

###########  Duplicate Zeros  ###########
arr = [1,0,2,3,0,4,5,0]

i = 0
while (i < len(arr)):
    if arr[i] == 0:
        arr.insert(i+1,0)
        arr.pop()
        i+=2
    else:
        i+=1
print(arr)

#########  Replace Elements with Greatest Element on Right Side  #########
arr = [17,18,5,4,6,1]
arr1 = []

for i in range(1,len(arr)):
    max1 = max(arr[i:])
    arr1.append(max1)
arr1.append(-1)
    
print(arr1)

 # lC soln #

arr = [17,18,5,4,6,1]
greatest = arr[-1]
new_greatest = arr[-1]
for i in range(len(arr)-1,-1,-1):
    if arr[i] > greatest:
        new_greatest = arr[i]
    arr[i] = greatest
    greatest = new_greatest
    arr[-1] = -1
print(arr)

#############  Decompress Run-Length Encoded List  ############

nums = [1,2,3,4]

arr = []
count = 0
for i in range(len(nums)):
    if i%2 == 0:
        j = 0
        count = nums[i]
        while(j < count):
            arr.append(nums[i+1])
            j += 1
    else:
        pass
        
print(nums)
print(arr)
"""



          