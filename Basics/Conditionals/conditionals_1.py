if True:
    print("Conditional was True")

if False:
    # does not print line below
    print("Conditional was False")

language = "Python"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")


user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")


# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example: "", (), [].
#     Any empty mapping. For example: {}.
