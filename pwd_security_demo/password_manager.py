import re
import hashlib
import secrets
import getpass

# Password Minimum Criteria:
def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        issues.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Add at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        issues.append("Add at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Add at least one special character.")

    if not issues:
        return True, "Strong password!"
    return False, issues

# Password Hashing and Verification:
def hash_password(password):
    salt = secrets.token_hex(16)  # random salt, unique per password
    pw_salt = (password + salt).encode('utf-8')
    hashed = hashlib.sha256(pw_salt).hexdigest()
    return hashed, salt

def verify_password(stored_hash, stored_salt, password_attempt):
    attempt_hash = hashlib.sha256((password_attempt + stored_salt).encode('utf-8')).hexdigest()
    return attempt_hash == stored_hash

# Storage for demonstration purposes:
user_db = {}

def register_user():
    username = input("Choose a username: ")
    password = getpass.getpass("Choose a password: ")  # hides input while typing

    strong, result = check_password_strength(password)
    if not strong:
        print("Password too weak. Issues found:")
        for issue in result:
            print(" -", issue)
        return

    hashed, salt = hash_password(password)
    user_db[username] = {"hash": hashed, "salt": salt}
    print(f"User '{username}' registered successfully.")
    print(f"(Stored hash: {hashed[:20]}... — the real password is never stored)")

def login_user():
    username = input("Username: ")
    password_attempt = getpass.getpass("Password: ")

    if username not in user_db:
        print("User not found.")
        return

    record = user_db[username]
    if verify_password(record["hash"], record["salt"], password_attempt):
        print("Login successful!")
    else:
        print("Incorrect password.")

# User Interface:
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        break
    else:
        print("Invalid option.")