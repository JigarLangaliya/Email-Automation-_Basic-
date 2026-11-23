# Birthday Email Automation

A Python project that checks whether a date recorded in a CSV file matches today's month and day. If a match is found, it loads an email letter template, replaces the `[NAME]` placeholder with the recipient's name, and sends the personalized message through Gmail using SMTP.

## How It Works

The program follows these steps:

1. Gets the current date from the computer.
2. Reads date records from `data.csv` using **Pandas**.
3. Builds a dictionary using the recorded month and day as the key.
4. Checks whether today's month and day match a date in the CSV file.
5. If a matching date is found:
   - Reads `letter_templates/letter_1.txt`.
   - Replaces `[NAME]` with the birthday person's name.
   - Connects to Gmail's SMTP server.
   - Sends the personalized email to the recipient.
6. If there is no matching date, it prints `Not today.`

## Project Structure

The project expects the following files and folders:

```text
birthday-email-automation/
│
├── main.py
├── data.csv
│
└── letter_templates/
    └── letter_1.txt
```

`letter_templates/letter_1.txt` is referenced by the Python program but was not included in the supplied files. Create this folder and template file before running the project.

## Requirements

- Python 3
- Pandas
- A Gmail account configured to allow SMTP access

Install the required Python package:

```bash
pip install pandas
```

## CSV Format

The supplied `data.csv` has these column headings:

```csv
name,email(receiver's email),year,month,day
```

Add one birthday record per row. For example:

```csv
name,email(receiver's email),year,month,day
Alex,alex@example.com,1998,11,23
Sam,sam@example.com,2001,5,14
```

Use numeric values for `year`, `month`, and `day`.

**Important: The supplied CSV and current Python code have an email-column mismatch.** The CSV column is named `email(receiver's email)`, but `main.py` accesses `birthday_person["email"]`. These names must match before the program can run successfully. Either rename the CSV column to `email`, or update the Python code to access `birthday_person["email(receiver's email)"]`.

The supplied CSV currently contains only the header row and no birthday records. Add your own records before testing.

## Birthday Letter Template

Create `letter_templates/letter_1.txt`. The program looks for the exact path below:

```text
letter_templates/letter_1.txt
```

Example template:

```text
Dear [NAME],

Wishing you a very Happy Birthday!
May your day be filled with happiness and success.

Best wishes,
Your Name
```

The program replaces `[NAME]` with the recipient's name before sending the email.

## Gmail Configuration and Security

The current `main.py` contains placeholder values for the sender's Gmail address and password:

```python
my_email = "YOUR_EMAil_ADDRESS"
password = "PASSWORD"
```

Replace these placeholders with valid credentials before attempting to send an email. For Gmail, use an **App Password** when your account supports it. Do not use your normal Gmail account password.

For better security, avoid writing credentials directly in the source code. Store them in environment variables and read them in Python instead. Never commit real passwords, App Passwords, or other secrets to GitHub.

## Run the Project

1. Open a terminal in the project folder.
2. Install Pandas:

   ```bash
   pip install pandas
   ```

3. Add birthday records to `data.csv`.
4. Make sure the CSV email column name matches the key used in `main.py`.
5. Create `letter_templates/letter_1.txt`.
6. Configure Gmail SMTP credentials securely.
7. Run:

   ```bash
   python main.py
   ```

## Expected Output

If today's date matches a birthday record, the program prints details about the match, loads the letter, and attempts to send the email. A successful send reaches the final message:

```text
Email sent!
```

If no birthday matches today's date, the program prints:

```text
Not today.
```

The exact output also includes the current date tuple and the birthday dictionary because the current script prints those values for debugging.

## Current Limitations

- The program checks only the month and day. The `year` field is stored in the CSV but is not used to determine a match.
- The current code uses one letter template, `letter_1.txt`.
- The program sends an email only when a birthday matches the computer's current date.
- The current code uses Gmail SMTP (`smtp.gmail.com`, port `587`) and STARTTLS.
- The program does not currently include error handling for missing files, invalid CSV data, login failures, or network problems.
- The CSV supplied with this project is empty apart from its column headings.

## Technologies Used

- **Python**: Main programming language
- **Pandas**: Reads and processes birthday records from the CSV file
- **datetime**: Gets the current date
- **smtplib**: Connects to Gmail SMTP and sends email messages
- **CSV**: Stores names, email addresses, and birthday dates

## Possible Improvements

- Select a random letter from multiple templates.
- Add validation for dates and email addresses.
- Add error handling for SMTP and file operations.
- Keep credentials in environment variables.
- Add logging instead of relying only on `print()` statements.
- Add a test mode that displays the generated email without sending it.

---

**Note:** This README documents the behavior and file requirements of the supplied `main.py` and `data.csv`. Fix the email-column mismatch and add the missing letter template before running the project.
