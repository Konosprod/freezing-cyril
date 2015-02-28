from tkinter import Tk
from bs4 import BeautifulSoup
import urllib.request
import sys

def copy_to_clipboard(string):

	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)


def get_source(url):
	reponse = urllib.request.urlopen(url)
	
	page_source = reponse.read()
	
	return BeautifulSoup(page_source.decode("utf8"))
	
def get_infos():
	url = input("Collez l'url de l'anime : ")
	format = input("Entrez le format que vous voulez : ")
	team = input("Entrez la team de sub que vous souhaitez : ")
	
	return (url, format, team)
	
def get_release(html):
	return html.find('div', id="releases")
	
	
def get_release_url(format, team, releases):
	urls = "" 
	
	olds = releases.findAll('tr')
	
	for i in olds:
		if (format in i.text) and (team in i.text):
			urls += i.findAll("a")[1].get("href") + "\n"
			
	return urls
	
def get_url(format, team, releases):
	urls = ""
	
	urls = get_release_url(format, team, releases)
	
	return urls
	
 
	
def main():
	(url, format, team) = get_infos()
	html = get_source(url)
	releases = get_release(html)
	
	urls = get_url(format, team, releases)
	
	copy_to_clipboard(urls)
	
	print("Les liens sont dans votre presse-papier")
	input()
	
if __name__ == "__main__":
	main()
	
