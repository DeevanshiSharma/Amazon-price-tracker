# Amazon price tracker\python
 Amazon product price tracker using Python & beautiful soup takes user input (URL of the product), fetches the price of that product from Amazon, and notifies via email.

Amazon product price tracker in python language scrapes the price of a product from the URL provided and notifies the user via email in real-time. 

The basic approach is that it gets access to the source code of the product page and scrapes the required details such as product title and product price. After scraping it logs in to the senders account and automatically send an email regarding the product price to the receiver.

Required libraries and modules:

>smtplib

>requests

>bs4

>datetime

If you have these packages already installed you are good to go. Otherwise, you can simply install these packages using the following command:

pip install package-name
Now, just implement the code and you are good to go :)

After executing the code, the output on the terminal should look something like this:
 ![image](https://user-images.githubusercontent.com/87795451/142896772-1110804c-9be2-40bc-8b83-bafcd72cef77.png)

Good luck!
