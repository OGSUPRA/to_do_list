import requests

r = requests.get("https://requests.readthedocs.io/en/latest/index.html")

print(r.status_code)
