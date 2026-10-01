# Secret Password 

attempts = 0

while True:
    password = input("Enter the secret password: ")
    
    if password == "python123":
        print("Access granted.")
        break  # Exit the loop immediately on success
        
    attempts += 1
    
    if attempts == 3:
        print("Account locked. Try again later.")
        break  # Exit the loop after 3 failed attempts
    else:
        print("Incorrect password. Try again.")
