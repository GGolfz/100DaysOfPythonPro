def prime_checker(number):
    prime = True
    if number < 2:
        prime = False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
    print("It's not a prime number." if not prime else "It's a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)