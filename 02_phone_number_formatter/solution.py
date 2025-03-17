# do not change the method name
def main():
    # your solution goes here
    phone_number = input(
        "Enter a 10-digit phone number (no spaces, special characters, or letters): ")

    phone_number.isdigit() and len(phone_number) == 10 or (print(
        "Error: Please enter exactly 10 digits.\nNo spaces, special characters and alphabetical characters."), exit())

    area_code = phone_number[:3]
    first_part = phone_number[3:6]
    last_part = phone_number[6:]

    formatted_number = f"({area_code}) {first_part}-{last_part}"

    print(f"Formatted Phone Number: {formatted_number}")


# do not change the code below
if __name__ == "__main__":
    main()
