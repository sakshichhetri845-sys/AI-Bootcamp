# A simple palindrome checker
n = int(input("Enter a number: "))
og = n
r = 0

while n > 0:
    digit = n % 10
    r = r * 10 + digit
    n //= 10

if og == r:
    print("Palindrome number")
else:
    print("Not a palindrome number")