# STRINGS - Sequence of characters.
# Terminated with a special character '\0'.
# Immutable objects.

# hi = "This is an example of a string"
# print(hi)

# name = input("Enter your Name: ")
# hi = "Hello "
# hi += name          # Enter your Name: Gagan
# print(hi)           # Hello Gagan

# hi = "World"
# hi = "r" + hi
# print(hi)             # rWorld

# ls1 = [1,2,3,4,5]
# print(ls1*3)            # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# string = "Python Lover"

# for i in range(len(string)):
#     if string[i] == 'L':
#         print(i)            # 7

# string = "Python Lover"
# char = 'o'       #input("Enter keyword to search: ")
# print(string.find(char))    # 4 --> Positive Index
# print(string.rfind(char))   # 8 --> Use .rfind to find character from reverse i.e, Negative Index
#                             # But the search starts from the first.

# s = "Hulk Captain America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos"

# print(s[:])         # Hulk Captain America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos
# print(s[10:])       # in America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos
# print(s[:60])       # Hulk Captain America Black Widow Dr Strange Spiderman Black
# print(s[21:39])     # Black Widow Dr Str

# ls = [1,2,3]
# print(ls[4])        # IndexError: list index out of range

# s = "The Avengers"
# print(s)                # The Avengers
# print(s.upper())        # THE AVENGERS
# print(s.lower())        # the avengers

# s = "the avengers"

# print(s.capitalize())      # The avengers  (First letter of string gets capitalized)

# s = "Hulk Captain America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos"
# print(s.split())        # ['Hulk', 'Captain', 'America', 'Black', 'Widow', 'Dr', 'Strange', 'Spiderman', 'Black', 'Panther', 'Winter', 'Soldier', 'Falcon', 'Iron', 'Man', 'Thanos']
# Converts the words in string to a list

# s = "Hulk* Captain America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos"
# print(s.split("*"))
# # ['Hulk', ' Captain America Black Widow Dr Strange Spiderman Black Panther Winter Soldier Falcon Iron Man Thanos']


# s = "2345643"
# print(s.isdigit())  # True


### DICTIONARY ###
# Is a built-in mapping type
# Makes keys to value
# Provides useful way to store data

# d = {"name" : "Gagan", 23 : "age", True : "Male"}
# print(d)
# print(type(d))

# from math import *
# print(pi)               # 3.141592653589793
# print(factorial(5))     # 120

# print(ceil(7.8))        # 8
# print(floor(7.8))       # 7

### HackerRank ###
# Swap Case

# def swap_case(s):
#     k = list(s)
#     for i in range(len(s)):
#         if k[i].isupper():
#             k[i] = k[i].lower()
#         elif k[i].islower():
#             k[i] = k[i].upper()
            
#     s = ""
#     for i in k:
#         s += i
#     return s

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# Capitalize (Type-1)
# Works for all types of characters.
# def solve(s):
#     string = ""
#     for i in range(len(s)):
#         if i == 0:
#             string += s[i].capitalize()
#             continue
#         if(s[i-1] == " "):
#            string += s[i].capitalize()
#            continue
        
#         string += s[i]
#     return string


## Capitalize (Type-2) ##
# Only works for letters not numbers.
# def solve(s):
#     p = s.split()
#     string = ""
#     for i in p:
#         string += i.capitalize() + " "
        
#     s = string
#     return s

# list1 = [1,2,3]
# list2 = list1
# list1[0] = 4
# print(list2)