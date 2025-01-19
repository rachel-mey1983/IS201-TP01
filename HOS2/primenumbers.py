def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    print(f"{num} is {'a' if is_prime(num) else 'not a'} prime number")

if __name__ == "__main__":
    main()
	
	