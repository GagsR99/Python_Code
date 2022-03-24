# # GIT Commands 
# git init
# git remote add origin 
# git add 
# git commit -m "message"
# git push origin master 
# git clone https://(github link)

# #LISTS
# # ls = ["Gagan", "Kriti", "Akash", "Vaishnavi"] # How to declare a list.

# # ls = ["name", True, 44.2, 57]
# # print(ls) 
# # print(type(ls))

# ls = ["Name", ["place", 70], True]
# print(ls)
# OUTPUT: ['Name', ['place', 70], True]

# ls = ["Gagan", "Kriti", "Akash", "Vaishnavi"]
# print(ls[2]) #---> Akash
# print(ls[-3]) #---> Kriti
# print(ls[3], ls[-2]) #---> Vaishnavi Akash

# ls = ["Gagan", "Kriti", "Akash", "Vaishnavi"]
# ls.append(999)
# print(ls) # ---> ['Gagan', 'Kriti', 'Akash', 'Vaishnavi', 999]

# ls.insert(2, "Cheetah")
# print(ls) # ---> ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi']

# ls = ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]
# print(ls)

# del(ls[2])
# print(ls) # ---> ['Gagan', 'Kriti', 'Akash', 'Vaishnavi', 999]

# ls = ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]
# print(ls[1:4]) # ---> ['Kriti', 'Cheetah', 'Akash']
# print(ls[2:]) # ---> ['Cheetah', 'Akash', 'Vaishnavi', 999]
# print(ls[:5]) # ---> ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi']
# print(ls[:]) # --->Prints complete List - ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999] 


# ls = ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]

# for i in ls:
#     print(i)

# for i in range(len(ls)):
    # print(i)

# for i in range(len(ls)):
#     print(ls[i])

# for i in ls:
#     print(ls) # --> ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]
#                     ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]      
#                     ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]      
#                     ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]      
#                     ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]      
#                     ['Gagan', 'Kriti', 'Cheetah', 'Akash', 'Vaishnavi', 999]    


# ls = [3, 10, 76, 45, 23, 135, 0, 289, 794]
# for i in ls:
#     if i < ls:
#         print(i) # --> if i < ls:
#                        # TypeError: '<' not supported between instances of 'int' and 'list'


# FUNCTIONS
# Refer below website for various functions
# https://docs.python.org/3/library/functions.html

# ls = [3, 10, 76, 45, 23, 135, 0, 289, 794]
# sums = 0

# for i in ls:
#     sums+=i

# print(sums) # 1375

# print(sum(ls)) # 1375

# HackerRank Min-Max-Sum Problem:
# def miniMaxSum(arr):
#     arr.sort()        # Sorting the list and then adding first 4 numbers in list to get minimum value.
#     miniSum = 0       # Then adding last 4 numbers in list to get maximum value.
#     maxSum = 0
#     for i in range(4):
#         miniSum+=arr[i]
    
#     print(miniSum, end=' ')
    
#     for i in range(4,0,-1):
#         maxSum+=arr[i]
    
#     print(maxSum, end=' ')

# ls = [3, 10, 76, 45, 23, 135, 0, 289, 794, 794]
# k = max(ls)
# print(k)
# count = 0
# for i in ls:               (OR)     for i in range(len(ls)):
#     if(i == k):                         if(ls[i] == k):
#         count+=1                            count+=1

# print(count)

#################################################################
# ls.sort()
# print(ls)
# ls.reverse()
# print(ls)