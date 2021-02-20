import requests
import os

print("=== START ===")

stream = os.popen("git describe --abbrev=0 --tags")
latest_tag = stream.read().strip("\n")
print("found latest tag", latest_tag)

print("fetching time series from npm")
response = requests.get("https://registry.npmjs.com/@forge/cli/")
print("fetched time series from npm")

timeseries: dict = response.json()["time"]

timeseries_keys = list(timeseries.keys())

print(f"found {len(timeseries_keys)} timeseries")

idx = timeseries_keys.index(latest_tag)
newer_versions = timeseries_keys[idx + 1 :]

print("found the following, newer versions:", newer_versions)

for version in newer_versions:
    print("creating empty commit for version", version)
    os.popen(f'git commit --allow-empty -m "v{version}"')
    print("creating tag for version", version)
    os.popen(f'git tag -a {version} -m "v{version}"')
    print("pushing tag for version", version)
    os.popen(f"git push origin {version}")

print("pushed tags, now pushing commits")
os.popen(f"git push")

print("=== DONE ===")
