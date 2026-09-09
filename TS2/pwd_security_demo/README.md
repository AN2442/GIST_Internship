# Secure Password Management Demo

## What this project does
This is a command-line Python program that demonstrates secure password handling practices, built as part of a cybersecurity internship task.

## Security principles demonstrated
- **Password strength validation**: rejects passwords that are too short or missing uppercase letters, lowercase letters, numbers, or special characters.
- **Hashing**: passwords are never stored in plain text. Instead, SHA-256 hashing is used to convert the password into a fixed-length, irreversible value.
- **Salting**: a random, unique salt is generated per user (using Python's `secrets` module) and combined with the password before hashing. This prevents attackers from using precomputed "rainbow table" attacks and ensures two users with the same password get different stored hashes.
- **Secure input**: the `getpass` module hides password input on screen while typing.
- **Authentication**: login works by re-hashing the entered password with the stored salt and comparing it to the stored hash.

## Technologies used
- Python 3
- Standard libraries: `hashlib`, `secrets`, `re`, `getpass`

## How to run
1. Install Python 3.
2. Run `python password_manager.py`
3. Choose Register or Login from the menu.

## What I learned
I learned why storing plain text passwords are dangerous, how salting protects against rainbow table attacks as well as how to validate password strength.
