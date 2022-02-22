#!/home/ubuntu/Development/devsecops/bin/python
message = "Builtins"

bool()
The bool() function is very helpful in converting an object to a Boolean value. This function returns True, except the object is false, empty, 0 or none.
# a = bool(22)
# print(a)
# output = True

divmod()
Gets a tuple including the quotient and remainder when argument1 is divided by argument2.
# a = divmod(6, 2)
# 
print(a)
# output = (3, 0)

exec()
The exec() function executes dynamic python code.
# a = 'name = "John"\nprint(name)'
# print(exec(a))