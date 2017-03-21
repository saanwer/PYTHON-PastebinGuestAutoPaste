import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Pastebin Guest Auto Paste
#http://pastebin.com/
#Coded by | WarLord
#https://github.com/saanwer
def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("text", help="Pastebin text")
	parser.add_argument("name", help="Pastebin name")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	browser.get("http://pastebin.com/")

	textElement = browser.find_element_by_id("paste_code")#Type inside "" if you have more than one word in the args to avoid error while running
	textElement.send_keys(args.text)
	nameElement = browser.find_element_by_name("paste_name")#Type inside "" if you have more than one word in the args to avoid error while running
	nameElement.send_keys(args.name)
	nameElement.send_keys(Keys.ENTER)

	os.system('cls')#os.system('clear') if Linux
	print "[+] Auto Post success!"
	browser.close()

if __name__ == "__main__":
	Main()
