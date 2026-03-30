
def is_prime():
    n = int(input("Is this a prime number? "))
    if n <= 1:
        print(False)
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        print(prime)

is_prime()

    