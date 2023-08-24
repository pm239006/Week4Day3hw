
#Week4 Day# Homework



# Most of the problems I have solved on Codewars have been the super simple problems since I have
# been struggling a lot to grasp the more advanced python problems. 

# 1 the question 
# Write a function that removes the spaces from the string, then return the resultant string.

# Examples:

# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"

#my response 

def no_space(x):
    for words in x:
        x = x.replace(" ", '')
    return x


# Since I used a for loop (so the loop traverses each character) I believe I made a soultion that was O(n) 
# bc it moves in current time, this time will increase based on the input or chars coming into the loop. 






# 2 the question 
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

#my solution 

def make_negative( number ):
    if number > 0:
        return number * (-1)
    elif number < 0: 
        return number
    else:
        return 0
# I believe this solution is O(1) because it moves in constant time.

#alternate way of solving 

def make_negative( number ):
    return number * -1 if number > 0 else number

#this is a better solution for space however, for time complexity it is also O(n) and moving in constant time.
#(I tried to find other ways to solve this more efficiently but 6 steps is the lowest I could get to in pythontutor)




#3 the question 
# convert a string to an array 

# my solution
#speed is O(n) since the length of the input will affect how long it takes to change the strings to arrays
def string_to_array(s):
    my_list = s.split(" ")
    return my_list



#alternate solution

def string_to_array(s):
    return s.split(" ")

#This solution I came up with originally is more efficent, the alternate solution divides the entire string by individul char
#meanwhile my solution grabs each "word" in the string an converts it to a list of strings. .split() is also linear it
#scans through each item and the more data we have inside, the longer it will take to complete the scan.

