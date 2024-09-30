usernames = []

if usernames:
    for username in usernames:
        print("\nHello admin, would you like to see a status report?")
    else:
        print("\nHello " + username + ", thank you for loggin in again.")
else:
    print("We need to find some users!")
