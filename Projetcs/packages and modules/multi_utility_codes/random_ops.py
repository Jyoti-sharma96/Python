import random
import string

def generate_random_number():
    print(f"Random Number: {random.randint(1, 100)}")

def generate_random_list():
    lst = [random.randint(1, 50) for _ in range(5)]
    print(f"Random List: {lst}")

def generate_random_password():
    try:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        pwd = "".join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {pwd}")
    except ValueError:
        print("Invalid input.")

def generate_random_otp():
    print(f"Generated OTP: {random.randint(1000, 9999)}")