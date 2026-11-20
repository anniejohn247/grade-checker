# St Andrews MMS Grade Checker

A lightweight Python program that monitors the University of St Andrews' MMS (Module Management System) for newly uploaded grades.

When a new grade is detected, the program sends a **Windows desktop notification** to let you know that your results are available, so you don't have to keep checking MMS manually.

## Getting Started

### 1. Set Up Authentication

Run the following command to create your authentication JSON file:

```bash
python ./save_details.py
```

Follow the prompts to enter your login details. This file stores the authentication information needed to access MMS.

### 2. Start the Grade Checker

Run the following command:

```bash
python ./src/grade_checker.py
```

Allow the program to continue running in the terminal. It will periodically check MMS for newly uploaded grades.

### 3. Receive Notifications

When a new grade is uploaded to MMS, you will receive a Windows desktop notification.

**Keep the program running** to ensure that you are notified when new grades become available.

## Requirements

- Python installed on your Windows machine.
- Access to the University of St Andrews MMS.
- A working internet connection.

## Disclaimer

This is an unofficial student-made tool and is not affiliated with or endorsed by the University of St Andrews.
