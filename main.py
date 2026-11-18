
import string
from getpass import getpass


def check_password(password):
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Uppercase letters": any(c.isupper() for c in password),
        "Lowercase letters": any(c.islower() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Special characters": any(c in string.punctuation for c in password)
    }

    common_passwords = {
        "password",
        "password123",
        "qwerty123",
        "12345678",
        "admin123"
    }

    score = sum(checks.values())

    if password.lower() in common_passwords:
        strength = "WEAK"
    elif score == 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return checks, strength


def main():
    print("=== Password Strength Checker ===")

    password = getpass("Enter a test password: ")

    checks, strength = check_password(password)

    print("\nPassword Analysis:")

    for name, passed in checks.items():
        status = "Yes" if passed else "No"
        print(f"{name}: {status}")

    print(f"\nPassword Strength: {strength}")


if __name__ == "__main__":
    main()
