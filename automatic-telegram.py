
import uuid
import ipaddress
import random
import requests
from selenium import webdriver

def generate_non_us_browser_id_with_ipv4():
    while True:
        # Generate a random UUID (Universally Unique Identifier)
        browser_id = str(uuid.uuid4())

        # Generate a random IPv4 address
        ipv4_address = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

        # Make the API request for geolocation using the extracted IPv4 address
        response = requests.post("http://ip-api.com/batch", json=[{"query": ipv4_address}]).json()

        # Check if the country code is not in the United States
        if response[0].get('countryCode', '') != 'US':
            # Return the combination of UUID and non-US IPv4 address
            return f"{browser_id}_{ipv4_address}"

# Generate a random UUID with non-US IPv4 address
random_non_us_browser_id_with_ipv4 = generate_non_us_browser_id_with_ipv4()

# Extract UUID and IPv4 parts
uuid_part, ipv4_part = random_non_us_browser_id_with_ipv4.split('_')

# Use the extracted values
print("Generated UUID:", uuid_part)
print("Generated Non-US IPv4 Address:", ipv4_part)

# Make the API request for geolocation using the extracted IPv4 address
response = requests.post("http://ip-api.com/batch", json=[{"query": ipv4_part}]).json()

# Print the geolocation information
for ip_info in response:
    for k, v in ip_info.items():
        print(k, v)
    print('\n')

# choose between Firefox or Chrome
# Create a new instance of the Firefox driver in headless mode
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

'''
# Create a new instance of the Chrome driver in headless mode
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
'''

# Navigate to a website (your target URL goes here)
driver.get("https://INSERT-TARGET-URL")

# List of cookies to delete
# Adjust as needed
cookies_to_delete = ['browserId', 'countryCode', 'sessionId']

# Iterate over cookies and delete if they exist
for cookie_name in cookies_to_delete:
    if cookie_name in [cookies['name'] for cookies in driver.get_cookies()]:
        driver.delete_cookie(cookie_name)

# Add the generated UUID as 'browserId' cookie
driver.add_cookie({'name': 'browserId', 'value': uuid_part})

# Extract the country code from the geolocation information
# Here, I assume that 'countryCode' is available in the 'country' field of the first IP info in the response
country_code = response[0].get('countryCode', 'Unknown')

# Add the extracted country code as 'countryCode' cookie
driver.add_cookie({'name': 'countryCode', 'value': country_code})

# Perform other actions if needed

# Close the browser window
#driver.quit()
# Driver.quit() is commented out for verification purposes so you can open dev tools and inspect.  Also note that headless really only works with Chrome as firefox still opens a browser_window.  Have not figured out how to resolve it 
# this script can be modified for user-case specifics. Don't do anythong illegal. For Educational and testing purposes.
