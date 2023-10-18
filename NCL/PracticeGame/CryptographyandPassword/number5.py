
import requests
from bs4 import BeautifulSoup
import hashlib

# Function to get a list of TV show titles
def get_tv_show_titles():
    url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [element.get_text() for element in soup.find_all("td", class_="titleColumn")]
    return titles

# Define the password hash you want to crack
hash_to_crack = input("Enter the password hash you want to crack: ").lower()

# Function to check if a password is correct
def is_password_correct(password, hash_to_match):
    hashed = hashlib.md5(password.encode()).hexdigest()  # Use the appropriate hashing algorithm
    return hashed == hash_to_match

# Get a list of TV show titles
tv_show_titles = get_tv_show_titles()

# Brute force the passwords
for password in tv_show_titles:
    if is_password_correct(password, hash_to_crack):
        print(f"Password cracked: {password} (Hash: {hash_to_crack})")

