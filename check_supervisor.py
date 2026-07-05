import urllib.request
import json

endpoints = [
    "http://192.168.1.41:8123/api/hassio/addons",
    "http://192.168.1.41:8123/api/hassio/info",
    "http://192.168.1.41:8123/api/hassio/supervisor/ping"
]

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5MTdiOTFkMTAzZTE0NmQ1YWIyZTg3YjFlMzkyNjUzYyIsImlhdCI6MTc4MzA3MjMwMSwiZXhwIjoyMDk4NDMyMzAxfQ.mDqgAQM6NYX0KcvrDOekXCpWAYN0-LJYgbGvt9Tlhxg",
    "Content-Type": "application/json"
}

for url in endpoints:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(f"Success for {url}:")
            print(html[:200])
    except Exception as e:
        print(f"Error for {url}: {e}")
