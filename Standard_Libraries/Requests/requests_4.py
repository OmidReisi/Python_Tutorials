import requests

# authentication are done either with forms or with basic-auth

# here we're setting a basic-auth system where username = omid, password = 1234
# now if the auth argument (username and password are passed as a tuple) matches our username and passowrd we get our response
r = requests.get(url=r"https://httpbin.org/basic-auth/omid/1234", auth=("omid", "1234"))

# if the response code is 401 that means unauthorized response code and are creditionals are wrong
print(r)


# by default requests don't have a timeout and wait indefinitely for a response
# you can test delayed response in httpbin.org as well with https://httpbin.org/delay/{seconds to delay}
# in order to add a timeout to our request we add the timeout argument in seconds

# here the url delays the response for 5 seconds but our timeout is 3 seconds
# if timeout is hit(response doesn't come before timeout) then a requests.exceptions.ReadTimeout exception is raised
r = requests.get(url=r"https://httpbin.org/delay/5", timeout=3)

print(r)
