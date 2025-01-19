def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()
