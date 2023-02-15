##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

my_email = "test.100.day@gmail.com"
app_password = "wukp pqxy imsi knzs"

# 1. Update the birthdays.csv
birth_csv = pandas.read_csv("birthdays.csv")
dict_csv = birth_csv.to_dict(orient="records")
current_month = int(dict_csv[0]["month"])
print(int(dict_csv[0]["day"]))
name_b = dict_csv[0]["name"]
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
print(day)
print(month)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as data:
    letter = data.read()
    current_letter = letter.replace("[NAME]", name_b)
    print(current_letter)
# 4. Send the letter generated in step 3 to that person's email address.
if month == current_month:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="onehandriddayofcode@yahoo.com",
                            msg=f"Subject:Hello\n\n{current_letter}.")
