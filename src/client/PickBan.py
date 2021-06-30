import requests, json

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