import smtplib

my_email = "test.100.day@gmail.com"
password = "100dayofcode"
app_password = "wukp pqxy imsi knzs"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="onehandriddayofcode@yahoo.com",
                        msg="Subject:Hello\n\nThis is body of my email.")
