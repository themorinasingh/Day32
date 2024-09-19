import smtplib

my_email_account = "morinasinghji@gmail.com" #testing
password = "sylp pxfl lrsq dlgi"

with  smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email_account,password=password)
    connection.sendmail(
        from_addr=my_email_account,
        to_addrs="morinasingh05@gmail.com",
        msg="Subject: Hi,"
            "\n How are you?"
            "Morina") #testing


