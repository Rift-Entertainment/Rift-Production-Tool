# Rift-Production-Tool

## Dependencies
To run this program you need Python 3.  
You also need the "requests" as well as the "paramiko" library, installable using:  
    `python -m pip install requests` <br />
    `python -m pip install paramiko`

## Riot.txt

Create a file "riot.txt", which contains a code letting riot find the project

## Product Registration

### Product name

Rift Production Tool

### Product Description
Rift Production Tool is a tailored multi-functional tool, used to give a better experience for League of Legends tournaments.
In first instance it will use the Spectator API to collect and return to a web-application the pick & ban phase of livestreamed matches of a tournament, in order to show said phase off through an aesthetically fitting interface.
The second instance is the usage of the Tournament API, to automatically prepare the game lobbies to make it easier for both the organizers and for the players, and also to collect the data related to the tournament's games, in order to show off for example, exemplar performances from players or overall statistics before important matches.
The tool would be used by Rift Entertainment asbl. a Luxembourg based non-profit organization (asbl.), providing high quality livestreaming services in Luxembourg and its surroundings, but also on a mission to provide overall entertainment to the people. We've already produced the show of a League of Legends tournament, and also being fans of the game we wish to further improve our production quality,  and our own potential tournaments, by using this tool.

## Documentation

This tool will make use of various APIs with the goal of improving the production quality of our League of Legends related treams.  
It will go through an undefined number of steps, with each step already improving the production.  
We will develop the product step by step and try to only move on to the next step once the current one is done.  
Steps may be added or removed along the way, or multiple steps may be fused into one and vice versa.  
For each step the way they will be executed will be described more or less precisely, the description evolving alongside development.  

### Steps

#### Step 1 - Live Pick&Ban Capture

  * Composants
    - "Game PC", PC in the lobby as spectator, which will run the program
    - "Stream PC", PC on which vmix is running, taking the webpage as browser source
    - A webserver hosting the webpage and containing its assets

  * Functional expectations
    - The program needs access to the current "champions.json"
    - The program uses the champions' ids to get their alias
    - The interface is coded in HTML and on a local website
    - The program sends a link (determined in the python script using the champion id) to the image to insert on the website, to the json file and the champ select's status

  * Program:
    - Using the LCU, the program detects entering a lobby, the interface is reset.
    - Once champ selection has started, player names are updated in the interface (before Tournament API, team logos will have to be put in through vmix)
    - Every 0.5 seconds the program updates the client's status, if an update happened ((summoner) spell, pick/ban, swap (,perk change)), the necessary link is updated in the json. Also, the timer is updated every 0.5 second.
    - Once the champ select is over, the program may stop running

##### Design
    * The webpage being hosted on a webserver, the same webserver will contain the json file and some local images.
        --> Find how we will modify the json file using a python script

#### Step 2 - (No tournament API) Stat tracking
   
  * To track player and team stats throughout a tournament
    - Get Match ID from played games (manually get them when players play a match)
      
#### Step 2' - (Tournament API) Stat tracking
  
  * Matches can be savec automatically using the tournament API 
