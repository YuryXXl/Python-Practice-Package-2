import sys
# do not change the method name
def main():
    encoded_message = input("Enter the encoded message: ")
    
    step = input("Enter the step size: ")

    if not step.isdigit() or int(step) <= 0:
        print("Error: Step size must be a positive integer")
        sys.exit(1)
    step = int(step)
    decoded_message = encoded_message[::step]
    
    print(f"Decoded Message: {decoded_message}")

# do not change the following lines:    
if __name__ == "__main__":
    main()