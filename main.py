from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

urls=[
    "https://www.cricbuzz.com/cricket-team/chennai-super-kings/58/players",
    "https://www.cricbuzz.com/cricket-team/delhi-capitals/61/players",
    "https://www.cricbuzz.com/cricket-team/punjab-kings/65/players",
    "https://www.cricbuzz.com/cricket-team/kolkata-knight-riders/63/players",
    "https://www.cricbuzz.com/cricket-team/mumbai-indians/62/players",
    "https://www.cricbuzz.com/cricket-team/royal-challengers-bangalore/59/players",
    "https://www.cricbuzz.com/cricket-team/rajasthan-royals/64/players",
    "https://www.cricbuzz.com/cricket-team/sunrisers-hyderabad/255/players",
]

with open('players.csv', 'a') as f:
    print("Name,Matches,Innings,NO,Runs,Highest Score,Average,Balls Faced,Strike Rate,100,200,50,4s,6s,"
          "Matches,Innings,Balls,Runs,Wickets,Best,Best,Economy,Average,Strike Rate,5W,10W", end="\n", file=f)

with open('points.csv','a') as f2:
    print("Name,Matches", end="\n", file=f2)

for url in urls:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    phtml = urlopen(req).read()

    psoup = soup(phtml, "html.parser")

    players = psoup.findAll("a", {"cb-col cb-col-50"})
    for player in psoup.findAll("a", {"cb-col cb-col-50"}):
        a = player.get("href")
        url2="https://www.cricbuzz.com/"+a
        req2 = Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
        phtml2 = urlopen(req2).read()
        psoup2 = soup(phtml2, "html.parser")
        name = psoup2.findAll("h1", {"class": "cb-font-40"})
        print(name[0].get_text())
        with open('players.csv', 'a') as f:
            print(name[0].get_text(), end=",", file=f)
        j=0
        i=0
        for tbody in psoup2.findAll('tbody'):
            for tr in tbody.findAll("tr"):
                for td in tr.findAll("td", {"class": "cb-col-8"}):
                    if td.get_text() == "IPL":
                        for td2 in tr.findAll("td", {"class": "text-right"}):
                            a = td2.get_text()
                            if(i<=23):
                                with open('players.csv', 'a') as f:
                                    print(a,end=",", file=f)
                                print(a, end=" ")
                                i=i+1
                                j=j+1
                            else:
                                with open('players.csv', 'a') as f:
                                    print(a, file=f)
                                print(a)
        if(j==0):
            with open('players.csv', 'a') as f:
                for i in range(25):
                    if(i<=23):
                        print("-", end=",",file=f)
                    else:
                        print("-", end="\n", file=f)

f.close()