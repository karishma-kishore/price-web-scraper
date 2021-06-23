import requests
from bs4 import BeautifulSoup
import smtplib
import time

#the url of the item whose price you want to track
URL='https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1624172630&sr=8-1'

#add your user agent
headers = {"User-Agent": ''}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[2:]
    convt_price = float(converted_price.replace(',',''))
    if(convt_price < 159990): #the price you want
        send_mail()

    #print(title.strip())
    #print(convt_price)

def send_mail():
    #to make a connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.ehlo()
    #to secure the connection
    server.starttls()
    server.ehlo()

    #enter credentials of the gmail acc from which you want to send an email
    server.login('','')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1624172630&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'xyz@gmail.com', #gmail acc from which you're sending the email
        'abc@outlook.com', #acc receiving the email
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

check_price()

#to execute it for x no. of times a day or so
#while(True):
#   check_price()
#  time.sleep(60*60)