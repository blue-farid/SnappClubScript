import requests

url = "https://snappclub.snapp.ir/api/v1/user/voucher/redeem"

# You should add your JWT token here in 'Authorization' header.

headers = {
    "Sec-Ch-Ua": '"Chromium";v="119", "NotA_Brand";v="24"',
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Locale": "fa-IR",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/119.0.6045.159 Safari/537.36"),
    "Content-Type": "application/json",
    "App-Version": "snapp club",
    "Accept": "*/*",
    "Origin": "https://snappclub.snapp.ir",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Authorization": "",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://snappclub.snapp.ir/reward/details/4076",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

# You May change the product_id.

payload = {"product_id": 4076}

def send_requests(url, headers, payload, count):
    for i in range(count):
        # Send the POST request
        response = requests.post(url, json=payload, headers=headers)
        # Check if we want to print out the status (can be commented out if not needed)
        print(f"Request {i+1}/{count}: Status Code {response.status_code}")

# You May change the count.

send_requests(url, headers, payload, 100)

