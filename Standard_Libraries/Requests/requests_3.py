import requests

# httpbin.org is website that allows us to see responses from the different requests we make with different url arguments
# this website returns respones as json objects
payload = {"page": 2, "count": 25}

# you can pass the arguments for your url directly in the url but requests module allows us to pass them as a dictionary as params argument and reassembels them in url automatically
r = requests.get(url=r"https://httpbin.org/get", params=payload)

# returns the url we sent the request to
print(r.url)

print(r.text)

data = {"username": "Omid79.dg", "password": "o_r1234"}

# this is how we post something to our url (http Post method) and data is the dictionary of data we send
r = requests.post(url=r"https://httpbin.org/post", data=data)

# if the response is a json object you can use this method instead (returns a dictionary)
r_dict = r.json()

print(r_dict.get("form"))


# you can use http put method with requests just like other methods with requests.put()
