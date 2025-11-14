text = input("Enter a string: ")

# Remove spaces and convert to lowercase
cleaned = text.replace(" ", "").lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")
