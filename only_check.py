import re
import requests

# Function to check if a URL exists
def check_url_exists(url):
    response = requests.get(url)
    return response.status_code != 404

# Read input from the file "check.txt"
with open("check.txt", "r") as file:
    for line in file:
        # Use a regular expression to extract the numbers between require() function
        match = re.search(r'require\((\d+)\)', line)

        if match:
            extracted_number = match.group(1)
            url = f'https://create.roblox.com/marketplace/asset/{extracted_number}'

            # Check if the URL exists
            if check_url_exists(url):
                print(f"{extracted_number} | Found valid existing module on the Roblox Library!")