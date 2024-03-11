## Installation and Set Up

First install Python version 3.10 or greater. You can find Pyton at their website here(https://www.python.org/).

Once you have confirmed Python is installed and is running a correct version, download the randomizer using either git or from the releases page.

You will need to set up some json files with data the application can read. Examples of these json files can be find in the example_json folder. Their are 3 file sthat need to be created, `compositions.json`, `players.json`, and `teams.json`. Files with those names must exist.

##### ff14.json

The games folder contains `ff14.json`, a file which has every job in FF14 contained in a dictionary.

    "PLD": {
        "full": "Paladin",
        "role": ["tank"]
    }

Looking at Paladin it is divided into three sections. A key, which is its shortened nickname and two fields, a `full` field for its full name, and a `role` filed with an array of its roles.

    "SCH": {
        "full": "Scholar",
        "role": ["healer", "shield"]
    }

Scholar is an example of a class with multiple roles, having both the `healer` and `shield` roles.

##### compositions.json

This is a file that contains a dictionary of all the possible compositions you want the randomizer to be able to fill.

    "Raid": ["tank", "tank", "shield", "regen", "melee", "ranged", "caster", "dps"],

For example, Raid wants 2 tanks, a shield healer, a regen healer, a melee dps, a ranged dps, a caster dps, and any dps.

    "Dungeon": ["tank", "healer", "dps", "dps"]

Dungeon is a less strict composition, wanting only a tank, healer, and 2 dps.

When looking for jobs to fill a slot, the randomizer will only pick from jobs that have that role. For example, only Scholar and Sage can fill a `shield` slot, but any of Scholar, Sage, White Mage, or Astrologian can fill a `healer` slot.

##### players.json

This a file that contains all the players that can form teams. It contains a players name, and the jobs they can play.

The `name` field contains the players name, while the `available_jobs` field contains the jobs they can play. `available_jobs` must be an array of strings, with each string corresponding to one of the nicknames used for jobs in `ff14.json`.

    {
        "name": "IPlayEverything",
        "available_jobs": ["DRK", "PLD", "GNB", "WAR", "MNK", "NIN", "SAM", "DRG", "RPR", "DNC", "BRD", "MCH", "RDM", "SUM", "BLM", "WHM", "SGE", "AST", "SCH"]
    }

IPlayEverything has them marked to play every possible job.

    {
        "name": "BLMMain",
        "available_jobs": ["BLM"]
    }

BLMMain only plays BLM.

Note that players with less jobs will select their roles first(the application will go through the players in the team, and assign them a role they can play and class to play it with).

##### teams.json

This is a file with teams of players. The randomizer will then fill out the selected composition with players from that team.

    "Static": ["IPlayEverything", "HealersOnly", "BLMMain", "TankerJo", "WeeabooFitin", "MetaSlave", "Miss_Jumpy_Rabbit", "Camelot"],

Each entry is simply the name of the team, and an array of the names of the players in that team.

## Running the Application

When you want to run the application, navigate to the folder it is installed using a command line, then type `python main.py COMPOSITION TEAMNAME` where COMPOSITION is the exact name of one of the compositions in compositions.json and TEAMNAME is the exact name of one of the teams in teams.json