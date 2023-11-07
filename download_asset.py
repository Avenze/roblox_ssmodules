import re
import requests
import os

# function to check if the asset still exists on the library
def check_url_exists(url, not_found_string="User is not authorized to access Asset"):
    response = requests.get(url)
    return not re.search(not_found_string, response.text)

#def check_url_exists(url):
#    response = requests.get(url)
#    return response.status_code != 404

# create or check if the download folder exists
download_folder = "download"
os.makedirs(download_folder, exist_ok=True)

# open the check_success.txt file, to write the existing assets
with open("check_success.txt", "w") as found_file:

    # read all input assets from the check.txt file lol
    with open("check.txt", "r") as file:
        for line in file:

            # regex comes in clutch yet again, extract the asset id from the entire line
            match = re.search(r'require\((\d+)\)', line)

            if match:
                extracted_number = match.group(1)
                url = f'https://assetdelivery.roblox.com/v1/asset/?id={extracted_number}'

                # pass the asset id to the function defined above
                if check_url_exists(url):
                    print(f"{extracted_number} | Found valid existing module on the Roblox Library!")
                    found_file.write(line)

                    # download it from the assetdelivery.roblox.com endpoint and change it's file extension to .rbxm (don't want no 7f828e97f3809823ed04196b2bf66dbb)
                    response = requests.get(url)
                    file_path = os.path.join(download_folder, f'{extracted_number}.rbxm')
                    with open(file_path, 'wb') as asset_file:
                        asset_file.write(response.content)
                    print(f"Downloaded file for ID {extracted_number} to {file_path}")