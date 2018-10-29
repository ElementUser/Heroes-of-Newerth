###################################################
# ElementUser's Simple Patch Notes Formatter
# Google Sheet Reference: https://docs.google.com/spreadsheets/d/1f98szyd025VFLrT1yBZG_9lQZiz0eIZ3sbBX49xNX4U/edit#gid=585347818
###################################################

from shutil import copyfile
import in_place
import datetime

# Vars
timeNow = datetime.datetime.now()
yearNow = str(timeNow.year)

gamePatchNotes = 'game_output.txt'
forumPatchNotes = 'forum_output.txt'

heroList = [ "Accursed" , "Adrenaline" , "Aluna" , "Amun-Ra" , "Andromeda" , "Apex" , "Arachna" , "Armadon" , "Artesia" , "Artillery" , "Balphagore" , "Behemoth" , "Berzerker" , "Blacksmith" , "Blitz" , "Blood Hunter" , "Bombardier" , "Bramble" , "Bubbles" , "Bushwack" , "Calamity" , "Chi" , "Chipper" , "Chronos" , "Circe" , "Corrupted Disciple" , "Cthulhuphant" , "Dampeer" , "Dark Lady" , "Deadlift" , "Deadwood" , "Defiler" , "Demented Shaman" , "Devourer" , "Doctor Repulsor" , "Draconis" , "Drunken Master" , "Electrician" , "Ellonia" , "Emerald Warden" , "Empath" , "Engineer" , "Fayde" , "Flint Beastwood" , "Flux" , "Forsaken Archer" , "Gauntlet" , "Gemini" , "Genesis" , "Geomancer" , "Glacius" , "Gladiator" , "Goldenveil" , "Gravekeeper" , "Grinex" , "Gunblade" , "Hammerstorm" , "Hellbringer" , "Ichor" , "Jeraziah" , "Kane" , "Keeper of the Forest" , "Kinesis" , "King Klout" , "Klanx" , "Kraken" , "Legionnaire" , "Lodestone" , "Lord Salforis" , "Madman" , "Magebane" , "Magmus" , "Maliken" , "Martyr" , "Master of Arms" , "Midas" , "Mimix" , "Moira" , "Monarch" , "Monkey King" , "Moon Queen" , "Moraxus" , "Myrmidon" , "Night Hound" , "Nitro" , "Nomad" , "Nymphora" , "Oogie" , "Ophelia" , "Pandamonium" , "Parallax" , "Parasite" , "Pearl" , "Pebbles" , "Pestilence" , "Pharaoh" , "Plague Rider" , "Pollywog Priest" , "Predator" , "Prisoner 945" , "Prophet" , "Puppet Master" , "Pyromancer" , "Rally" , "Rampage" , "Ravenor" , "Revenant" , "Rhapsody" , "Riftwalker" , "Riptide" , "Salomon" , "Sand Wraith" , "Sapphire" , "Scout" , "Shadowblade" , "Shellshock" , "Silhouette" , "Sir Benzington" , "Skrap" , "Slither" , "Solstice" , "Soul Reaper" , "Soulstealer" , "Succubus" , "Swiftblade" , "Tarot" , "Tempest" , "Thunderbringer" , "Torturer" , "Tremble" , "Tundra" , "Valkyrie" , "Vindicator" , "Voodoo Jester" , "War Beast" , "Warchief" , "Wildsoul" , "Witch Slayer" , "Wretched Hag" , "Zephyr"  "Accursed" , "Adrenaline" , "Aluna" , "Amun-Ra" , "Andromeda" , "Apex" , "Arachna" , "Armadon" , "Artesia" , "Artillery" , "Balphagore" , "Behemoth" , "Berzerker" , "Blacksmith" , "Blitz" , "Blood Hunter" , "Bombardier" , "Bramble" , "Bubbles" , "Bushwack" , "Calamity" , "Chi" , "Chipper" , "Chronos" , "Circe" , "Corrupted Disciple" , "Cthulhuphant" , "Dampeer" , "Dark Lady" , "Deadlift" , "Deadwood" , "Defiler" , "Demented Shaman" , "Devourer" , "Doctor Repulsor" , "Draconis" , "Drunken Master" , "Electrician" , "Ellonia" , "Emerald Warden" , "Empath" , "Engineer" , "Fayde" , "Flint Beastwood" , "Flux" , "Forsaken Archer" , "Gauntlet" , "Gemini" , "Genesis" , "Geomancer" , "Glacius" , "Gladiator" , "Goldenveil" , "Gravekeeper" , "Grinex" , "Gunblade" , "Hammerstorm" , "Hellbringer" , "Ichor" , "Jeraziah" , "Kane" , "Keeper of the Forest" , "Kinesis" , "King Klout" , "Klanx" , "Kraken" , "Legionnaire" , "Lodestone" , "Lord Salforis" , "Madman" , "Magebane" , "Magmus" , "Maliken" , "Martyr" , "Master of Arms" , "Midas" , "Mimix" , "Moira" , "Monarch" , "Monkey King" , "Moon Queen" , "Moraxus" , "Myrmidon" , "Night Hound" , "Nitro" , "Nomad" , "Nymphora" , "Oogie" , "Ophelia" , "Pandamonium" , "Parallax" , "Parasite" , "Pearl" , "Pebbles" , "Pestilence" , "Pharaoh" , "Plague Rider" , "Pollywog Priest" , "Predator" , "Prisoner 945" , "Prophet" , "Puppet Master" , "Pyromancer" , "Rally" , "Rampage" , "Ravenor" , "Revenant" , "Rhapsody" , "Riftwalker" , "Riptide" , "Salomon" , "Sand Wraith" , "Sapphire" , "Scout" , "Shadowblade" , "Shellshock" , "Silhouette" , "Sir Benzington" , "Skrap" , "Slither" , "Solstice" , "Soul Reaper" , "Soulstealer" , "Succubus" , "Swiftblade" , "Tarot" , "Tempest" , "Thunderbringer" , "Torturer" , "Tremble" , "Tundra" , "Valkyrie" , "Vindicator" , "Voodoo Jester" , "War Beast" , "Warchief" , "Wildsoul" , "Witch Slayer" , "Wretched Hag" , "Zephyr" ]
itemList = [ "Abyssal Skull" , "Acolyte's Staff" , "Alacrity Band" , "Alchemist's Bones" , "Amulet of Exile" , "Apprentice's Robe" , "Arcana" , "Arcane Bomb" , "Arcane Nullifier", "Armor of the Mad Mage" , "Assassin's Shroud" , "Astrolabe" , "Axe of the Malphai" , "Barbed Armor" , "Barrier Idol" , "Beastheart" , "Behemoth's Heart" , "Blessed Orb" , "Blight Stones" , "Blood Chalice" , "Bloodborne Maul" , "Bolstering Armband" , "Bottle" , "Bound Eye" , "Broadsword" , "Brutalizer" , "Codex" , "Corrupted Sword" , "Crushing Claws" , "Daemonic Breastplate" , "Dancing Blade" , "Dawnbringer" , "Doom Bringer" , "Dreamcatcher" , "Duck Boots" , "Dust of Revelation" , "Elder Parasite" , "Energizer" , "Firebrand" , "Fleetfeet" , "Flying Courier" , "Fortified Bracer" , "Frostburn" , "Frostwolf's Skull" , "Frozen Light" , "Genjuro" , "Geometer's Bane" , "Ghost Marchers" , "Gloves of the Swift" , "Glowstone" , "Grave Locket" , "Grimoire of Power" , "Guardian Ring" , "Harkon's Blade" , "Health Potion" , "Hellflower" , "Helm of the Black Legion" , "Helm of the Victim" , "Homecoming Stone" , "Hungry Spirit" , "Hypercrown" , "Icebrand" , "Icon of the Goddess" , "Insanitarius" , "Iron Buckler" , "Iron Shield" , "Jade Spire" , "Kuldra's Sheepstick" , "Lex Talionis" , "Lifetube" , "Lightbrand" , "Logger's Hatchet" , "Luminous Prism" , "Madfred's Brass Knuckles" , "Major Totem" , "Mana Potion" , "Manatube" , "Marchers" , "Mark of the Novice" , "Master's Legacy" , "Mighty Blade" , "Minor Totem" , "Mock of Brilliance" , "Mystic Vestments" , "Neophyte's Book" , "Nome's Wisdom" , "Null Stone" , "Nullfire Blade" , "Ophelia's Pact" , "Orb of Zamos" , "Perpetual Cogwheel" , "Pickled Brain" , "Plated Greaves" , "Platemail" , "Portal Key" , "Post Haste" , "Power Supply" , "Pretender's Crown" , "Punchdagger" , "Puzzlebox" , "Quickblade" , "Refreshing Ornament" , "Rejuvenation Potion" , "Restoration Stone" , "Riftshards" , "Ring of Sorcery" , "Ring of the Teacher" , "Ringmail" , "Runed Cleaver" , "Sand Scepter" , "Savage Mace" , "Scarab" , "Searing Light" , "Shaman's Headdress" , "Shield of the Five" , "Shieldbreaker" , "Shrunken Head" , "Slayer" , "Snake Bracelet" , "Sol's Bulwark" , "Sorcery Boots" , "Soulscream Ring" , "Soultrap" , "Spell Sunder" , "Spellshards" , "Spiked Bola" , "Staff of the Master" , "Steamboots" , "Steamstaff" , "Stormspirit" , "Striders" , "Sustainer" , "Sword of the High" , "Symbol of Rage" , "Tablet of Command" , "Thunderclaw" , "Trinket of Restoration" , "Twin Blades" , "Ultor's Heavy Helm" , "Veiled Rot" , "Void Talisman" , "Void Talisman" , "Voltstone" , "Ward of Revelation" , "Ward of Sight" , "Warhammer" , "Warpcleft" , "Whispering Helm" , "Wind Whistle" , "Wingbow" ]
subheaderList = [ "Banning Phase", "Picking Phase" , "Single Draft", "Other", "General", "Well", "Bosses", "Champions of Newerth", "Mid Wars", "Team Deathmatch", "Ability", "Consumable Slots", "Forests of Caldavar", "MVP Votes", "Gold Changes"]
abilityNameList = ["Decimate" , "Fire Surge", "Armordillo", "Homing Missile", "Fissure", "Shockwave", "Rocket Barrage", "Tar Toss", "Sawblade Showdown", "Guttling Hook", "Magic Brew", "Steam Turret", "Explosive Flare", "Deadeye", "Money Shot", "Piercing Arrows", "Recluse", "Greedgutter", "Thoughtsteal", "Elemental Warp", "Chrysalis", "Volatile Pod", "Nymphora's Zeal", "Grace of the Nymph", "Bubble Pop", "Preservation", "Flight", "Whiplash", "Fireflies", "Rolling Thunder", "Withering Presence", "Summon Booboo", "Reboot", "Rush", "Side Step", "Lunge", "Inhuman Nature", "Jungle Toxin", "Glacial Downpour", "Saint's Blood", "Acid Bomb", "Weapon Enhancement", "Overcharged Shot", "Master's Call", "Stampede", "Might of the Herd"]

copyfile("patch_notes.txt",gamePatchNotes)
copyfile("patch_notes.txt",forumPatchNotes)

# Defs
def wordInString(word, string_value):
    return True if re.search(r'\b' + word + r'\b', string_value) else False

def formatPatchNotes_InGame(destFile):
    with in_place.InPlace(destFile) as file:
        for line in file:
            # Version header
            if line.startswith('Version '):
                line = line.replace('Version ', '^980Version ', 1)
                line = line.rstrip('\n') # These 2 lines of code are required to properly concatenate at the end of the current text line
                line =  line + '^*' + '\n'

            # Date line
            if line.endswith(yearNow + '\n'):
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
                if line.startswith(str(heroName)) and len(str(heroName))+2 >= len(line): # Specific exception for hero names in hero abilities; accounts for the hidden \n
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

def formatPatchNotes_Forum(destFile):
    with in_place.InPlace(destFile) as file:
        for line in file:
            # Top header: addition of the "Welcome" statement to patch notes
            if line.startswith('Version '):
                line = '[CENTER][B][COLOR=#ffd700][SIZE=5]Welcome to Heroes of Newerth[/SIZE]' + '\n' + '[SIZE=4]' + line
                line = line.rstrip('\n')

            if ('-------------' in line):
                line = line.replace('-------------', ' - ')
                line = line.rstrip('\n')

            # Date line
            if line.endswith(yearNow + '\n'):
                line = line.rstrip('\n')
                line =  line + '[/SIZE][/COLOR][/B][/CENTER]' + '\n'

            # Headers
            if line.startswith('=== '):
                line = line.replace('=== ', '===[COLOR=#ffa500][SIZE=3][B] ', 1)
                line = line.replace(' ===', ' [/B][/SIZE][/COLOR]===', 1)
            if line.startswith('== '):
                line = line.replace('== ', '==[COLOR=#ffa500][SIZE=3][B] ', 1)
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
                if line.startswith(str(heroName)) and len(str(heroName))+2 >= len(line): # Specific exception for hero names in hero abilities; accounts for the hidden \n
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

# Main
formatPatchNotes_InGame(gamePatchNotes)
formatPatchNotes_Forum(forumPatchNotes)

print("Patch notes formatting complete! :)")