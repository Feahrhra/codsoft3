import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        desired_length = int(input("Specify the desired length of the password: "))
        if desired_length <= 0:
            print("Please enter a valid length.")
        else:
            password = generate_password(desired_length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
