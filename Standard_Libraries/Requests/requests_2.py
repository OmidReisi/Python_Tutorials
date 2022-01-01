import requests

r = requests.get(url=r"https://xkcd.com/353/")

# returns the status code of the response:
# 200's are success
# 300's are redirects
# 400's are client errors (like if you try accessing something you don't have permission to)
# 500's are server errors
print(r.status_code)

# returns true for status_code less than 400
print(r.ok)

# returns a dictionry of headers attached to response
print(r.headers)

