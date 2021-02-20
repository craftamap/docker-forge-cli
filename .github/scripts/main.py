import requests
import os

stream = os.popen("git describe --abbrev=0 --tags")
latest_tag = stream.read().strip("\n")

response = requests.get("https://registry.npmjs.com/@forge/cli/")

timeseries: dict = response.json()["time"]

idx = list(timeseries.keys()).index(latest_tag)
new_list = list(timeseries.keys())[idx + 1 :]


for version in new_list:
    print("creating empty commit for version", version)
    os.popen(f'git commit --allow-empty -m "v{version}"')
    print("creating tag for version", version)
    os.popen(f'git tag -a {version} -m "v{version}"')
    print("pushing tag for version", version)
    os.popen(f"git push origin {version}")
