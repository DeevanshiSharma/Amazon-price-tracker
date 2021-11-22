import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import time



def price_tracker(): 
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Time: ", current_time)
	print("Connecting...")
	URL = "https://www.amazon.in/Kelloggs-Crunchy-Multigrain-Breakfast-Cereal/dp/B096JZNHKW/ref=sr_1_5?dchild=1&keywords=cereal&qid=1633085601&sr=8-5"
    # Get url to extract data
	r = requests.get(URL) 
	soup = BeautifulSoup(r.content , 'html.parser') 
	print("Fetching price...")
	js_test = soup.find('span', id ="priceblock_ourprice") 
	if js_test is None: 
		js_test = soup.find('span', id ="priceblock_dealprice")		
	
	for str in js_test.string() : 
		str = js_test 

	# To integer
	str = str[1:]
	# asc_str = str.encode("ascii")
	str = str.replace(",", "")
	str = str.replace(" ", "")
	current_price = int(float(str)) 
	print("Current price = ", current_price) 
	


while True: 
	price_tracker()
	print("Will fetch again after 1 minute. To stop press ctl + c...")
	time.sleep(60) 