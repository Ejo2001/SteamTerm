import sqlite3
import requests
import os
import time
from termcolor import colored

#stream = os.popen(Command)
#output = stream.read()
#print(output)

Conn = sqlite3.connect('gamedatabase.db')

Cursor = Conn.cursor()

try:
    Cursor.execute('''CREATE TABLE games 
            (appid, name, publisher, launchcmd, filename)''')
except:
    print("Database already exist")

url = "http://104.248.34.22:8000"

class game():
    def __init__(self):
        self.filename = "NULL"
        self.appid = "NULL"
        self.name = "NULL"
        
def gamelibrary():
    stream = os.popen("clear")
    output = stream.read()
    print(output)
    stream = os.popen("ls /etc/SteamGames/steamapps")
    output = stream.read()
    if output == "":
        print("No games found")
    else:
        print(output)
    input("Press enter to continue...")

def launch():
    Cursor.execute("SELECT * FROM games")
    launchlist = {}
    count = 1
    for g in Cursor.fetchall():
        stream = os.popen("ls /etc/SteamGames/steamapps")
        output = stream.read()
        if output.find(g[4]) == 0:
            launchlist[count] = g[1]
            count += 1
    for item in launchlist:
        print(f"{item} {launchlist.get(item)}")
    gtl = input("Which game would you like to launch?")
    command = ("SELECT launchcmd FROM games WHERE name = Counter-Strike: Global Offensive")
    print(Cursor.execute(command))
    #Cursor.execute(command)
    #print(command)
    #stream = os.popen(command)
    time.sleep(3)
    input("Press enter to continue...")

def install():
    Cursor.execute("SELECT * FROM games")
    print("Install")
    launchlist = {}
    count = 1
    for g in Cursor.fetchall():
        stream = os.popen("ls /etc/SteamGames/steamapps")
        output = stream.read()
        print(g[4])
        if not output.find(g[4]):
            launchlist[f"{count}"].append(g[1])
            count += 1
    input("Press enter to continue...")

def gamedb():
    Cursor.execute("SELECT * FROM games")
    for g in Cursor.fetchall():
        print(g[1])
    input("Press enter to continue...")


def updategamedb():
    print("Updating game database")
    response = requests.get(url)
    if int(response.status_code) == 200:
        Cursor.execute("drop table games")
        Cursor.execute("CREATE TABLE games (appid, name, publisher, launchcmd, filename)")
        for i in response.json():
            Cursor.execute("INSERT INTO games (appid, name, publisher, launchcmd, filename) VALUES (?, ?, ?, ?, ?)", (i["appid"], i["name"], i["publisher"], i["launchcmd"], i["filename"]))
    else:
        print("Could not reach database, Error Code " + str(response.status_code))
    

def start():
    print(colored('STEAMTERM', 'green', attrs=['bold']))
    time.sleep(2)
    updategamedb()




start()

while True:
    time.sleep(1)
    stream = os.popen("clear && cat ./logo.txt")
    output = stream.read()
    print(output)
    print(colored('_'*15, 'red'))
    print("1. List installed games\n2. View game database\n3. Install game\n4. Launch game\n5. Quit")
    answer = input("Please enter a number: ")
    try:
        if int(answer) == 1:
            gamelibrary()
        elif int(answer) == 2:
            gamedb()
        elif int(answer) == 3:
            install()
        elif int(answer) == 4:
            launch()
        elif int(answer) == 5:
            break
    except:
        print("Please enter a correct input")

stream = os.popen("clear")
output = stream.read()
print(output)
