###################################################
# ElementUser's Simple Patch Notes Formatter
# Google Sheet Reference: https://docs.google.com/spreadsheets/d/1f98szyd025VFLrT1yBZG_9lQZiz0eIZ3sbBX49xNX4U/edit#gid=585347818
###################################################

from shutil import copyfile
import in_place
import datetime

# Variables
timeNow = datetime.datetime.now()
yearNow = str(timeNow.year)
yearNowPlusOne = str(timeNow.year + 1)

gamePatchNotes = 'game_output.txt'
forumPatchNotes = 'forum_output.txt'
motdPatchNotes = 'motd_output.txt'

# heroList also contains neutrals for the sake of entity highlighting
heroList = [ "Accursed" , "Adrenaline" , "Aluna" , "Amun-Ra" , "Andromeda" , "Apex" , "Arachna" , "Armadon" , "Artesia" , "Artillery" , "Balphagore" , "Behemoth" , "Berzerker" , "Blacksmith" , "Blitz" , "Blood Hunter" , "Bombardier" , "Bramble" , "Bubbles" , "Bushwack" , "Calamity" , "Chipper" , "Chronos" , "Circe" , "Corrupted Disciple" , "Cthulhuphant" , "Dampeer" , "Dark Lady" , "Deadlift" , "Deadwood" , "Defiler" , "Demented Shaman" , "Devourer" , "Doctor Repulsor" , "Draconis" , "Drunken Master" , "Electrician" , "Ellonia" , "Emerald Warden" , "Empath" , "Engineer" , "Fayde" , "Flint Beastwood" , "Flux" , "Forsaken Archer" , "Gauntlet" , "Gemini" , "Genesis" , "Geomancer" , "Glacius" , "Gladiator" , "Goldenveil" , "Gravekeeper" , "Grinex" , "Gunblade" , "Hammerstorm" , "Hellbringer" , "Ichor" , "Jeraziah" , "Kane" , "Keeper of the Forest" , "Kinesis" , "King Klout" , "Klanx" , "Kraken" , "Legionnaire" , "Lodestone" , "Lord Salforis" , "Madman" , "Magebane" , "Magmus" , "Maliken" , "Martyr" , "Master of Arms" , "Midas" , "Moira" , "Monarch" , "Monkey King" , "Moon Queen" , "Moraxus" , "Myrmidon" , "Night Hound" , "Nitro" , "Nomad" , "Nymphora" , "Oogie" , "Ophelia" , "Pandamonium" , "Parallax" , "Parasite" , "Pearl" , "Pebbles" , "Pestilence" , "Pharaoh" , "Plague Rider" , "Pollywog Priest" , "Predator" , "Prisoner 945" , "Prophet" , "Puppet Master" , "Pyromancer" , "Qi" , "Rally" , "Rampage" , "Ravenor" , "Revenant" , "Rhapsody" , "Riftwalker" , "Riptide" , "Salomon" , "Sand Wraith" , "Sapphire" , "Scout" , "Shadowblade" , "Shellshock" , "Silhouette" , "Sir Benzington" , "Skrap" , "Slither" , "Solstice" , "Soul Reaper" , "Soulstealer" , "Succubus" , "Swiftblade" , "Tarot" , "Tempest" , "Thunderbringer" , "Torturer" , "Tremble" , "Tundra" , "Valkyrie" , "Vindicator" , "Voodoo Jester" , "War Beast" , "Warchief" , "Wildsoul" , "Witch Slayer" , "Wretched Hag" , "Zephyr"  "Accursed" , "Adrenaline" , "Aluna" , "Amun-Ra" , "Andromeda" , "Apex" , "Arachna" , "Armadon" , "Artesia" , "Artillery" , "Balphagore" , "Behemoth" , "Berzerker" , "Blacksmith" , "Blitz" , "Blood Hunter" , "Bombardier" , "Bramble" , "Bubbles" , "Bushwack" , "Calamity" , "Chi" , "Chipper" , "Chronos" , "Circe" , "Corrupted Disciple" , "Cthulhuphant" , "Dampeer" , "Dark Lady" , "Deadlift" , "Deadwood" , "Defiler" , "Demented Shaman" , "Devourer" , "Doctor Repulsor" , "Draconis" , "Drunken Master" , "Electrician" , "Ellonia" , "Emerald Warden" , "Empath" , "Engineer" , "Fayde" , "Flint Beastwood" , "Flux" , "Forsaken Archer" , "Gauntlet" , "Gemini" , "Genesis" , "Geomancer" , "Glacius" , "Gladiator" , "Goldenveil" , "Gravekeeper" , "Grinex" , "Gunblade" , "Hammerstorm" , "Hellbringer" , "Ichor" , "Jeraziah" , "Kane" , "Keeper of the Forest" , "Kinesis" , "King Klout" , "Klanx" , "Kraken" , "Legionnaire" , "Lodestone" , "Lord Salforis" , "Madman" , "Magebane" , "Magmus" , "Maliken" , "Martyr" , "Master of Arms" , "Midas" , "Mimix" , "Moira" , "Monarch" , "Monkey King" , "Moon Queen" , "Moraxus" , "Myrmidon" , "Night Hound" , "Nitro" , "Nomad" , "Nymphora" , "Oogie" , "Ophelia" , "Pandamonium" , "Parallax" , "Parasite" , "Pearl" , "Pebbles" , "Pestilence" , "Pharaoh" , "Plague Rider" , "Pollywog Priest" , "Predator" , "Prisoner" , "Prophet" , "Puppet Master" , "Pyromancer" , "Rally" , "Rampage" , "Ravenor" , "Revenant" , "Rhapsody" , "Riftwalker" , "Riptide" , "Salomon" , "Sand Wraith" , "Sapphire" , "Scout" , "Shadowblade" , "Shellshock" , "Silhouette" , "Sir Benzington" , "Skrap" , "Slither" , "Solstice" , "Soul Reaper" , "Soulstealer" , "Succubus" , "Swiftblade" , "Tarot" , "Tempest" , "Thunderbringer" , "Torturer" , "Tremble" , "Tundra" , "Valkyrie" , "Vindicator" , "Voodoo Jester" , "War Beast" , "Warchief" , "Wildsoul" , "Witch Slayer" , "Wretched Hag" , "Xemplar" , "Zephyr", "Catman Champion", "Dragon Master", "Dreadbeetle Queen", "Minotaur", "Predasaur Crusher", "Skeleton King", "Vulture Lord", "Vagabond Leader", "Werebeast Enchanter", "Wolf Commander", "Dragon", "Fire Ogre", "Dreadbeetle", "Predasaur"]
itemList = [ "Abyssal Skull" , "Acolyte's Staff" , "Alacrity Band" , "Alchemist's Bones" , "Amulet of Exile" , "Apprentice's Robe" , "Arcana" , "Arcane Bomb" , "Arcane Nullifier", "Armor of the Mad Mage" , "Assassin's Shroud" , "Astrolabe" , "Axe of the Malphai" , "Barbed Armor" , "Barrier Idol" , "Beastheart" , "Behemoth's Heart" , "Blessed Orb" , "Blight Stones" , "Blood Chalice" , "Bloodborne Maul" , "Bolstering Armband" , "Bottle" , "Bound Eye" , "Broadsword" , "Brutalizer" , "Codex" , "Corrupted Sword" , "Crushing Claws" , "Daemonic Breastplate" , "Dancing Blade" , "Dawnbringer" , "Doom Bringer" , "Dreamcatcher" , "Duck Boots" , "Dust of Revelation" , "Elder Parasite" , "Energizer" , "Firebrand" , "Fleetfeet" , "Flying Courier" , "Fortified Bracer" , "Frostburn" , "Frostwolf's Skull" , "Frozen Light" , "Genjuro" , "Geometer's Bane" , "Ghost Marchers" , "Gloves of the Swift" , "Glowstone" , "Grave Locket" , "Grimoire of Power" , "Guardian Ring" , "Harkon's Blade" , "Health Potion" , "Hellflower" , "Helm of the Black Legion" , "Helm of the Victim" , "Homecoming Stone" , "Hungry Spirit" , "Hypercrown" , "Icebrand" , "Icon of the Goddess" , "Insanitarius" , "Iron Buckler" , "Iron Shield" , "Jade Spire" , "Kuldra's Sheepstick" , "Lex Talionis" , "Lifetube" , "Lightbrand" , "Logger's Hatchet" , "Luminous Prism" , "Madfred's Brass Knuckles" , "Major Totem" , "Mana Potion" , "Manatube" , "Marchers" , "Mark of the Novice" , "Master's Legacy" , "Mighty Blade" , "Minor Totem" , "Mock of Brilliance" , "Mystic Vestments" , "Neophyte's Book" , "Nome's Wisdom" , "Null Stone" , "Nullfire Blade" , "Ophelia's Pact" , "Orb of Zamos" , "Perpetual Cogwheel" , "Pickled Brain" , "Plated Greaves" , "Platemail" , "Portal Key" , "Post Haste" , "Power Supply" , "Pretender's Crown" , "Punchdagger" , "Puzzlebox" , "Quickblade" , "Refreshing Ornament" , "Rejuvenation Potion" , "Restoration Stone" , "Riftshards" , "Ring of Sorcery" , "Ring of the Teacher" , "Ringmail" , "Runed Cleaver" , "Sand Scepter" , "Savage Mace" , "Scarab" , "Searing Light" , "Shaman's Headdress" , "Shield of the Five" , "Shieldbreaker" , "Shrunken Head" , "Slayer" , "Snake Bracelet" , "Sol's Bulwark" , "Sorcery Boots" , "Soulscream Ring" , "Soultrap" , "Spell Sunder" , "Spellshards" , "Spiked Bola" , "Staff of the Master" , "Steamboots" , "Steamstaff" , "Stormspirit" , "Striders" , "Sustainer" , "Sword of the High" , "Symbol of Rage" , "Tablet of Command" , "Thunderclaw" , "Trinket of Restoration" , "Twin Blades" , "Ultor's Heavy Helm" , "Veiled Rot" , "Void Talisman" , "Void Talisman" , "Voltstone" , "Ward of Revelation" , "Ward of Sight" , "Warhammer" , "Warpcleft" , "Whispering Helm" , "Wind Whistle" , "Wingbow", "Tome of Elements", "Ioyn Stone", "Toxin Claws", "Sacrificial Stone", "Token of Life", "Frostfield Plate", "Spyglass", "Golden Apple", "Lunar Tear", "Pegasus Boots"]
subheaderList = [ "Banning Phase", "Picking Phase" , "Single Draft", "Other", "General", "Well", "Bosses", "Champions of Newerth", "Mid Wars", "Team Deathmatch", "Ability", "Consumable Slots", "Forests of Caldavar", "MVP Votes", "Gold Changes", "Towers"]
abilityNameList = ["Decimate" , "Fire Surge", "Armordillo", "Homing Missile", "Fissure", "Shockwave", "Rocket Barrage", "Tar Toss", "Sawblade Showdown", "Guttling Hook", "Magic Brew", "Steam Turret", "Explosive Flare", "Deadeye", "Money Shot", "Piercing Arrows", "Recluse", "Greedgutter", "Thoughtsteal", "Elemental Warp", "Chrysalis", "Volatile Pod", "Nymphora's Zeal", "Grace of the Nymph", "Bubble Pop", "Preservation", "Flight", "Whiplash", "Fireflies", "Rolling Thunder", "Withering Presence", "Summon Booboo", "Reboot", "Rush", "Side Step", "Lunge", "Inhuman Nature", "Jungle Toxin", "Glacial Downpour", "Saint's Blood", "Acid Bomb", "Weapon Enhancement", "Overcharged Shot", "Master's Call", "Stampede", "Might of the Herd", "Void Rip", "Carnage", "Entangle", "Unbreakable", "Cascade Event", "Shared Existence", "Rift Burn", "Crippling Pollen", "Shards of Harkon", "Mana Sunder", "Arcane Vortex", "Retribution", "Sol's Conviction", "Life Leech", "Transfusion", "Tundra Blast", "Chilling Presence", "Essence Link", "Noxious Cloud", "Shell Surf", "Firebomb", "Dragon's Path", "Funeral Pyre", "Sunder's Vault", "Time Leap", "Chronofield", "Storm Cloud", "Taunt", "Whirling Blade", "Conflagrate", "Kindled Fury", "Stalagmites", "Chuck", "Enlarge", "Gore", "Decelerate", "Terror Mounds", "Impalers", "Call of Winter", "Flash of Darkness", "Dark Mana", "Willowmaker", "Ludicrous Speed", "Wish for Revenge", "Boulder Toss", "Slam", "Ancient Skin", "Fury", "Draining Venom", "Enfeeble", "Ember Shard", "Regurgitate", "Corpse Conversion", "Hell on Newerth", "Bombardment", "Crippling Puncture", "Healing Wave", "Magnetic Contraption", "Opposite Charges", "Fiery Barrage", "Cataclysm", "Perch & Plunge", "Berserk", "Ballistic", "HEAT Round", "Mirage Strike", "Edge Counter", "Teleport", "Earthshatter", "Puppeteer's Hold", "Puppet Show", "Wish for Power", "Desert's Curse", "Mirage", "Vanish", "Lance-A-Long", "Heart Piercer", "Booboo", "Fractal Field", "Wall of Mirrors", "Dimensional Link", "Life Tap", "Dark Lord's Presence", "The Undying", "Storm Blades", "Static Shock", "Power Overwhelming", "Death Lotus", "Tree Grapple", "Relentless Salvo", "Vault", "Avenging Leap", "Fervor", "Ricochet", "Far Scry", "Bound by Fate", "Luck of the Draw", "Power Throw", "The Burning Ember", "Chaotic Flames", "Crippling Dart", "Enlightenment", "Doppelganger", "Unholy Expulsion", "Stagger", "Electric Shield", "Hunter's Command", "Overgrowth", "As One", "Reflection", "Call of the Damned", "Infernal Instability", "Fire & Ice", "Corpse Explosion", "Crippling Slugs", "Galvanize", "Demon Strike", "Righteous Strike", "Sol's Blessing", "Conscription", "Master of the Mantra", "Transmute", "Primal Surge", "Debilitate", "Persecution", "Voodoo Puppet", "Compel", "Horned Strike", "Mortification", "Essence Shroud", "Staccato", "Disco Inferno", "Undertow", "In My Element", "Unstable Shard", "Crystallize", "Mousetrap", "Unleash Vorax", "Toxicity", "Judgment", "Cursed Ground", "Summon Hellhounds", "Warcry", "Silver Bullet", "Schism", "Cyclones", "Wind Shield", "Spore Breath", "Ensnaring Shrubbery", "Demonic Execution", "Cold Shoulder", "Unholy Strength", "Shadow Step", "Illusory Assault", "Protective Charm", "Noxious Nightcrawler", "Cleansing Wind", "Prison Break", "Elemental", "Meteor", "Wan Jin Slam", "Earth's Grasp", "Crystal Field", "Force of Balance", "Steel Resolve", "Face Off", "Bat Blast", "Blade Frenzy", "Crippling Volley", "Blood Crazy", "Blood Sense", "Hemorrhage", "Terrorize", "Vampiric Flight", "Consume", "Frigid Field", "Hunter's Command", "Mana Rift", "Heavenly Vault", "Ionic Dash", "Extinguish", "Carnivorous", "Metamorphosis", "Sticky Bomb", "The Keg", "Spider Mines", "Sacred Totems", "Spirit Walk", "Power of the Elders", "Curse of Ages", "Discharge", "Stalk", "Barrel Roll", "Gash", "Ephemeral Forge", "Matraxe", "Flurry", "Invigorate", "Shared Fate", "Battle Experience", "Scavenge", "Poison Spray", "Toxin Wards", "Courageous Leap", "Valkyrie's Prism", "Torrent", "Heartache", "Trample", "Glacial Spike", "Shadow Walk", "Twin Breath", "Twin Fangs", "Fire and Ice", "Waylay", "Guardian Angel", "Group Chuck", "Quickshield", "Reckless Charge", "A Thousand Cuts", "Ancestral Assault", "Asphyxiate", "Whirlbubble", "Dark Swarm", "Terrorform", "Hive Mind", "Flick", "Animate Forest", "Strength in Numbers", "Corpse Toss", "Lava Surge", "Swarm", "Divide & Conquer", "LRM", "Spiked Dart", "Rewind", "Energy Absorption", "Split Fire", "Stasis Smash", "Essence Shift", "Death's Halo", "Comet", "Dimensional Link", "Void Rip", "Lethal Range", "Multi-Strike", "Blinding Dash", "Graceful Strikes", "Spider Sting", "Pilfering", "Wave of Death", "Grave Silence", "Siphon Soul", "Gauntlet Blast", "Flagellation", "Headsmash", "Nature's Wrath", "Ophelia's Judgment", "Shackled", "Swift Slashes", "Echo Strikes", "Flash Freeze", "Evil Presence", "Siphon Soul", "Path of Destruction", "Ashes to Ashes", "Watery Grave", "Perfect Storm", "Nature's Guidance", "Telekinetic Control", "Emerald Lightning", "Emerald Red", "Restless", "Enrage", "Lightning Shackles", "Dream of Madness", "Summon Gawain", "Nether Strike", "Hammer Throw", "Brute Strength", "Summon Malphas", "Moon Finale", "Plague Rider", "Master's Incantation", "Typhoon", "Shard Blast", "Ignite", "Chomp!", "Focus Buffer", "Cleansing Shock", "Summon Malphas", "Mors Certissima", "Command", "Haunt", "Sonar Scream", "Plague Carrier", "Counter Attack", "Essence Projection", "Grapple", "Infest", "Shadow", "Javelin of Light", "Flash", "Weed Field", "Magic Carp", "Venomous Leap", "Terror", "Electric Eye", "Zoomerang", "Lightning Rod", "Chain Reaction", "Impalement", "Mark of Death", "Electric Tide", "Corrupted Conduit", "Lightning Storm", "Webbed Shot", "Static Discharge", "Overload", "3 Point Strike", "Geo Stalk", "Goblin Toss", "Bluster", "Parade of Power", "Disarm", "Gargantuan's Blast", "Feint's Siphon", "Blast Off", "Three's a Crowd", "Overdrive", "Illusive Dash", "Piercing Shards", "Electric Frenzy", "Static Grip", "Silencing Shot", "Rift Stalk", "Morph", "Voodoo Wards", "Soul's Sight", "Call of the Valkyrie", "Miniaturization", "Dig", "Stone Hide", "Shatterstorm", "Fire Shield", "Sear", "Air Strike!", "Take Cover", "Obliterate", "Dreams of Madness", "Rocket Drill", "Lodestone Plates", "Final Chapter", "Mighty Swing", "Sword of the Damned", "Hellbourne Zeal", "Energy Field", "Blazing Strike", "Protective Melody", "Precision", "Special Ammunition", "Flaming Hammer", "Frenzy", "Draconic Defense", "Drink", "Illusory Veil", "Synergy", "Hollowpoint Shells", "Dead Eye", "Icy Imprisonment", "B.A.N.G.", "Mana Combustion", "More Axes", "Dragonfire", "Arcane Hymn", "Summon Vorax", "Bear Form", "Graveyard", "Tsunami Charge", "Lunar Glow", "Mesmerize", "Power Drain"]

copyfile("patch_notes.txt",gamePatchNotes)
copyfile("patch_notes.txt",forumPatchNotes)
copyfile("patch_notes.txt",motdPatchNotes)


# Functions
def formatPatchNotes_InGame(destFile: str) -> None:
    """
    Formats the patch notes for the in-game HoN client

    Attributes:
        destFile: name of the file to write the formatted content to
    """
    with in_place.InPlace(destFile) as file:
        for line in file:
            # Version header
            if line.startswith('Version '):
                line = line.replace('Version ', '^980Version ', 1)
                line = line.rstrip('\n') # These 2 lines of code are required to properly concatenate at the end of the current text line
                line =  line + '^*' + '\n'

            # Date line
            if line.endswith((yearNow) + '\n') or line.endswith((yearNowPlusOne) + '\n'):
                line = '^980' + line
                line = line.rstrip('\n')
                line =  line + '^*' + '\n'

            # Headers
            if line.startswith('=== '):
                line = line.replace('=== ', '===^960 ', 1)
                line = line.replace(' ===', ' ^*===', 1)
            if line.startswith('== '):
                line = line.replace('== ', '==^960 ', 1)
                line = line.replace(' ==', ' ^*==', 1)
            if line.startswith('= '):
                line = line.replace('= ', '=^075 ', 1)
                line = line.replace(' =', ' ^*=', 1)

            # Starting bullet characters for start of line
            if line.startswith('- '):
                line = line.replace('- ', '^947-^* ', 1)
            if line.startswith('*'):
                line = line.replace('*', '   ^274*^* ', 1)
            if line.startswith('+'):
                line = line.replace('+', '^947+^*', 1)

            # Heroes highlighting
            for heroName in heroList:
                if line.startswith(str(heroName)) and (len(str(heroName))+2 >= len(line) or line.endswith('Reworked)\n') ): # Specific exception for hero names in hero abilities; accounts for the hidden \n
                    line = '^059' + line
                    line = line.rstrip('\n')
                    line =  line + '^*' + '\n'
            
            # Items highlighting
            for itemName in itemList:
                if line.startswith(str(itemName)) or line.startswith('New '):
                    line = '^077' + line
                    line = line.rstrip('\n')
                    line =  line + '^*' + '\n'

             # Subheader highlighting
            for subheaderName in subheaderList:
                if line.startswith(str(subheaderName)):
                    line = '^075' + line
                    line = line.rstrip('\n')
                    line =  line + '^*' + '\n'

            # Ability name highlighting
            for abilityName in abilityNameList:
                if line.startswith(str(abilityName)):
                    line = '^256' + line
                    line = line.rstrip('\n')
                    line =  line + '^*' + '\n'

            # Misc. terms
            if line.startswith('New Picking Mode') or line.startswith('Kongor'):
                line = '^539' + line
                line = line.rstrip('\n')
                line =  line + '^*' + '\n'

            file.write(line)
        file.close()

def formatPatchNotes_Forum(destFile: str) -> None:
    """
    Formats the patch notes for the official HoN forums

    Attributes:
        destFile: name of the file to write the formatted content to
    """
    with in_place.InPlace(destFile) as file:
        for line in file:
            # Top header: addition of the "Welcome" statement to patch notes
            if line.startswith('Version '):
                line = '[CENTER][B][COLOR=#ffd700][SIZE=26]Welcome to Heroes of Newerth[/SIZE]' + '\n' + '[SIZE=20]' + line
                line = line.rstrip('\n')

            if ('-------------' in line):
                line = line.replace('-------------', ' - ')
                line = line.rstrip('\n')

            # Date line
            if line.endswith((yearNow) + '\n') or line.endswith((yearNowPlusOne) + '\n'):
                line = line.rstrip('\n')
                line =  line + '[/SIZE][/COLOR][/B][/CENTER]' + '\n'

            # Headers
            if line.startswith('=== '):
                line = line.replace('=== ', '===[COLOR=#ffa500][SIZE=18][B] ', 1)
                line = line.replace(' ===', ' [/B][/SIZE][/COLOR]===', 1)
            if line.startswith('== '):
                line = line.replace('== ', '==[COLOR=#ffa500][SIZE=18][B] ', 1)
                line = line.replace(' ==', ' [/B][/SIZE][/COLOR]==', 1)
            if line.startswith('= '):
                line = line.replace('= ', '=[COLOR=#ffd700] ', 1)
                line = line.replace(' =', ' [/COLOR]=', 1)

            # Starting bullet characters for start of line
            if line.startswith('- '):
                line = line.replace('- ', '[COLOR=#ff66cc]-[/COLOR] ', 1)
            if line.startswith('*'):
                line = line.replace('*', '[COLOR=#00cc99]*[/COLOR] ', 1)
            if line.startswith('+'):
                line = line.replace('+', '[COLOR=#ff66cc]+[/COLOR][I][COLOR=#ffffcc]', 1)
                line = line.rstrip('\n')
                line = line + '[/I][/COLOR]' + '\n'

            # Hero highlighting
            for heroName in heroList:
                if line.startswith(str(heroName)) and (len(str(heroName))+2 >= len(line) or line.endswith('Reworked)\n')): # Specific exception for hero names in hero abilities; accounts for the hidden \n
                    line = '[COLOR=#0099ff][B]' + line
                    line = line.rstrip('\n')
                    line =  line + '[/B][/COLOR]' + '\n'
            
            # Item highlighting
            for itemName in itemList:
                if line.startswith(str(itemName)) or line.startswith('New '):
                    line = '[COLOR=#00cccc][B]' + line
                    line = line.rstrip('\n')
                    line =  line + '[/B][/COLOR]' + '\n'

            # Subheader highlighting
            for subheaderName in subheaderList:
                if line.startswith(str(subheaderName)):
                    line = '[COLOR=#00cc99]' + line
                    line = line.rstrip('\n')
                    line =  line + '[/COLOR]' + '\n'

            # Ability name highlighting
            for abilityName in abilityNameList:
                if line.startswith(str(abilityName)):
                    line = '[COLOR=#0099cc]' + line
                    line = line.rstrip('\n')
                    line =  line + '[/COLOR]' + '\n'

            # Misc. terms
            if line.startswith('New Picking Mode') or line.startswith('Kongor'):
                line = '[COLOR=#ff0066]' + line
                line = line.rstrip('\n')
                line =  line + '[/COLOR]' + '\n'
            
            file.write(line)
        file.close()


def formatPatchNotes_MotD(destFile: str) -> None:
    """
    Formats the patch notes for the Message-of-the-Day (MotD) panel using HTML tag formatting

    Attributes:
        destFile: name of the file to write the formatted content to
    """
    with in_place.InPlace(destFile) as file:
        for line in file:
            # Handle whitespaces at start of line
            if line.startswith('\n'):
                line = '<br />'

            # Top header: addition of the "Welcome" statement to patch notes
            if line.startswith('Version '):
                line = '<p><strong><span style="color: #ffd700; font-size: 18pt;">Welcome to Heroes of Newerth</span></strong></span>' + '<br />' + '<strong><span style="color: #ffd700; font-size: 18pt;">' + line
                line = line.rstrip('\n')

            if ('-------------' in line):
                line = line.replace('-------------', ' - ')
                line = line.rstrip('\n')

            # Date line
            if line.endswith((yearNow) + '\n') or line.endswith((yearNowPlusOne) + '\n'):
                line = line.rstrip('\n')
                line =  line + '</span></strong></p>' + '\n'

            # Headers
            if line.startswith('=== '):
                line = line.replace('=== ', '===<strong><span style="font-size: 14pt; color: #ffa500;"> ', 1)
                line = line.replace(' ===', ' </span></strong>===', 1)
            if line.startswith('== '):
                line = line.replace('== ', '==<strong><span style="font-size: 14pt; color: #ffa500;"> ', 1)
                line = line.replace(' ==', ' </span></strong>==', 1)
            if line.startswith('= '):
                line = line.replace('= ', '=<span style="color: #ffd700";> ', 1)
                line = line.replace(' =', ' </span>=', 1)

            # Starting bullet characters for start of line
            if line.startswith('- '):
                line = line.replace('- ', '<br /><span style="color: #ff66cc;">-</span> ', 1)
            if line.startswith('*'):
                line = line.replace('*', '<br /><span style="color: #00cc99;">*</span> ', 1)
            if line.startswith('+'):
                line = line.replace('+', '<span style="color: #ff66cc;">+</span><em><span style="color: #ffffcc;">', 1)
                line = line.rstrip('\n')
                line = line + '</em></span>' + '<br />'

            # Hero highlighting
            for heroName in heroList:
                if line.startswith(str(heroName)) and (len(str(heroName))+2 >= len(line) or line.endswith('Reworked)\n')): # Specific exception for hero names in hero abilities; accounts for the hidden \n
                    line = '<br /><strong><span style="color: #0099ff";>' + line
                    line = line.rstrip('\n')
                    line =  line + '</span></strong>' + '\n'
            
            # Item highlighting
            for itemName in itemList:
                if line.startswith(str(itemName)) or line.startswith('New '):
                    line = '<br /><strong><span style="color: #00cccc";>' + line
                    line = line.rstrip('\n')
                    line =  line + '</span></strong>' + '\n'

            # Subheader highlighting
            for subheaderName in subheaderList:
                if line.startswith(str(subheaderName)):
                    line = '<br /><span style="color: #00cc99";>' + line
                    line = line.rstrip('\n')
                    line =  line + '</span>' + '\n'

            # Ability name highlighting
            for abilityName in abilityNameList:
                if line.startswith(str(abilityName)):
                    line = '<br /><span style="color: #0099cc";>' + line
                    line = line.rstrip('\n')
                    line =  line + '</span>' + '\n'

            # Misc. terms
            if line.startswith('New Picking Mode') or line.startswith('Kongor'):
                line = '<br /><span style="color: #ff0066";>' + line
                line = line.rstrip('\n')
                line =  line + '</span>' + '\n'
            
            file.write(line)
        file.close()


# Main
formatPatchNotes_InGame(gamePatchNotes)
formatPatchNotes_Forum(forumPatchNotes)
formatPatchNotes_MotD(motdPatchNotes)

print("Patch notes formatting complete! :)")