#Boolean represent one of two values: True or False
# bool() function allows you to evaluate any value, and give you True or False in return.
# Almost any value is evaluated to True if it has some sort of content; any string is True, except empty strings; any number is True, except 0; any list, tuple, set and dictionary are True, except empty ones.
def bool_test(a) :
    return bool(a)

print(bool_test("String"))  
print(bool_test(30))
print(bool_test([]))
print(bool_test(["a non empty", "list"]))

# Creating a Function
def type_check(a):
    if type(a) == str:
        return "this variable type is: String"
    if type(a) == int:
        print("this variable type is: Integer")
    if type(a) == float:
        print("this variable type is: Float")
    if type(a) == list:
        print("this variable type is: List")
print(type_check(5))

print("hello!">"hello")
print((3*0)==(0))
print("house"=="home")

def evenodd(a):
    if len(a) % 2 == 0:
        return "even"
    else:
        return "odd"


def function_name(variable_input):
    #This is my first function
    print("I am running my function")
    variable_output = variable_input + " World"
    return(variable_output)
printing_var = function_name("Hi")
print(printing_var)


def function_name(variable_input):
    print("I am running my function!")
    variable_output = variable_input + " world!"
    return variable_output

print(function_name("Hello"))

def double_input(input):
    output = input*2
    return output
print(double_input("Hello"))
print(double_input(2))
print(double_input([1,2,3]))


def multiple_input(var1,var2):
    type(var1) == int, type(var2) == list
    print(var2)
    printing_output = var2[var1]
    return printing_output
print(multiple_input(0,[1,2,3,4]))
print(multiple_input(2,["var1","var2","var3","var4"]))
print(multiple_input(-1,[1,2,3,4]))


def square_times(var_one,var_two):
    type(var_one),type(var_two) == int or float
    square = var_one**2
    times = square*var_two
    return times
print(square_times(3,9))
print(square_times(-3,2))

def uniques(list):
    list_set = set(list)
    uniques = list_set
    return uniques
print(uniques[1,2,2,3])
