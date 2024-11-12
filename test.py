import requests
import datetime


PROXY_ADDRESS = "5.59.251.170"
PROXY_PORT = 6209
PROXY_USERNAME = "dmrandiq"
PROXY_PASS = "ue66hhh99bgk"

# Define your proxy settings
proxies = {
    "http": f"http://{PROXY_USERNAME}:{PROXY_PASS}@{PROXY_ADDRESS}:{PROXY_PORT}",
    "https": f"http://{PROXY_USERNAME}:{PROXY_PASS}@{PROXY_ADDRESS}:{PROXY_PORT}"
}

# print(f"http://{PROXY_USERNAME}:{PROXY_PASS}@{PROXY_ADDRESS}:{PROXY_PORT}")

# Make a request with proxy

# Example: GET request to httpbin.org
# response = requests.get('https://ipv4.icanhazip.com', proxies=proxies)

# Check the response
# print(response.text)
# This should print the IP address that the server sees, which should be the proxy IP if everything is set up correctly.

current_time = datetime.datetime.now()

print(current_time)