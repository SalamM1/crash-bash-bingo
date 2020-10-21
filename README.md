# Crash Bash Bingo Generator
Python script to generate JSON export of a Crash Bash Bingo that can be used on Bingosync.com


## How to Run
No external libraries are used.
Make sure the data/ folder is in the same folder as the main.py file. Make sure the data/ folder contains the cbash-bingo-config.json AND cbash-bingo-data.csv file.
To run, simply call python on the main.py file (main.py). This will output the result into a file "crashbash-bingo.json", and also print to command line. The result can be pasted directly on to [bingosync.com](https://bingosync.com/).


## Configuration
The generator allows you to configure what it can generator to a certain extent. All these options can be found in the data/cbash-bingo-config.json file. An explanation for all the settings is given below.


### Warp Rooms
There are 5 boolean options. The options match each of the five warp rooms in Crash Bash. Marking the first entry as "False" will remove all levels in the First Warp Room from the generator, and so on.


### Game Types
There are 7 boolean options. There are 7 game types in Crash Bash, each with 4 minigames (eg. Crashball games are Crashball, Beach Ball, N. Ballism and Sky Balls). The order if as follows:
* Crashball
* Polar
* Pogo
* Bash
* Fox
* Dash
* Medieval 


"False" will remove the respective set of games from the generator.


### Bosses
As the name suggests, "False" will remove Bosses from the generator.


### Collectible
There are 5 boolean options. The options match type of challenge available in the game in the order as follows:
* Trophy
* Gem
* Crystal
* Gold Relic
* Platinum Relic

"False" will remove the challenge from appearing in the generator.


### Exclude Levels
This is a list of level names (eg. Pogo Padlock) or challenges (eg. Ring Ding Platinum Relic) as strings. Any level or challenges inserted here will be excluded regardless of the previous settings.


### Included Levels
This is a list of level names (eg. Pogo Padlock) as strings. Any level inserted here will be included regardless of the previous settings.
