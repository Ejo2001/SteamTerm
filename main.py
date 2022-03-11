import sqlite3
import requests
import os


#stream = os.popen(Command)
#output = stream.read()
#print(output)

Conn = sqlite3.connect('GameDatabase.db')

Cursor = Conn.cursor()

try:
    Cursor.execute('''CREATE TABLE Games
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
    stream = os.popen("ls /etc/SteamGames/steamapps")
    output = stream.read()
    if output == "":
        print("No games found")
    else:
        print(output)
    input("Press enter to continue...")

def launch():
    stream = os.popen("firefox")
    print("Launch")
    input("Press enter to continue...")

def install():
    print("Install")
    input("Press enter to continue...")

def gamedb():
    print("gamedb")
    input("Press enter to continue...")

def updategamedb():
    print("Updating game database")
    response = requests.get(url)
    print(response.text)
    stream = os.popen("apt update")
    output = stream.read()
    print(output)
    input("Press enter to continue...")
    


updategamedb()

while True:
    stream = os.popen("clear")
    output = stream.read()
    print(output)
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
