# A simple prime number checker
n = int(input("Enter a number: "))

if n <= 1:
    print("Neither a prime nor composite number")
else:
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Composite number")