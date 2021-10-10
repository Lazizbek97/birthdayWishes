##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import os, random
import csv
import smtplib

MY_EMAIL = "lazizbekfayziyev@gmail.com"
MY_PASSWORD = "lazizjonsh97"

wish_to = ""
now = dt.datetime.now()
month = str(now.month)
day = str(now.day)
with open("birthdays.csv", "r") as bds_file:
    birthdays = csv.reader(bds_file)
    for birthday in birthdays:
        if month==birthday[3] and day == birthday[4]:
            file  = random.choice(os.listdir("/home/lazizbek/Desktop/udemy/birthday_wisher/letter_templates/"))
            wish = ''
            with open(f"letter_templates/{file}","r") as wish_letter:
                data = wish_letter.readlines()
                ''.join(data)
                for row in data:
                    wish += row
                wish_to = wish.replace("[NAME]", f"{birthday[0]}")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="laziz.fayziev@mail.ru",
                        msg=f"subject:Happy Birthday!\n\n{wish_to}")



