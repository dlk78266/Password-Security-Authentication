# Password Security and Authentication Mechanisms

## Introduction

Passwords are one of the most commonly used methods for authenticating users in computer systems and online services. Weak passwords can be easily guessed, stolen, or cracked by attackers, leading to unauthorized access and data breaches.

This report explores common password attacks, explains the differences between hashing and encryption, compares weak and strong passwords, and discusses best practices for securing user accounts. A Python script using the bcrypt library is also implemented to demonstrate secure password hashing and password verification.

## Common Password Attacks

### 1. Brute Force Attack

A brute force attack involves trying every possible combination of characters until the correct password is found. Although this method guarantees success eventually, it becomes time-consuming when strong and lengthy passwords are used.

Example passwords vulnerable to brute force attacks:

```text
1234
abcd
pass
```

---

### 2. Dictionary Attack

In a dictionary attack, attackers use a predefined list of commonly used passwords and words to guess user credentials. This method is much faster than brute force because it focuses only on likely passwords.

Examples:

```text
password
welcome123
admin
qwerty
```

---

### 3. Credential Stuffing

Credential stuffing occurs when attackers use usernames and passwords obtained from previous data breaches to gain access to accounts on other websites. This attack is successful because many users reuse the same password across multiple services.

## Hashing vs Encryption

Hashing and encryption are both cryptographic techniques, but they serve different purposes.

| Feature | Hashing | Encryption |
|---------|---------|------------|
| Purpose | Verify data integrity | Protect confidentiality |
| Reversible | No | Yes |
| Secret Key Required | No | Yes |
| Used for Password Storage | Yes | No |
| Examples | bcrypt, SHA-256 | AES, RSA |

### Why Hashing is Preferred for Password Storage

Passwords should not be stored in plain text because anyone who gains access to the database can read them. Encryption is also not ideal because encrypted passwords can be decrypted using a key.

Hashing algorithms such as bcrypt generate a fixed-length output that cannot be reversed to obtain the original password. Bcrypt also adds a unique salt to each password, making attacks like rainbow tables ineffective.

## Weak vs Strong Password Comparison Matrix

| Weak Password Characteristics | Strong Password Characteristics |
|------------------------------|---------------------------------|
| Less than 8 characters | At least 12 characters |
| Uses common words | Uses random combinations |
| Contains only letters | Includes uppercase, lowercase, numbers, and symbols |
| Easy to guess | Difficult to predict |
| Reused across websites | Unique for every account |

### Examples

| Weak Password | Strong Password |
|--------------|----------------|
| password | T9#kLm@4Qx!2 |
| admin123 | G7$pR8!mN2@z |
| qwerty | X1^aP9@tL3#s |
| 123456 | H8*eR2!vW7@m |

## Security Recommendations

To improve password security and protect user accounts, the following practices should be followed:

- Use passwords that are at least 12 characters long.
- Combine uppercase letters, lowercase letters, numbers, and special symbols.
- Avoid using personal information such as names, birthdays, or phone numbers.
- Do not reuse passwords across multiple websites or applications.
- Enable Multi-Factor Authentication (MFA) whenever possible.
- Store passwords using secure hashing algorithms such as bcrypt instead of plain text or reversible encryption.
- Use password managers to generate and store complex passwords securely.
- Regularly update passwords, especially after a suspected data breach.

## Conclusion

Password security plays a vital role in protecting digital systems and user information. Weak passwords and poor storage practices make systems vulnerable to attacks such as brute force, dictionary attacks, and credential stuffing. Using strong passwords, secure hashing techniques like bcrypt, and additional protections such as multi-factor authentication significantly reduces security risks. The implemented Python script demonstrates how bcrypt can securely hash and verify passwords, providing a practical example of modern authentication practices.