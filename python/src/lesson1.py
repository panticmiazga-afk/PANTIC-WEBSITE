# # Hello Lesson 1 Python project

# import datetime

# print("Hello! Welcome to Python world!")
# name = input("What is your name?")
# hobby = input("What is your favorite hobby?")

# # get current date and  time

# now = datetime.datetime.now()

# print("\n---Personal Greeting---")
# print(f"Hi {name}! It's {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
# print(f"Enjoy coding while you {hobby}!")


""""
# YOUR TASK (ASSIGNMENT PROJECT 1)

#importing date time

import datetime

print("Hello! User Welcome to our site")

name = input("What is your name? ")
hobby = input("What is favorite hobby? ")
age = input("What is your age? ")
goal = input("In a sentence provide you academic goal... ")

print("Thank you for your user details")

#getting the current date and time

now = datetime.datetime.now()


print("\n---Personal Greeting---")

print(f"Hello {name}! It's {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
print(f"{name}, have a nice time🌀☃🌜🌝🌈")


# PROJECT 2 "CHATBOT GREETER"

print("👋Hello! I'm ChatBot 2.0")

name = input("What is your name? ")

#type conversion

age = int(input("How old are you? "))
subject = input("What is your favorite subject?")

future_age = age + 5

#conditional if/ else

if age < 18:
    print("Keep learning you've got a bright future")
else:
    print("Never stop growing and exploring")

print(f"\nNice to meet you, {name}!")
print(f"Wow, you love {subject}! That's awesome")
print(f"In 5 years you will be {future_age} years old🎉🎉🎁")

"""

# PROJECT  3 : PASSWORD VALIDATOR

import re
import hashlib
from datetime import datetime

def password_rules(password):
    """" Rules a list of failed rules (empty list => valid)"""
    fails = []
    if len(password) < 8:
        fails.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        fails.append("Password must include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        fails.append("Password must include at least one lowercase letter.")
    if not re.search(r"\d", password):
        fails.append("Password must include at least one digit.")
    if not re.search(r"[!@#$%^&*]", password):
        fails.append("Password must include at least one special character.")
    return fails

def hash_password(password):
    """"Return a sha256 hex digest of password (not salt for simplicity)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def save_user(username, hashed_pw):
    now = datetime.now().isoformat()
    line = f"{username}: {hashed_pw}: {now}\n"
    with open("users.text", "a", encoding = "utf-8") as f:
        f.write(line)


def main():
    print("===Create your account ===")
    username = input("Enter username: ").strip()
    attempts = 3
    while attempts > 0:
        pwd = input("Create password: ")
        confirm = input("Confirm password: ")
        if pwd != confirm:
            print("Password do not much. Try again.")
            attempts -=1
            continue
    
        failed = password_rules(pwd)
        if failed:
            print("Password invalid for the following reasons:")
            for reason in failed:
                print("-", reason)
            attempts -=1
            print(f"You have {attempts} attempts left.\n")
            continue

        # success
        hashed = hash_password(pwd)
        save_user(username, hashed)
        print(f"Account created successfully for {username} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    else:
        # runs if while loop finished without break
        print("Too many failed attempts. Please try again later.")

if __name__ == "__main__":
    main()