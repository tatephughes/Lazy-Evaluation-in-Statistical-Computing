def bool_func_1():
   print("bool_func_1 was evaluated")
   return True

def bool_func_2():
   print("bool_func_2 was evaluated")
   return False

result = bool_func_1() | bool_func_2()
print(result)

result = bool_func_1() or bool_func_2()
print(result)

def my_or_function(bool1,bool2): return bool1 or bool2

print(my_or_function(bool_func_1(),bool_func_2()))
