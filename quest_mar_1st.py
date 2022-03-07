<<<<<<< HEAD
#!/home/helen/Development/devsecops/bin/python
#Identify the type of each of the following variables and write it as a comment next to the variable
a = 299 #  int
print(type(a))
b = 90.0 # a float
print(type(b))
c = "145" # str
print(type(c))
d = "\u0CA0_\u0CA0" #str
print(type(d))
e = "True" # str
print(type(e))
f = True # bool
print(type(f))
g = len('Sample') # str
print(type(len(g)))
h = 100**30 # int
print(type(h))
i = 1 >= 1 # bool
print(type(i))
j = 30%7 #int
print(type(j))
k = 30/7 #float
print(type(k))
l = b + 7 # int
print(type(l))
m = 128 << 1 # int
print(type(m))
n = bin(255) # str
print(type(n)
o = ['k', 'l', 'm', 'n' ] # list
print(type(o))
p = len('o') # int
print(type(p))
#What value is at the end of the varialbe my_var at the end of these assignments. Add a comparison after the last statement
#in the form of my_val ==
my_var = 99
my_var += 11
print (my_var)
my_var = str(my_var)
print(my_var)
my_var *= 2
print(my_var)
my_var = len(my_var)
print(my_var)
my_var *= 4
print(my_var)
my_var = 24
if my_var  == 4:
   print(my_var)
else:
   print(my_var)
#Change the loop below so that it prints the numbers from 1 to 10
for i in range(0, 11):
    print(i)
#Save a copy of your favorite snack as a variable. Using that variable, print your favorite snack 100 times
fav_snack = ('cashew_nuts ')*100
print(fav_snack)   
#Make a list of your grocery items with prices 9.42, 5.67, 3.25, 13.40, 7.50 and store it as a variable. Using a builtin function, #find the cheapest and the most expensive items on your shopping list
item_list = {'cheetos':3.25,'cashew_nuts':13.40, 'milk':7.50, 'cereal':5.67,'juice':9.42}
maximum = max(item_list.values())
minimum = min(item_list.values())
print(maximum)
print(minimum)
#Import random. run dir(random.randint). Use Randint to randomly print between 0 and 100 copies of your favorite snack
import random
rand_num = random.randint(0,101)
for i in range(rand_num):
    print('cheetos')
#Run dir(random). Find a function in random that you can use to print a random item from your grocery list. Remember you can use #help to find out what functions do.
import random
item_list = ["cheetos", "cashew_nuts", "bread", "tomatoes","onions"]
random_item = random.choice(item_list)
print(random_item)
#Write code to randomly select items from your groceries list, round them to the nearest integer and print the result.
import random
item_list = [3.25, 13.40, 7.50, 5.67, 9.42]
random_item = random.choice(item_list)
print(round(random_item))
#Previously,we used the * operator to print a hundred copies of your favorite snack. This time use a while loop to print 50 copies of your favorite snack.
count = 0
while count <= 50:
    print("cheetos")
count +=1
print(count)
#Mix and Match! Write a while loop that uses the * operator to print multiple copies of your favorite snack per line. Print out 10 lines where the first line has one copy of your favorite snack and the last line hast 10.
count = 0
while count<= 100:
    print("cheetos "*1)
    print("cheetos "*10*10)
    break
print(count)
#Challenge: Your neighborhood grocery store is having a weird promotion called "Win free change". A random item is picked from your #grocery list and you pay 10 dollars. If the item is less than 10 dollars, you get the item and the balance from the items price. 
#If the item is more than 10 dollars, you get the item and the difference in the price as change. Write the code to randomly pick a #price from your price list and print out the amount the cashier
=======
#!/home/helen/Development/devsecops/bin/python
#Identify the type of each of the following variables and write it as a comment next to the variable
a = 299 #  int
print(type(a))
b = 90.0 # a float
print(type(b))
c = "145" # str
print(type(c))
d = "\u0CA0_\u0CA0" #str
print(type(d))
e = "True" # str
print(type(e))
f = True # bool
print(type(f))
g = len('Sample') # str
print(type(len(g)))
h = 100**30 # int
print(type(h))
i = 1 >= 1 # bool
print(type(i))
j = 30%7 #int
print(type(j))
k = 30/7 #float
print(type(k))
l = b + 7 # int
print(type(l))
m = 128 << 1 # int
print(type(m))
n = bin(255) # str
print(type(n)
o = ['k', 'l', 'm', 'n' ] # list
print(type(o))
p = len('o') # int
print(type(p))
#What value is at the end of the varialbe my_var at the end of these assignments. Add a comparison after the last statement
#in the form of my_val ==
my_var = 99
my_var += 11
print (my_var)
my_var = str(my_var)
print(my_var)
my_var *= 2
print(my_var)
my_var = len(my_var)
print(my_var)
my_var *= 4
print(my_var)
my_var = 24
if my_var  == 4:
   print(my_var)
else:
   print(my_var)
#Change the loop below so that it prints the numbers from 1 to 10
for i in range(0, 11):
    print(i)
#Save a copy of your favorite snack as a variable. Using that variable, print your favorite snack 100 times
fav_snack = ('cashew_nuts ')*100
print(fav_snack)   
#Make a list of your grocery items with prices 9.42, 5.67, 3.25, 13.40, 7.50 and store it as a variable. Using a builtin function, #find the cheapest and the most expensive items on your shopping list
item_list = {'cheetos':3.25,'cashew_nuts':13.40, 'milk':7.50, 'cereal':5.67,'juice':9.42}
maximum = max(item_list.values())
minimum = min(item_list.values())
print(maximum)
print(minimum)
#Import random. run dir(random.randint). Use Randint to randomly print between 0 and 100 copies of your favorite snack
import random
rand_num = random.randint(0,101)
for i in range(rand_num):
    print('cheetos')
#Run dir(random). Find a function in random that you can use to print a random item from your grocery list. Remember you can use #help to find out what functions do.
import random
item_list = ["cheetos", "cashew_nuts", "bread", "tomatoes","onions"]
random_item = random.choice(item_list)
print(random_item)
#Write code to randomly select items from your groceries list, round them to the nearest integer and print the result.
import random
item_list = [3.25, 13.40, 7.50, 5.67, 9.42]
random_item = random.choice(item_list)
print(round(random_item))
#Previously,we used the * operator to print a hundred copies of your favorite snack. This time use a while loop to print 50 copies of your favorite snack.
count = 0
while count <= 50:
    print("cheetos")
count +=1
print(count)
#Mix and Match! Write a while loop that uses the * operator to print multiple copies of your favorite snack per line. Print out 10 lines where the first line has one copy of your favorite snack and the last line hast 10.
count = 0
while count<= 100:
    print("cheetos "*1)
    print("cheetos "*10*10)
    break
print(count)
#Challenge: Your neighborhood grocery store is having a weird promotion called "Win free change". A random item is picked from your #grocery list and you pay 10 dollars. If the item is less than 10 dollars, you get the item and the balance from the items price. 
#If the item is more than 10 dollars, you get the item and the difference in the price as change. Write the code to randomly pick a #price from your price list and print out the amount the cashier
>>>>>>> c0c3e85e7b7d4fde3440545fca0839bea06f8324
