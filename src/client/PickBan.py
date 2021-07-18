import requests, json
from paramiko import *

"""
Deprecated, but kept for now as reference
# Send signal to clean web interfae
base_url = "https://euw1.api.riotgames.com"
reg_url = "https://europe.api.riotgames.com"
# Personal key here for testing purposes
print("Enter your API key: ")
key = input()
if not key:
    key =""
key_url = "?api_key="+key

print("\nEnter the Summoner name of the account you wish to spectate: \n(By default it's '')")
sum = input()
if not sum:
    sum = ""

r = requests.get(f"{base_url}/lol/summoner/v4/summoners/by-name/{sum}{key_url}")
r_status_code = r.status_code
if r_status_code == 200:
    d = r.json()
    encryptedSummonerId = d["id"]
    print(f"Got id from user: {sum}")

r = requests.get(f"{base_url}/lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}{key_url}")
r_status_code = r.status_code
print(r_status_code)
if r_status_code == 200:
    c_game = r.json()
    print(c_game)
    print(c_game["gameStartTime"])
    print(c_game["gameLength"])
"""
# Send Signal that Champ Select was started + Summoner names

# During Champ Select:

## Check if current state package has changed, if yes send it
## A state package is a tuple of the form: (state, {Blue/Red}, {0/1/2/3/4}, champ_id)
## I.e. If current state was (NULL, NULL) (default) and we get state: Blue player 0 banning champ, we send (1, Blue, 0, NULL) to server
## If no champion is to be sent in that state, the id is NULL
"""
States:
0   - NULL (default state) - Every position slot only has the player's role icon, under it the player's Summoner name and the ban_slots contain a base icon
1   - {Blue/Red} banning champ {0/1/2/3/4} - {Blue/Red} team's player {0/1/2/3/4} is currently banning an enemy champion, ban_champ_ph in slot {0/1/2/3/4} is blinking in banning team's colour
2   - {Blue/Red} locked ban champ {0/1/2/3/4} - {Blue/Red} team's player {0/1/2/3/4} just locked a ban, champ_icon is put instead respective ban_champ_ph in slot {0/1/2/3/4}
3   - {Blue/Red} picking {0/1/2/3/4} - {Blue/Red} team's player {0/1/2/3/4} is currently picking but not hovering a champion, position slot {0/1/2/3/4} blinks in the team's colour, and the player's Summoner name is highlighter the same colour.
4   - {Blue/Red} hovering champ {0/1/2/3/4} - {Blue/Red} team's player {0/1/2/3/4} is currently hovering a champion, position slot {0/1/2/3/4} is replaced with champion_banner. Summoner name is still highlighted in team's colour and slot still blinks.
5   - {Blue/Red} locks pick {0/1/2/3/4} - {Blue/Red} team's player {0/1/2/3/4} just locked a pick, position slot {0/1/2/3/4} is replaced with champion_banner, Summoner name returns to normal, and slot stops blinking
"""

# Base banners links for reset
base_top_banner = "assets/banner-top.png"
base_jgl_banner = "assets/banner-jgl.png"
base_middle_banner = "assets/banner-middle.png"
base_bottom_banner = "assets/banner-bottom.png"
base_sup_banner = "assets/banner-sup.png"

# Bases of the links for banners and icons
banner_link = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/"
bl_core = "/skins/base/"
bl_tail = "loadscreen.jpg"

icon_link = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/"
il_tail = ".png"

# SSH connection data
host = ""
port = 22
username = "admin"
password = input()

# Creation of transport to create an SFTP connection
transport = Transport((host, port))
transport.connect(username=username, password=password)
sftp = SFTPClient.from_transport(transport)

# Loading json data of file
sftp.chdir("")
myfile = sftp.open("links.json")
json_obj = json.load(myfile)
myfile.close()
print("file closed")

# Setting up for while loop
go = True
start = time.time() # Temporarily used to limit loop in time

while go:
	start_time = time.time() # Used to measure time passed during actions

	# Temporary way of setting right data in json file, will change once access to LCU is granted
	side = "blue"
	phase = "picks"
	pos = "1"
	champion_name = "ahri"
	timestamp = int(time.time()*100)

	# Modifying json data
	json_obj["timestamp"] = timestamp
	json_obj["links"][side][phase][pos] = banner_link+champion_name+bl_core+champion_name+bl_tail

	# Updating json file
	myfile = sftp.open("links.json", "w")
	json.dump(json_obj, myfile)
	myfile.close()

	# Checking time
	duration = time.time() - start_time
	difference = 0.5-duration
	if difference > 0:
		time.sleep(difference)
	if time.time() - start >= 5:
		go = False


# Closing the SSH conncections
sftp.close()
print("sftp closed")
transport.close()
print("transport closed")