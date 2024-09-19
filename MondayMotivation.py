import smtplib
import datetime as dt
import random

now = dt.datetime.now()
today = now.weekday()

with open("quotes.txt") as file:
    quotes = file.read()

quote_list = quotes.split("\n")

my_email_account = "morinasinghji@gmail.com" #testing
password = "sylp pxfl lrsq dlgi"

if today == 3:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() #enables transport layer security, which encrypts our email on way to receiver
        connection.login(user=my_email_account, password=password)
        connection.sendmail(from_addr=my_email_account, to_addrs="morinasing@gmail.com", msg=f"Subject: Monday Motivation \n\n {random.choice(quote_list)}")