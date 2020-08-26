"""
This script obtains the date of every HoN patch by extracting the modified date file property from zipped hon.exe files

These zipped hon.exe files are obtained by downloading them from the official HoN CDN

The results get printed to console & also get appended to an output.txt file
"""


from datetime import datetime
from io import BytesIO
import urllib.request
import zipfile, os, sys

# Constants
url_string_prefix = "http://dl.heroesofnewerth.com/wac/i686"
url_string_suffix = "hon.exe.zip"
pathname = os.path.dirname(sys.argv[0])
output_file_name = os.path.abspath(pathname) + "/output.log"

patch_version_base = {
    "major": 0,
    "minor": 1,
    "hotfix": 21
}

def get_modified_date_from_url(url_string):
    """
    Gets a zip file that contains a hon.exe file
    Extracts the modified date of that hon.exe file & returns it
    """
    with urllib.request.urlopen(url_string) as response:
        #TODO: Handle HTTP Error 404 here
        with zipfile.ZipFile(BytesIO(response.read()), 'r') as zip_file:
            for hon_exe_file in zip_file.filelist:
                year = hon_exe_file.date_time[0]
                month = hon_exe_file.date_time[1]
                day = hon_exe_file.date_time[2]
                modified_date = datetime(year, month, day)
                modified_date_string = modified_date.strftime("%Y-%m-%d")
                return modified_date_string

# Open output file to write to
with open(output_file_name, 'a+') as output_file:
    # Reference for reading & overwriting a file: https://stackoverflow.com/a/2424410
    text = output_file.read()
    output_file.seek(0)
    output_file.write(text)
    output_file.truncate()

    while (True):
        # Construct URL string
        patch_string = f'{patch_version_base.get("major")}.{patch_version_base.get("minor")}.{patch_version_base.get("hotfix")}'
        url_string = f'{url_string_prefix}/{patch_string}/{url_string_suffix}'
        modified_date = get_modified_date_from_url(url_string)

        formatted_final_patch_string = f'{patch_string} {modified_date}'
        
        # Print to console & append to file
        print(formatted_final_patch_string)
        output_file.write(formatted_final_patch_string + "\n")

        # Increment counter
        patch_version_base["hotfix"] = patch_version_base.get("hotfix") + 1



