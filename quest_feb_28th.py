#!/home/helen/Development/devsecops/bin/python
# 1. Make a shopping list of 5 things you need at the grocery store # put each item on a line by itself
#Ans
my_list = ["milk", "sugar", "veggies", "bread", "tissue"]
for item in my_list:
    print(item)

#2 Your items ring up as 9.45, 5.67, 3.20, 7.47 and 20.23. Use python as a handy # calculator to calculate the total of your shopping.
#Ans
milk = 9.45
sugar = 5.67
veggies = 3.20
bread = 7.47
tissue = 20.23
result=(9.45+5.67+3.20+7.47+20.23)
print(result)

#3. But wait, you decide to buy five more of the last item. Recalculate the total
#Ans
milk = 9.45
sugar = 5.67
veggies = 3.20
bread = 7.47
tissue = 20.23*6
result=(9.45+5.67+3.20+7.47+(20.23*6))
print(result)
#4. Usingg a built in function, determine the length of this phrase: 'Blood oxygenation level dependant functional magnetic resource imaging'.
#Ans
my_phrase = len('Blood oxygenation level dependant functional magnetic resource imaging')
print("The length of str is: ", my_phrase)
#5. Pick your favorite snack, use the * operator to print it a 100 times.
#Ans
my_snack = 'popcorn'*100
print(my_snack)
#6 Modify the code to print it with spaces in between.
my_snack = ('popcorn ') *100
print(my_snack)
#7 Challenge: run 'dir('any_string')' Pick any two interesting methods and #run 'help('any_string'.interesting_method)' Can you figure out how to use these #methods
#8 Bonus Challenge Can you figure out how to do the same thing on exercise 1 with just one line
