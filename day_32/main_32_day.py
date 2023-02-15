import smtplib

my_email = "test.100.day@gmail.com"
password = "100dayofcode"
app_password = "wukp pqxy imsi knzs"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=app_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="onehandriddayofcode@yahoo.com",
#                         msg="Subject:Hello\n\nThis is body of my email.")

import random
import datetime as dt

now = dt.datetime.now()
wk = now.weekday()
md = now.month
a = now.day
print(md)
print(a)

# with open("quotes.txt") as data:
#     quotes = random.choice(data.readlines())
#     print(quotes)
#
# if now == now:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=app_password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="onehandriddayofcode@yahoo.com",
#                             msg=f"Subject:Hello\n\n{quotes}.")

# print(now)
#
# date_of = dt.datetime(year=1992, month=5, day=19)
# print(date_of)
