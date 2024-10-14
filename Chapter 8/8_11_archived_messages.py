def show_messages(printed_messages):
    """Print all messages in the list"""
    print("Showing all the messages:")
    for printed_message in printed_messages:
        print(printed_message.title())


def send_messages(unprinted_messages, printed_messages):
    """Print each message, and then move it to sednd_messages"""
    print("\nSending all messages:")
    while unprinted_messages:
        current_message = unprinted_messages.pop()
        print(current_message.title())
        printed_messages.append(current_message)


unprinted_messages = ["welcome", "bienvenutto", "bem-vindo", "willkommen"]
show_messages(unprinted_messages)

printed_messages = []
send_messages(unprinted_messages[:], printed_messages)

print("\nFinal lists:")
print(unprinted_messages)
print(printed_messages)
