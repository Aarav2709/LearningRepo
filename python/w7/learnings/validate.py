import re  # Import the Regular Expressions Library.

email = input("Enter your email: ")  # Ask the user to enter the email.

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Congrats! The email is valid.") # Complicated. Images provided.
else:
  print("The email is invalid.") # Ez pez.``
