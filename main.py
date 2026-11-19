from oyster_num_finder import OysterNumFinder

oyster_num_finder = OysterNumFinder()

finished = False

while finished == False:

    digits = input("Enter the 10-digit Oyster code from your receipt: ")

    if digits.isdigit() and len(digits) == 10:
        print(digits)
        print(f"Your Oyster card number is:"
            f"{digits} {oyster_num_finder.checksum(digits):02d}") 
    else:
        print("Invalid input")

    new_code = input("Do you have another code you would like to submit? Yes or no: ")
    if new_code.lower() in ("yes", "y"):
        print("Feel free to try again")
    else:
        print("Thank you for using this service.")
        break
