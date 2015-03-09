from tkinter import Tk
from bs4 import BeautifulSoup
import urllib.request
import requests
import argparse
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
	
def add_to_client(urls):
	payload = {'urls' : urls}
	headers = {'Content-Type'  : 'application/x-www-form-urlencoded'}
	r = requests.post("http://127.0.0.1:8080/command/download/", data=payload, headers=headers)
	return 0
		
def get_urls():
	(url, format, team) = get_infos()
	html = get_source(url)
	releases = get_release(html)
	
	urls = get_url(format, team, releases)
	
	#add_to_client(urls)
	
	#copy_to_clipboard(urls)
	
	#print("Les liens sont dans votre presse-papier")
	
	return urls

def print_menu():
	choix = int(input("Que voulez-vous ?\n\t1) Presse papier\n\t2) Ajouter au clien torrent\n: "))
	while(choix < 1 and choid > 2):
		choix = int(input("Que voulez-vous ?\n\t1) Presse papier\n\t2) Ajouter au clien torrent\n: "))
	
	return choix
	
def main():
	
	choix = print_menu() 
	
	urls = get_urls()
	
	if choix == 1:
		copy_to_clipboard(urls)
	else:
		add_to_client(urls)
	
	return 0
	
if __name__ == "__main__":
	main()
	
