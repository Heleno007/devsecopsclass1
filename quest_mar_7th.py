#!/home/helen/Development/devsecops/bin/ python
#write some code that randomly picks a price from your price list (9.42, 5.67, 3.25, 13.40, 7.50) and prints True if the price is greater than 10 or false if its not.
#Ans
import random
price_list= [9.45, 5.67, 3.25, 13.40, 7.50]
random_price = random.choice(price_list)
for each in price_list:
    if each > 10.00:
        print(each, "True") 
    else:
        print(each, "False")
#You are provided with the following list ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']. Write code to print True if the following items ['bread', 'rice', 'okra', 'water', 'egusi'] are found in the list. Can you do this with a for loop?
#Ans
list1 = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogbono', 'eru']
list2 = ['bread', 'rice', 'okra', 'water', 'egusi']
for each in list1:
    if each == each in list2:
        print(each, 'True')
    else:
        print(each, 'False')
#Write a for loop that prints every letter in the phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
#Ans
phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
for each in phrase:
    print(each)
#Create a grocery list. Now use a for loop to print the words "Note to self, buy" and the grocery item.
#Ans
grocery_list= ['bread', 'rice', 'okra', 'water', 'egusi']
for each in grocery_list:
    print("Note to self, buy", each)
#Now create a for loop that prints a numbered list of your grocery items.
#Ans
grocery_list= [[1,'bread'], [2,'rice'], [3,'okra'], [4,'water'], [5,'egusi']]
for k,v in grocery_list:
    print(k,v)
#Evidently your favorite snack is more important than anything else in your grocery list. Modify the last exercise to stop if and when it finds your favorite snack in your grocery list.
#ans
item_list = ["cheetos", "bread", "cashew_nuts", "tomatoes","onions"]
for each in item_list:
    print(each)
    if each == "cashew_nuts":
        break
#Use the string split method, to segment all the words in the phrase ""Blood-oxygenation level dependent functional magnetic resource imaging" using a for loop.
#Ans
my_str = "Blood-oxygenation level dependent functional magnetic resource imaging"
print(my_str.split())
#Use the range method to write a for loop to print out a numbered grocery list. if you have not created a groucery list, create it.
#Use enumerate to print out a numbered grocery list. if you don't have a grocery list, create one.
lst = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogbono', 'eru']
for count, value in enumerate(lst, start=1):
    print(count, value)