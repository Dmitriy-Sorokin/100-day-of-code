import smtplib

my_email = "test.100.day@gmail.com"
app_password = "wukp pqxy imsi knzs"

class NotificationManager:


    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="onehandriddayofcode@yahoo.com",
                                msg=f"Subject:Hello\n\n.Umbrella ooooeeeeeeeyyyyyy.")
