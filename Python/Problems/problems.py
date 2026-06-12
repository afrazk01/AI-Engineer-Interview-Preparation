# reverse an integer 
def reverse_integer(x):
    if x < 0:
        sign = -1
    else:
        sign = 1
    x = abs(x) # we take absolute because absolute value of a number is always positive
    rev = 0
    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10
    return sign * rev

a = -123
print(reverse_integer(a))

print('------------------')

a = 'hello world'
print(a[::-1]) # this is a slicing technique to reverse a string first we take the whole string and then we step backwards with -1

s = "baba"
index = 0
length = len(s)-1
s = list(s) # we convert the string to a list because strings are immutable in python and we cannot change them directly
while index < length:
    s[index], s[length] = s[length], s[index] # we swap the characters at index and length
    index += 1
    length -= 1
print(''.join(s)) # we convert the list back to a string and print it


# if is a palindrome
def is_palindrome(value):
    s = str(value).lower() # we convert the input to a string and then to lowercase to ignore case sensitivity
    return s == s[::-1] # we check if the string is equal to its reverse
print(is_palindrome('bab')) # this is a famous palindrome phrase

# sum of numbesr in a list
def sum_of_numbers(lst):
    total = 0
    for num in lst:
        total += num
    return total

# find minimum and maximum in a list
def find_minimum_and_maximum(lst):
    if not lst:
        return None, None # if the list is empty we return None for both minimum and maximum
    minimum = lst[0]
    maximum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

# find duplicate elements in a list
def find_duplicates(lst):
    seen = set() # we use a set to keep track of seen elements because sets do not allow duplicates
    duplicates = set() # we use another set to keep track of duplicates
    for num in lst:
        if num in seen:
            duplicates.add(num) # if the number is already seen we add it to duplicates
        else:
            seen.add(num) # if the number is not seen we add it to seen
    return list(duplicates) # we convert the set of duplicates back to a list and return it