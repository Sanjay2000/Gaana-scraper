import requests,json
from pprint import pprint 
from bs4 import BeautifulSoup
from pprint import pprint
import webbrowser

url="https://gaana.com/topcharts"
page= requests.get(url).text
soup = BeautifulSoup(page,"html.parser")
search=soup.find_all("div",class_="arwtork_label")
url_list=[]
a=0
for j in search:
	a+=1
	url=("https://gaana.com"+j.find('a').get('href'))
	naam_lst=(j.find('a').text)
	print(a,naam_lst)
	url_list.append(url)
user=int(input("ennter the nubr >"))
req=(url_list[user-1])
song_req=requests.get(req).text

soup1=BeautifulSoup(song_req,"html.parser")
get=soup1.find_all("div",class_="playlist_thumb_det")
song_url=[]
b = 0
for i in get:
	b+=1
	song_name=(i.find("a").text)	
	pprint(str(b)+" "+song_name)
	song_url.append(i.find('a').get("href"))
user1=int(input('enter the song >'))
gaana=(song_url[user1-1])
webbrowser.open(gaana, new=0, autoraise=True)





