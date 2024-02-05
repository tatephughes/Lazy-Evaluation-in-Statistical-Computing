def my_or_function(bool1, bool2):
  return (bool1 | bool2)

def bool_func_1():
   print("bool_func_1 was evaluated")
   return True

def bool_func_2():
   print("bool_func_2 was evaluated")
   return False

result = my_or_function(bool_func_1(), bool_func_2())
print(result)

def my_lazy_or_function(bool1, bool2):
    return (bool1 or bool2)

result = my_lazy_or_function(bool_func_1(), bool_func_2())
print(result)
