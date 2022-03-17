#!/home/helen/Development/devsecops/bin/ python
#Write a python function that takes one argument, which is a list and swaps the first and last items on that list
#Write the code that allows you to show that your function works as it should

def groceries(item):
    item [0], item[-1] = item [-1], item[0]
    return item
item = ['peanuts', 'cashew_nuts', 'cheetos', 'walnuts']
print(groceries(item))

#Write a pythhon function that takes one argument which is a string and reverses the order of the words in the string.
#Write the code allowing you to show that your function works
def reversed_string(text):
    result = "" 
    for char in text:
        result = char + result
    return result
reversed_string("Keep being awesome!")

def reverse_string(text):
    return text[::-1]
story = reverse_string("My name is Helen!")
print(story)
# Create a dictionary and display its keys alphabetically.
#Display both the keys and values sorted in alphabetical order by the key.
# Function calling
def dictionairy():
 # Declare hash function     
    key_value ={}   
# Initializing value
    key_value[2] = 56      
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18     
    key_value[3] = 323

print ("Task 1:-\n")
print ("Keys are:")
# iterkeys() returns an iterator over the
# dictionary’s keys.
for i in sorted ('key_value'.keys()) :
    print(i, end = " ")
def main():
    # function calling
    dictionairy()            
# Main function calling
    if __name__=="__main__":
        main() 
#Same as part (ii), but sorted in alphabetical order by the value.
def dictionairy():
# Declaring the hash function     
    key_value = {}
# Initialize value
    key_value[2] = 56      
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18     
    key_value[3] = 323
print ("Task 2:-\nKeys and Values sorted in",
            "alphabetical order by the key  ") 
# sorted(key_value) returns an iterator over the
# Dictionary’s value sorted in keys. 
for i in sorted (key_value):
    print ((i, key_value[i]), end =" ")

def main():
    # function calling
    dictionairy()            
# main function calling
if __name__=="__main__":    
    main()

#Write a python function called doings that takes one argument named number. if number is even, doings should print dividing number by 2, 
#divide number by two and return the answer. if number is odd,the function should print, multiplying number by 3 and adding one, then multiply number 
#by 3 and add one to it and return that result. Then write a function that allows a user to enter the numbers that get passed to the doing function. 
#It should keep asking for the number as long as the result of doings is not 1.
#Write two functions. One should use a for loop to print the numbers between 1 and 100. 
for i in range(1, 101):
    print(i, end=" ")
print()
# The second should use a while loop to print the numbers between 1,
# and 100.
num = 1
while num <=100:
    print(num)
    num = num + 1
#Write a Python program to square and cube every number in a given list of integers using Lambda.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
#Write a Python program to check whether a given string is number or not using Lambda.
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))
