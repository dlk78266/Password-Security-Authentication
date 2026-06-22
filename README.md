# Password Security and Authentication Mechanisms

## Project Overview

This project demonstrates the importance of password security and modern authentication mechanisms. It explains common password attacks, compares hashing and encryption techniques, and provides a Python implementation for securely hashing and verifying passwords using the bcrypt library.

## Features

- Research on common password attacks
- Comparison between hashing and encryption
- Weak vs strong password analysis
- Secure password hashing using bcrypt
- Password verification demonstration
- Testing evidence included

## Project Structure

```
Password-Security-Authentication/

README.md

requirements.txt

docs/
    REPORT.md

src/
    password_hasher.py

assets/
    demo_output.txt
```

## Prerequisites

- Python 3.x
- pip package manager

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Running the Script

Execute the following command from the project directory:

```bash
python src/password_hasher.py
```

## Example Output

```text
Enter a password to hash: Cyber123!

Generated Hash:
$2b$12$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Enter password again for verification: Cyber123!

Password verified successfully.
```

Additional testing results are available in:

```
assets/demo_output.txt
```

## Author

Dondapati Likhith Kumar
B.Tech Cyber Security
Pragati Engineering College