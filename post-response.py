import requests
import base64

payload = {
    "github_url": "",
    "contact_email": "your_email_here",
    "solution_language": "python"
}

email = "your_email_here"
totp = "0298980727" # don't forget to always replace this brah

# Authorization header
auth_value = f"{email}:{totp}"
auth_header = base64.b64encode(auth_value.encode()).decode() # ty stack overflow fr fr

# POST request
url = "post_url"
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json"
}

# via https://www.w3schools.com/python/ref_requests_response.asp
response = requests.post(url, json=payload, headers=headers) # cuz post() returns response object -> ty doc

# Check the response status
if response.status_code == 200:
    print("Request successful:", response.json()) # since response is in JSON i think
else:
    print("Error:", response.status_code, response.text)
