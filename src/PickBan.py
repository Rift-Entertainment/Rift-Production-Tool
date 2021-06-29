import requests, json


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
