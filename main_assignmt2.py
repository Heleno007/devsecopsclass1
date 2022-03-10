#!/home/helen/Development/devsecops/bin/python
#Write a function called all_the_snacks that takes one argument. Use the * operator to print that snack 100 times.
#ans
all_the_snacks = 'peanuts '*100, 'cashew_nuts ', 'biscuits ', 'plantain_chips '
print(all_the_snacks)

#Test your function using multiple items from your grocery list. If you don't have a grocery list, this would be a good time to
#create one
#Ans
grocery_list = ['bread '*100, 'butter '*100, 'groundnuts '*100, 'sugar '*100, 'garri '*100, 'egusi '*100, 'ogbono '*100]
print(grocery_list)

#You notice that your all_the_snacks prints your snacks all squished together. Rewrite the function to take a second argument, #called spacer which we will use to put some space between the snack items. 
spacer = ['bread '*100,'butter '*100, 'groundnuts '*100, 'sugar '*100, 'garri '*100, 'egusi '*100, 'ogbono '*100]
for each in spacer:
    print("\n",each)
#Try your rewritten function with multiple inputs
#Ans
all_the_snacks = 'peanuts ', 'cashewnuts ', 'biscuits ', 'plantain_chips '
favorite = input("Enter your favorite snack here: ")
print(favorite)
#Rewrite your all_the_snacks function so that it takes an additioanl argument called num. Use this variable to customize how many #times your snack is printed out.
#Ans
all_the_snacks = 'peanuts ', 'cashew_nuts ', 'biscuits ', 'plantain_chips '
num= 'peanuts ', 'cashew_nuts ', 'biscuits ', 'plantain_chips '
for each in num:
    print("\n",each*10)
#Write a price_matcher function that takes no arguments but prints a random item from your grocery list everytime it is run.
#ans
import random
grocery_list = ['bread', 'butter', 'groundnuts', 'sugar'] 
random  = random.choice(grocery_list)
for item in random:
    print(item)
#Write an in_grocery_list function that takes a grocery list and prints true if the item is on your grocery list and false if #otherwise
in_grocery_list = 'peanuts ', 'cashew_nuts ', 'biscuits ', 'plantain_chips '
for each in in_grocery_list:
    if each == each in in_grocery_list:
        print(True)
    else:
        print(False)
#Write the all the snacks function so that num and spacer have default values of 100 and ',' respectively.
#Ans
all_the_snacks = 'peanuts ', 'cashew_nuts ', 'biscuits ', 'plantain_chips '
num= 'peanuts'', ', 'cashew_nuts '', ', 'biscuits '', ', 'plantain_chips'', '
spacer = ['bread'', '*100,'butter'', '*100, 'groundnuts'', '*100, 'sugar'', '*100, 'garri'', '*100, 'egusi'', '*100, 'ogbono'', '*100]
for each in num:
    print("\n",each*100)
for each in spacer:
    print("\n",each)
#Challenge: use input to get your neighbors favorite color and store it as a variable.
fav_col = input("Enter neighbor's fav color here: ")
print(fav_col)
#Write an april_fools_color_swapper that uses input to get your favorite color, uses input to get your neighbors color and then prints them with your name and your neighbor's name. On the next line, it should swap your color for your neighbors color and print them.
Helen_col = input("Helen's color is: ")
David_col = input("David's color is: ")
Helen_col, David_col= David_col, Helen_col
print('Helen_col: ', Helen_col)
print('David_col: ', David_col)
#Create a function called shout which ask a user for their name and shouts it back to them
#So if the user is called Nora, your function should print HELLO NORA!
def shout(word="HELLO NORA"):
    return word.capitalize()+"!"
print(shout())
