import smtplib
import datetime as dt
import random

MY_EMAIL = "pchu204@yahoo.com"
MY_PASSWORD = "abcXYZ12@"

now = dt.datetime.now()
# year = now.year
# month = now.month
# date_of_birth = dt.datetime(year=1994, month=12, day=15, hour=22)
# print(date_of_birth)
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:  # this SMTP information is specific for yahoo mail only.
        # for hotmail: smtp.live.com
        # for gmail: smtp.mail.google.com
        # for any other SMTP information, just Google

        # TLS: Transfer Layer Security: Way of securing connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jaanmunu007@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

        """
        Running this might result in some errors. Go to gmail security page and turn off
        'Two-step verification' and 'Use your phone to sign-in'
        Turn on 'less secure apps'
        """
    print(quote)