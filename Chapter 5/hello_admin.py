usernames = ["dgeichert", "geisa84", "admin", "daidruida", "vilmalopes"]

for username in usernames:
    if username != "admin":
        print("\nHello " + username + ", thank you for loggin in again.")
    else:
        print("\nHello admin, would you like to see a status report?")
