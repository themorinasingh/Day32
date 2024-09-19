#Imports
import datetime as dt
import random
import smtplib
import pandas

#harnessing data from csv
data = pandas.read_csv("./birthdays.csv")
birthdays = data.to_dict(orient="records")
# print(birthdays)

#Function to send birthday email
def email_sender(to_email="morinasing@gmail.com", name="Morina"):
    my_email = "morinasinghji@gmail.com"
    password = "sylp pxfl lrsq dlgi"

    num_list = [1,2,3]
    with open(f"./letter_templates/letter_{random.choice(num_list)}.txt") as file:
        email_body = file.read()

    email_body = email_body.replace("[NAME]", name)

    message = f"Subject:Happy Birthday! \n\n {email_body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=to_email, msg=message)

#checking today's date and sending emails
today = dt.datetime.now()
for birthday in birthdays:
    if birthday["month"] == today.month and birthday["day"] == today.day:
        email_sender(birthday["email"], birthday['name'])

