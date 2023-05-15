from twilio.rest import Client
import os
import smtplib
import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.in/Apple-MacBook-Laptop-12%E2%80%91core-30%E2%80%91core/dp/B0BSJ3FD8W/ref=sr_1_3?keywords=laptop&refinements=p_36%3A20000000-&rnid=7252027031&sr=8-3"
HEADER_URL="https://myhttpheader.com/"
PRICE_YOU_WANT_TO_BUY_AT=400000
header_data=requests.get(HEADER_URL)

data=requests.get(URL).text
soup=BeautifulSoup(data,"html.parser")
price=soup.select_one("span .a-price-whole").getText().replace(",","")[:-2]
title=soup.select_one("#productTitle").getText()
if (int(price)<PRICE_YOU_WANT_TO_BUY_AT):
    account_sid=os.environ["ACCOUNT_SID"]
auth_token=os.environ["AUTH_TOKEN"]
# Sending Message
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"{title} is available at {PRICE_YOU_WANT_TO_BUY_AT} you can check it out at {URL}",
    from_="TWILIO PROVIDED NUMBER",
    to="TO NUMBER"
)

print(message.status)
# Sending Email
my_mail="YOUR EMAIL"
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_mail,password="YOUR PASSWORD FOR APP")
                connection.sendmail(from_addr=my_mail,to_addrs=my_mail,msg=f"Subject:Price Drop Alert\n\n{title.encode('utf-8')} is available at {PRICE_YOU_WANT_TO_BUY_AT}you can check it out at {URL}")
                connection.close() 


