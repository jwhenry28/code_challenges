import sys
import random
import string
from tempfile import TemporaryFile
import textwrap

main_prompt = """
--------------------------------------------------------------------------------
Welcome to Code1! In this challenge, you will be asked ten "riddles". 
Answering the riddle correctly will allow you to progress to the next riddle. 
Answering incorrectly will force you to restart. 

You can solve each riddle by looking at the source code of this program. Or you
could guess blindly, but I don't think that would work. Each riddle is related 
to string manipulation in Python. If you don't know what something means in the 
code, search for it online.

You can end the program by typing "exit" for any riddle, or by guessing 
incorrectly.

Good luck!
--------------------------------------------------------------------------------


"""

# This function just prints the riddle and then collects whatever input you give
# it. You don't need to look at this unless you are curious.
def level_start(str):
    for line in str.split("\n"):
        print(textwrap.fill(line, 80, replace_whitespace=False))
    user_str = input("Enter your guess\n> ").strip()

    if user_str.lower() == "exit":
        print("Goodbye!")
        sys.exit()

    return user_str

# Generates a string of eight random lowercase letters
def generate_random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=8))


### Start looking here! 
# Hint - you want each function to return True
def level1():
    user_string = level_start("This is an easy one. What is my name?")
    print(user_string)
    if (user_string == "CODE001"):
        return True #you want this
    return False #not this

def level2():
    user_string = level_start("This one requires learning a bit about string manipulation. What is my favorite color?")
    if (user_string == "purple".upper()):
        return True
    return False

def level3():
    user_string = level_start("Do you know what string concatenation is? That will help you on this level.")
    answer = "first" + "SECOND" + "third"
    if (user_string == answer):
        return True
    return False

def level4():
    user_string = level_start("There is more than one way to modify strings in Python...")
    answer = "aaa"
    answer += "BBB"
    answer += "ccc"
    if (user_string == answer):
        return True
    return False

def level5():
    clue = generate_random_string()
    prompt = "This challenge is about formatted strings. Look them up to see what they do! Your clue for this riddle is {clue}".format(clue=clue)
    user_string = level_start(prompt)
    if (user_string == (clue + " is my clue.")):
        return True
    return False

def level6():
    prompt = "By now, you've probably realized that strings are just a set of characters. Strings are a type of 'variable' in Python. You can think of a variable as a box that holds some value, like word or a number. There are other types of variables in Python too, such as an integer (int) which holds a whole number. You can convert a string into an int with the int() function. Use that knowledge to solve this level!"
    try:
        user_str = level_start(prompt)
        user_int = int(user_str)
        if (user_int == 100):
            return True
    except: # the exception will occur if you do not input an int
        print("I didn't recognize that number...")
        return False
    return False

def level7():
    prompt = """In Python, you can make 'decisions' with your code using 'if' statements. An 'if' statement looks like this:
if (condition):
    func()

In the above example, func() will only be executed if 'condition' returns true. If 'condition' returns false, func() will be skipped. Typically, 'condition' will be some kind of comparison, such as (x > y) or (user_string == 'CODE001').

'if' statements can also be complemented by an 'else' statement to provide a second response:
if (x > 100):
    func1()
else:
    func2()

In the above block, func1() will be executed if x is greater than 100 (where x is some integer variable). If x is less than or equal to 100, func2() will be executed. 

if/else blocks work great when we only have two options, but sometimes we want more than two choices. In this situation, we can use "elif" (short for "else if") like so:
if (x < 100):
    func1()
elif (x < 500):
    func2()
else:
    func3()

In the above example, func1() will be executed if x is less than 100. If x is greater than or equal to 100, but less than 500, func2() will execute. For any other value of x, func3() will execute. Note that we can add as many "elif" blocks as we want. It's also important to note that Python will pick the first branch where 'condition' returns true. So if x=50 in the example above, both 50 < 100 and 50 < 500 would return true. But only func1() would execute, because it is first.

This level deals with if/elif/else blocks. Enter three numbers separated by a space to make a guess. There are multiple correct solutions to this level. Try and find inputs to reach all three end points!
"""
    user_string = level_start(prompt)
    
    # Check to make sure user typed three numbers
    keep_searching = True
    while (keep_searching):
        try:
            nums = user_string.split()
            first_num = int(nums[0])
            second_num = int(nums[1])
            third_num = int(nums[2])
            keep_searching = False
        except:
            print("You didn't enter three numbers, separated by a space. Example: '1 2 3'. Try again!")
            user_string = input("> ")

    # if/elif/else block
    if (first_num > 100) and (second_num == 250):
        print("You found the first solution!")
        return True
    elif (first_num + second_num == third_num):
        print("You found the second solution!")
        return True
    elif (third_num == 1000) and (second_num < 0) and (third_num - first_num < second_num):
        print("You found the third solution!")
        return True
    else:
        return False

def level8():
    prompt = """In Python, we can perform various operations on int variables. This includes all basic arithmetic operations:
    addition: +
    subtraction: -
    multiplication: *
    division: /
    
In Python, there is a second numerical variable called a 'float'. You can think of floats as decimal numbers:

x = 4
y = 4.0

In the above example, x is an int and y is a float. Floats are stored differently on the computer than integers, which is why they can have the same numerical value but still be different types. We can convert from a float to an integer like so:
x = int(4.5)

Since integers must be whole numbers, this will drop the 0.5 and assign the value of 4 to x. It's also important to note that 'combining' an integer with a float will always return a float. So in the following examples:
x = 4.5 + 4
x = 4.5 * 4
x = 4.5 / 4
x = 4.5 - 4

x is always a float.

This level deals with numerical variables and operations in Python. Try to figure out the correct end result!
"""

    a = 9
    b = 4.5
    c = int(a * b)
    d = c / 4
    e = d + 5.5
    f = int(e - a)

    user_string = level_start(prompt)
    # Make sure user gave a number
    try:
        num = int(user_string)
    except:
        print("That is not a number. Please guess a number:")
        return False

    if (num == f):
        return True

    return False

def level9():
    prompt = "This level combines strings and numbers. You can convert a float or integer into a string with the str() function. If you want to concatenate a number with a string, you must convert the number into a string first. Or you can use the .format function shown earlier.\n\nAs a reminder, if you see something new, search for it online!"
    
    try:
        user_num = int(level_start(prompt))
    except:
        return False

    base_num = 1
    whole_num = base_num + user_num

    whole_num_string = str(whole_num)
    if (len(whole_num) > 10):
        return True
    return False

def level10():
    prompt = """This level introduces a new type of variable called a list. Lists are just a set of other variables and are declared with square brackets: [1, 2, 3]. These variables can be of any time, even other lists, and a list does not need to contain all variables of the same type. Therefore, these are all valid lists:
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = ["a", 2, 3.3]
list4 = [[1, 2, 3], ["a", "b", "c"], [1, "b", 3]]

You can access the nth element of a list using square brackets like so: 
list1 = [1, 2, 3]
first_element = list1[0]
second_element = list1[1]

It might be confusing that the first element is at list[0]. This is because the number inside the square bracket is the offset from the start of the list. So you can think of list[n] like "starting point of list" + "n". This makes list[1] the second element, list[2], the third element, and so on.

Lists can also be "sliced" to generate a subset of the list. This is also done with the square brackets. If you wanted a list of all objects in a given list between positions i and j, you would do:
bigger_list = [1, 2, 3, 4, 5]
smaller_list = bigger_list[i:j]

This would include everything between bigger_list[i] and bigger_list[j], including bigger_list[i] (but not bigger_list[j]). So for i=1, j=5, smaller_list would be [2, 3, 4].

This level has three sub-challenges that you must complete, related to everything you've learned so far. This is the hardest level :-) And remember, if you see something you don't know yet, search for it online!

For challenge one, you must enter two integers separated by a space.
"""

    user_string = level_start(prompt)
    keep_looping = True
    while keep_looping:
        try:
            nums = user_string.split()
            num1 = int(nums[0])
            num2 = int(nums[1])
            keep_looping = False
        except:
            print("Please enter two numbers separated by a space, like so: 1 2")

    ### First challenge
    master_list = [19, 20, 15, 24, 50, 16, 24, 3, 10, 34]

    if (num2 - num1 != 3):
        return False
    
    numbers = master_list[num1:num2]
    number_sum = numbers[0] + numbers[1] + numbers[2]
    if (number_sum < 90):
        return False
    
    print("Sub-challenge 1/3 completed!")

    ### Second challenge
    # You might need to look up what a "for loop" is in Python
    master_list = [
        [1, 2, "a"],
        [1, "a", 3],
        ["a", "b", "c"],
        [1, 2, 3],
        ["a", 2, 3]
    ]

    print("Enter a single number")
    user_string = input("> ")

    try:
        index = int(user_string)
        chosen_list = master_list[index]
    except:
        return False

    for element in chosen_list:
        if isinstance(element, int):
            return False

    print("Sub-challenge 2/3 completed!")

    ### Third challenge
    # Hint:           0          1       2       3      4        5     6        7         8       9
    master_list = ["logging", "there", "words", "are", "fish", "some", "in", "sentence", "this", "blue"]
    print("Enter a list of numbers, separated by spaces")
    user_string = input("> ")
    try:
        list_indexes_strings = user_string.split()
        list_indexes = [int(x) for x in list_indexes_strings]
    except:
        print("wrong")
        return False

    selected_strings = [master_list[x] for x in list_indexes]
    final_string = ' '.join(selected_strings)

    print("[" + final_string + "]")
    if (final_string != "there are words in this sentence"):
        return False

    print("Sub-challenge 3/3 completed!")
    return True


### Don't worry about this code unless you are just curious
def main():
    print(main_prompt)

    funcs = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]
    print("Enter a level number to skip ahead, or else press enter to start at the beginning.")
    num_str = input("What level would you like to try?\n> ")
    try:
        i = int(num_str) - 1
    except:
        i = 0

    if i < 0 or i >= 10:
        print("That number is out of bounds. There are only {num} levels.".format(num=len(funcs)))
        sys.exit()

    print("Starting at level {num}\n".format(num=i+1))

    while i < 10:
        print("[Level {num}] \n".format(num=i+1), end="")
        res = funcs[i]()
        if (not res):
            print("Sorry, that is incorrect. Goodbye!\n")
            sys.exit()
        i += 1
        print("Correct! Moving on to level", i+1, "\n")

    print("Congratulations! You win! I hope you enjoyed this and learned something about computer programming.")

main()
