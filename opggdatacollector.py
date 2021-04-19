from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bSoup
import datetime

#Functions

def giveChampNum(champName):
	if(champName == "")

def getPlayerLink(name):
	linkName = name.replace(" ", "+")
	"https://na.op.gg/summoner/userName=" + linkName

def collectPerson(name):
	and_url_group = getPlayerLink(name)
	new_url = and_url_group
	sClient = cReq(new_url)
	snd_page_html = sClient.read()
	sClient.close()

	snd_page_soup = bSoup(snd_page_html, "html.parser")
	gamesCollected = 0

	while(gamesCollected < 10):
		games = snd_page_soup.findAll("div",{"class":"GameItemWrap"})
		gametype = games[gamesCollected].find("div",{"class":"GameType"})
		if(gametype.text == "Ranked Solo"):
			teams = games[gamesCollected].findAll("div",{"class":"Team"})
			try:
				temp = teams[0].find("div",{"class":"Summoner Requester"})
				playersTeam = 0
			except:
				playersTeam = 1
			try: 
				f.write()

filename = date + ".csv"

f = open("Data/" + filename, "w")



f.close()