import requests
from urllib.parse import urlparse

rs = requests.get('https://raw.githubusercontent.com/tenzindorji/randomurl/refs/heads/main/random_urls_1000.txt')

url_string = rs.text

famousurls = {}

for url in url_string.splitlines():
    domain = urlparse(url).netloc
    famousurls[domain] = famousurls.get(domain, 0) + 1
print(famousurls)

print(max(famousurls, key=famousurls.get))

logs = [
    "ERROR 500 Database timeout",
    "ERROR 404 Page not found",
    "ERROR 500 Connection reset",
    "ERROR 503 Service unavailable"
]

freq = {}

for err in logs:
    freq[err.split()[1]] = freq.get(err.split()[1], 0) + 1

print(freq)

#max_error = max(freq, key=lambda x: x[1])
max_error = max(freq, key=freq.get)
print(f"max error code is {max_error} and has occurred {freq[max_error]} times")



logs = [
    "192.168.1.10 GET /home",
    "10.0.0.5 GET /login",
    "192.168.1.10 POST /order"
]


freq = {}

for log in logs:
    ip=log.split()[0]
    freq[ip] = freq.get(ip, 0) + 1
print(max(freq, key=freq.get))


#active users

logs = [
    "user=tenzin action=login",
    "user=john action=view",
    "user=tenzin action=checkout"
]


freq = {}

for log in logs:
    user = log.split("=")[1].split()[0]
    #print(user)
    freq[user] = freq.get(user, 0) + 1

print(max(freq, key=freq.get))


logs = [
    "GET /api/users",
    "GET /api/orders",
    "GET /api/users",
    "POST /api/login"
]

freq = {}

for log in logs:
    api = log.split("/")[-1]
    freq[api] = freq.get(api, 0) + 1
print(freq)


orders = [
    {"product": "iphone"},
    {"product": "ipad"},
    {"product": "iphone"}
]

freq= {}

for order in orders:
    product = order["product"]
    freq[product] = freq.get(product, 0) + 1
print(freq)


text = "python is great and python is easy"

freq = {}

for i in text.split():
    freq[i] = freq.get(i, 0) + 1

print(freq)


pods = [
    ("prod", 2),
    ("dev", 1),
    ("prod", 3),
    ("qa", 2),
    ("dev", 2)
]



freq = {}

for k, v in pods:
    freq[k] = freq.get(k, 0) + v

print(freq)




events = [

    ("payment", "ERROR"),
    ("payment", "ERROR"),
    ("auth", "WARN"),
    ("auth", "ERROR"),
    ("search", "WARN")
]


freq = {}

for service, error in events:
    freq.setdefault(service, {}) 
    freq[service][error] = freq[service].get(error, 0) + 1
print(freq)