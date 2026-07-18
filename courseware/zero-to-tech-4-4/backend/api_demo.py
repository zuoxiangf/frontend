import requests

resp = requests.get("https://api6.ipify.org/?format=json")
print(resp.json())

a =(1,2,3);

a[0] = 3;
print(a);