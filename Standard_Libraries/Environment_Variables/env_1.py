import os

# store your environment variables in your user section of windows environment variables and then use the os.environ method which returns a dictionary to get them
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)
