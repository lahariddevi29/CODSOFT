import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length should be a positive integer")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer for the length.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
