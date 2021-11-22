import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib

# put in the url of product whose price you want to track
Url = "copy_the_url"
# change header according to your device
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

def send_mail():
    # connecting to the smtplib server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    #logging in the senders account
    server.login( 'Your_id', 'your_psswd')
    
    # the message 
    subject = 'Offers on your favourite Products!! ' 
    body = ("Check out latest offer's available for your favourite Amazon product !!!!! "+ Url )

    msg = f"Subject: {subject}\n\n{body}"
    
    #sending the mail with latest price
    server.sendmail("senders_id","recievers_id",msg)

    #print a message to confirm that the email has been sent
    print('Mail has been sent.')
    
    # quitting the server
    server.quit()

def price_tracker():
    now = datetime.now()

    current_date = now.strftime("%m/%d/%Y")
    current_time = now.strftime("%H:%M:%S")

    print( "On ", current_date, " at " , current_time)
    
    # extracting data from the url
    r = requests.get(Url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    
    # fetching required data
    product_title = soup.find(id = "productTitle").get_text().strip()

    product_price = soup.find('span', id = 'priceblock_ourprice')
    
    if product_price is None :
        product_price = soup.find('span', id = 'priceblock_dealprice')
    
    str = ""
    
    for line in product_price.stripped_strings :
        str = line
    
    str = str[1:]
    
    current_price = str
    
    print("Current price of", product_title ,"is Rs.",current_price)
    
    send_mail()
    

while True :
    price_tracker()
    
    input("Press Enter to fetch again.")
