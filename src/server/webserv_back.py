import requests, json

# Startup

state_package = (NULL, NULL, NULL, NULL)
state = state_package[0]
team = state_package[1]
player = state_package[2]
champion_id = state_package[3]

#Reception of info

#while champ select ongoing we wait for info (?, need to see how comm works here)

# With this link we can access the champion's whole json
champ_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{champion_id}.json"
req = requests.get(champ_url)
champ_json = req.json()

# Let's suppose we get a champion "id" (cdragon, "key" in ddragon)
# Then we need to also grab the champions "alias" attribute (cdragon, "id" in ddragon)
champion_alias = champ_json["alias"].lower()

# Champion Icons:
# champion_id = champion's "id" attribute in cdragon json
icon_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/{champion_id}.png"
print(icon_url)

# Champion Loadscreen banner
banner_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/{champion_alias}/skins/base/{champion_alias}loadscreen.jpg"
print(banner_url)