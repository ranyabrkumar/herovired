# Python Assignment

## Q1: Password Strength Checker

### Task:
Create a Python script to check the strength of a password based on the following criteria:
- Minimum length: At least 8 characters.
- Contains both uppercase and lowercase letters.
- Contains at least one digit (0-9).
- Contains at least one special character (e.g., `!`, `@`, `#`, `$`, `%`).

### Requirements:
- Implement a function `check_password_strength(password: str) -> bool`.
- Take user input for the password and validate it using the function.
- Provide feedback to the user about the password's strength.

---

## Q2: CPU Health Monitoring

### Task:
Write a Python program to monitor the CPU usage of the local machine.

### Requirements:
- Continuously monitor CPU usage.
- Display an alert if CPU usage exceeds a predefined threshold (e.g., 80%).
- Run indefinitely until interrupted.
- Include error handling for exceptions.

### Hint:
- Use the `psutil` library (`pip install psutil`).
- Use `psutil.cpu_percent()` to get the CPU usage percentage.

### Expected Output:
```
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
...
```

---

## Q3: Configuration File Parser

### Task:
Automate configuration management by parsing a configuration file.

### Requirements:
- Read a configuration file (sample provided below).
- Extract key-value pairs and store them in a data structure (e.g., dictionary).
- Handle errors if the file is not found or cannot be read.
- Save the extracted data as JSON in a database.
- Create a GET request to fetch the stored information.

### Sample Configuration File:
```
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

### Sample Output:
```
Configuration File Parser Results:
Database:
- host: localhost
- port: 3306
- username: admin
- password: secret

Server:
- address: 192.168.0.1
- port: 8080
```

---

## Q4: Backup Script

### Task:
Implement a Python script `backup.py` to back up files from a source directory to a destination directory.

### Requirements:
- Copy all files from the source directory to the destination directory.
- Append a timestamp to file names in the destination directory if a file with the same name already exists.
- Handle errors if the source or destination directory does not exist.

### Sample Command:
```bash
python backup.py /path/to/source /path/to/destination
```

---

## Submission Instructions:
1. Complete all tasks.
2. Push your code to a GitHub repository.
3. Share the repository link in a text, Word, or PDF file.
4. Submit the file containing the repository link via Vlearn.
