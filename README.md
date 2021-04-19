# Discord LazySlavie
A multipurpose Discord bot with several features such as a string-to-PDT calculator, google search, among others. This project will use Discord.py API to function.
    
## Features
### Text-based Calculator
The text-based calculator featured in LazySlavey is directly stolen from a dedicated console applet.

It takes string as input, checks every character, removes all invalid characters, groups numbers and operators inside strings in a list, scans for operators, does operations in order using PEMDAS, then outputs the result.
### Google Search
This google search module relies on another module called googlesearch. The code here is purely for compatibility with __init__.
### Random reponse (yesno, fishbowl, rps, d6, d20, megarps, russianroulette)
All RNG-based applets belong in this category. All the possible options are categorized in lists stored in a module called listlist.py.
    These applets simply choose a random item in a list and outputs the result. Some (like fishbowl and russianroulette) involve more code to work as intended.
### Games
There are currently no games made for this bot. Planned games are as follows:
* 100-level mini-RPG game
* Tictactoe
* Keep talking and nobody explodes
* Uno

## Installation:
Contact the head developer [@DefinitelyRus](twitter.com/DefinitelyRus) for installation instructions.

## Usage:
Simply extract the .rar file and run __init__.py.
**Please read the installation instructions before doing this!**

## Contributors:
* DefinitelyRus

## License: 
This project uses GNU General Public License v3.0. See LICENSE for more information.

## Trivia:
* The "Lazy" in LazySlavie refers to our group called Lazy Buns because Rus is part of the group and he wanted to make his own Discord bot for his server and also his friends' servers. The "Slavie" refers to the European ethnic-linguistic group called "Slavs". All members of Lazy Buns pronouce it as /slave-y/ as suppose to a more proper /slav-ie/, although Rus says it should **not** be confused with slaves, even when the group insists otherwise because of their dark humor.
* Many commands LazySlavie features are from Rus's previous projects when he didn't bother with UI. He simply repurposed the code to be usable with the bot, instead of just being an ugly console app.
* The game Text Adventure is originally planned as a console-based test-only RPG game to be made with Kerlernder. It's still functionally the same, but it uses Discord as a medium instead of a console. It also lets multiplayer be implement much more easily.
