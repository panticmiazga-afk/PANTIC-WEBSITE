# password_validator.py
import re
import hashlib
from datetime import datetime

def password_rules(password):
    """Return a list of failed rules (empty list => valid)."""
    fails = []
    if len(password) < 8:
        fails.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        fails.append("Password must include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        fails.append("Password must include at least one lowercase letter.")
    if not re.search(r"\d", password):
        fails.append("Password must include at least one digit.")
    if not re.search(r"[!@#$%^&*()_\-+=\[\]{};:,.<>?/\\|`~]", password):
        fails.append("Password must include at least one special character.")
    return fails

def hash_password(password):
    """Return a sha256 hex digest of password (not salt for simplicity)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def save_user(username, hashed_pw):
    now = datetime.now().isoformat()
    line = f"{username}:{hashed_pw}:{now}\n"
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(line)

def main():
    print("=== Create your account ===")
    username = input("Enter username: ").strip()
    attempts = 3
    while attempts > 0:
        pwd = input("Create password: ")
        confirm = input("Confirm password: ")
        if pwd != confirm:
            print("Passwords do not match. Try again.")
            attempts -= 1
            continue

        failed = password_rules(pwd)
        if failed:
            print("Password invalid for the following reasons:")
            for reason in failed:
                print("-", reason)
            attempts -= 1
            print(f"You have {attempts} attempts left.\n")
            continue

        # success
        hashed = hash_password(pwd)
        save_user(username, hashed)
        print(f"Account created successfully for {username} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        break
    else:
        # runs if while loop finished without break
        print("Too many failed attempts. Please try again later.")

if __name__ == "__main__":
    main()



