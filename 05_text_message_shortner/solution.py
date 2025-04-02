# do not change the method name
def main():
    message = input("Enter a message: ")

    replacements = {
        " with ": " w/ ",
        " for ": " 4 ",
        " to ": " 2 ",
        " and ": " & ",
        " at ": " @ "
    }

    original_message = message

    original_length = len(message)

    for word, abbreviation in replacements.items():
        message = message.replace(word, abbreviation)

    message = message[0].upper() + message[1:] if message else ""

    if len(message) > 160:
        message = message[:157] + "..."

    shortened_length = len(message)

    print(f"Original message ({original_length} chars): {original_message}")
    print(f"Shortened message ({shortened_length} chars): {message}")
    print(f"You saved {original_length - shortened_length} characters!")
    
# do not change the following lines:
main()
