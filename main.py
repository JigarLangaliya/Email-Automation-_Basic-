import datetime as dt
import pandas
import smtplib

# -------------------- CHECK TODAY'S DATE -------------------- #

today = dt.datetime.now()
today_tuple = (today.month, today.day)

print("Today's date:", today_tuple)

# -------------------- READ CSV -------------------- #

data = pandas.read_csv("data.csv")
print(data)

birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

print("Email dictionary:", birthdays_dict)

# -------------------- CHECK IF TODAY MATCHES -------------------- #

if today_tuple in birthdays_dict:

    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    print("Match found:", name, email)

    # -------------------- READ LETTER -------------------- #

    with open("letter_templates/letter_1.txt") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", name)

    print("Letter loaded")

    # -------------------- SEND EMAIL -------------------- #

    my_email = "YOUR_EMAil_ADDRESS"
    password = "PASSWORD"

    message = f"Subject: Testing Email\n\n{contents}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=message
        )

    print("Email sent!")

else:
    print("Not today.")