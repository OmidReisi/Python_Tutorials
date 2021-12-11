import os

# this module allows us to work with .env files
from dotenv import load_dotenv

# this method adds the environment variables from a .env file to the os.environ dictionary
# this method look for the file in CWD and works it's way up to the parent directory till it reaches the root directory
# you can pass an explicit path to a .env file as well if you want to.
load_dotenv(r"./.env")

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)


print()

for item in os.environ:
    print(item)
