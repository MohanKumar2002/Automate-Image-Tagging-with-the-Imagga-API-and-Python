import requests
import json
from pathlib import Path

# Specify the path to the image file on your desktop
image_path = Path("d:\Python Projects\AI Cloud\images.jpg").expanduser()

url = "https://api.imagga.com/v2/tags"

files = {'image': open(image_path, 'rb')}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2FhYzE1YWM3OGU2ZDhiOTpiMTE4NzJlZjAxZTM4ODhkZDZhZGUxMzYzOTFhM2IxNg=="
}

response = requests.request("POST", url, headers=headers, files=files)
data = json.loads(response.text.encode("ascii"))

for i in range(10):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)