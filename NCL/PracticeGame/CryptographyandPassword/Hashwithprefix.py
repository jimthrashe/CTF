import hashlib #hashlib is goated btw

# Define the known prefix
prefix = "SKY-ICYY-"

# Define the password hash you want to crack
target_hash = input("")

# Function to check if a password is correct
def is_password_correct(password):
    # Hash the password using the same method as the target hash
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed == target_hash

# Brute force the passwords
for i in range(10000):  # Try all 4-digit combinations
    password_attempt = f"{prefix}{i:04d}"
    if is_password_correct(password_attempt):
        print(f"Password cracked: {password_attempt}")
        break

