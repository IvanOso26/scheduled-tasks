##################### Normal Starting Project ######################
import os 
import smtplib
import datetime as dt
import random
import pandas as pd
import smtplib
from email.message import EmailMessage
MY_EMAIL = os.environ.get("pythonday32angela@gmail.com")
MY_PASSWORD = os.environ.get("ikem evks mzwv wyay")


now = dt.datetime.now()
month = now.month
day = now.day
today = (month,day)

data = pd.read_csv("birthdays.csv")
data.to_excel("birthdays.xlsx")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row.to_dict() for index,data_row in data.iterrows()}

if today in birthdays_dict:

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_dict[today]["name"])
        Email_message = EmailMessage()

        Email_message["Subject"] = "Happy Birthday!"
        Email_message["From"] = MY_EMAIL
        Email_message["To"] = birthdays_dict[today]["email"]
        Email_message.set_content(contents)



    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(Email_message)


