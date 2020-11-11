import os
import sys
import requests

print(os.getcwd())
sys.path.append(os.getcwd())
import amesh

if __name__ == "__main__":
    url = "https://slack.com/api/files.upload"
    b = amesh.get_entry().to_bytes()
    token = os.getenv("SLACK_BOT_TOKEN")
    data = {
        "token": token,
        "channels": "otiai10-dev",
    }
    files = {'file': ('amesh.png', b, 'image/png')}
    res = requests.post(url, data=data, files=files)
    print(res.status_code)
    print(res.content)
