===========================================
Patch Notes Formatter for HoN
===========================================

- Requires Python 3.x. The program can be ran via the host computer's OS terminal by typing in "python patchNotesFormatter.py".

- Running patchNotesFormatter.py requires a patch_notes.txt file. Doing so will output some files: forum_output.txt, game_output.txt, and motd_output.txt 
- These files contain the patch notes formatted specifically for the forum patch notes, in-game patch notes, and the Message-of-the-Day (MotD) patch notes
- The specific forum format the script formats for is the one used by the HoN forums: https://forums.heroesofnewerth.com/index.php
- Additional strings in the subheaders & ability name lists may need to be defined, since those are not obtained dynamically through an external source.
