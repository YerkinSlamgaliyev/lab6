import math
import time

def multiply_list(numbers):
    return math.prod(numbers)

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)

def all_true(t):
    return all(t)

numbers = list(map(int, input("Enter numbers separated by spaces to multiply: ").split()))
print(f"Product of numbers: {multiply_list(numbers)}")

string = input("Enter a string to count upper and lower case letters: ")
upper, lower = count_case(string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

palindrome_string = input("Enter a string to check if it's a palindrome: ")
print(f"Is the string a palindrome? {is_palindrome(palindrome_string)}")

num = float(input("Enter a number to find the square root of: "))
delay = int(input("Enter delay in milliseconds: "))
print(f"Square root after delay: {delayed_sqrt(num, delay)}")

bool_values = tuple(map(bool, map(int, input("Enter boolean values (1 for True, 0 for False) separated by spaces: ").split())))
print(f"Are all values True? {all_true(bool_values)}")
