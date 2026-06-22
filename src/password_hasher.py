import bcrypt

password = input("Enter a password to hash: ")

hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print("\nGenerated Hash:")
print(hashed_password.decode())

login_password = input("\nEnter password again for verification: ")

if bcrypt.checkpw(
        login_password.encode(),
        hashed_password):
    print("Password verified successfully.")
else:
    print("Incorrect password.")