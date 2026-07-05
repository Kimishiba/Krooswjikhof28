import urllib.request
import json

url = "http://192.168.1.41:8123/api/config"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNjhiMmQwODJhZTQ0NzYzOTJmZGNjNDY2OTgwOThjMiIsImlhdCI6MTc4MjY3MzM4OCwiZXhwIjoyMDk4MDMzMzg4fQ.tpfps7BgZyoKiaKF9AqRdoRVEODkR9LhLCeCF1ElAlM"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(json.dumps(json.loads(html), indent=2))
except Exception as e:
    print(f"Error: {e}")
