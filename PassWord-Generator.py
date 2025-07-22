import random
import string

def generate_password(length=12):
    # Characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Simple Password Generator")
    try:
        length = int(input("Enter desired password length (e.g., 8-16): "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
