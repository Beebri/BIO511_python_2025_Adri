# Practical 3: Python Functions
#==============================================================================
#3.1 Defining a function
"""
def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return
#3.2 Calling the function
my_added_numbers = add_two_numbers(1, 1)

print(my_added_numbers) # will print 2  
"""
#==============================================================================
# 4.O defined variables
# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"
#==============================================================================
# 4.1 
# Count-above  (uses nums, limit, count)
# Goal: make a small function called whatever you want and then call(run) it.

# a) Define a function named count_above that takes two arguments: seq and lim.
"""
def count_above(seq, lim):
# b) Inside the function, create a LOCAL variable named count starting at 0.
    count = 0
# c) Loop through seq; for each number strictly greater than lim, increase count by 1.
    for n in seq:
        if n > lim:
            count += 1
# d) Return count.
    return count
# e) Outside the function:
#    - Print the GLOBAL count.
#    - Call count_above(nums, limit) and print the returned number.
#    - Print the GLOBAL count again (notice the global didn’t change).
print(count)
x = count_above(nums, limit)
print(x)
print(count)
"""
# Your code below
def count_above(seq, lim):
    count = 0
    for n in seq:
        if n > lim:
            count += 1
    return count
print(count)
x = count_above(nums, limit)
print(x)
print(count)
#==============================================================================
#4.2 
# Text summary  (uses text, summary)
# Goal: classify characters with an if/elif/else chain and return a clear result.

# a) Define a function named summarize_text that takes one argument: s.
"""
def summarize_text(s):
# b) Inside the function, create a LOCAL variable named summary that holds a result dictionary
#    with exactly these keys: "digits", "letters", "other" — each starting at 0.
    summary = {"digits" : 0, "letters" : 0, "other": 0 }
# c) Loop through each character in s:
#       - if the character is a digit, increase "digits"
#       - elif the character is a letter, increase "letters"
#       - else increase "other"
    for character in s:
        if character.isdigit():
            summary["digits"] += 1
        elif character.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
# d) Return the summary dictionary.
    return(summary)
# e) Outside the function:
#    - Print the GLOBAL summary.
#    - Call summarize_text(text) and print the returned dictionary.
#    - Print the GLOBAL summary again.
print(summary)
y = summarize_text(text)
print(y)
print(summary)
"""
# Your code below
def summarize_text(s):
    summary = {"digits" : 0, "letters" : 0, "other": 0 }
    for character in s:
        if character.isdigit():
            summary["digits"] += 1
        elif character.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return(summary)
print(summary)
y = summarize_text(text)
print(y)
print(summary)
 #==============================================================================
# 4.3
#C) Aggregate with mode  (uses nums, limit, result)
# Goal: nested decisions based on a mode string. Return one final value.

# a) Define a function named aggregate that takes three arguments: seq, mode, threshold.
"""
def aggregate(seq, mode, threshold):
# b) Inside the function, create a LOCAL variable named result.
#    Initialize it based on mode:
#       - if mode is "sum": start at 0
#       - if mode is "count": start at 0
#       - if mode is "max": start at None (meaning “no qualifying value yet”)
    result = {"sum":0, "count":0, "max":0}
    
    if mode == "sum":
        result["sum"] = 0
    elif mode == "count":
        result["count"] = 0
    elif mode == "max":
        result["max"] = -1
    else:
        print("no modes found")
    for n in seq:
        if n < 0:
            print(f"ignored negative number {n}")
        elif n >= threshold:
            if mode == "sum":
                result["sum"] += n
            elif mode == "count":
                result["count"] += 1
            else:
                if n > result["max"] or result["max"] == -1:
                    result["max"] = n
    return(result)
                
print(result)
a = aggregate(nums, "sum", limit)
b = aggregate(nums, "count", limit)
c = aggregate(nums, "max", limit)
print(a)
print(b)
print(c)
print(result)
"""
            
# c) Loop through each number n in seq:
#       - First, ignore n if it is negative (skip it).
#       - If n is at least threshold, then:
#           * if mode is "sum": add n to result
#           * elif mode is "count": increase result by 1
#           * else (treat any other mode as "max"):
#                 if result is None or n is greater than result, update result to n

# d) Return the result.

# e) Outside the function:
#    - Print the GLOBAL result.
#    - Call and print each of these:
#         aggregate(nums, "sum", limit)
#         aggregate(nums, "count", limit)
#         aggregate(nums, "max", limit)
#    - Print the GLOBAL result again.

# Your Code below
def aggregate(seq, mode, threshold):
    result = {"sum":0, "count":0, "max":0}
    
    if mode == "sum":
        result["sum"] = 0
    elif mode == "count":
        result["count"] = 0
    elif mode == "max":
        result["max"] = -1
    else:
        print("no modes found")
    for n in seq:
        if n < 0:
            print(f"ignored negative number {n}")
        elif n >= threshold:
            if mode == "sum":
                result["sum"] += n
            elif mode == "count":
                result["count"] += 1
            else:
                if n > result["max"] or result["max"] == -1:
                    result["max"] = n
    return(result)
                
print(result)
a = aggregate(nums, "sum", limit)
b = aggregate(nums, "count", limit)
c = aggregate(nums, "max", limit)
print(a)
print(b)
print(c)
print(result)
