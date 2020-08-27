"""
This script obtains the date of every HoN patch by extracting the modified date file property from zipped hon.exe files.

These zipped hon.exe files are obtained by downloading them from the official HoN CDN.

HoN's patch versions follow semantic versioning, which consists of 3 numbers ("major", "minor", and "patch"): https://semver.org/. 
Semantic versioning follows a certain pattern, which allows for trial-and-error version checking via version incrementation (since the "patch" number in the version is always monotone increasing & continuous).

Basically, if a patch version does not exist, the "patch" number is set to 0 and the "minor" number is incremented.
If that minor version does not exist, then increment the "major" version and set the "minor" and "patch" number to 0 again.
The script stops running when the iteration's patch version string matches the latest patch version string.

Each HoN patch version string & date of the patch are printed to console & are also appended to an output.log file.
"""

from datetime import datetime
from io import BytesIO
from http.client import HTTPException
from urllib import request
from urllib.error import HTTPError
import zipfile, os, sys

# External imports (pip install required)
import phpserialize

# ===========
# Constants
# ===========
url_string_prefix = "http://dl.heroesofnewerth.com/wac/i686"
url_string_suffix = "hon.exe.zip"
pathname = os.path.dirname(sys.argv[0])
output_file_path = os.path.abspath(pathname) + "/output.log"

# Number of http errors to encounter before incrementing the major version
# Used for tolerance purposes to ensure that versions aren't mistakenly missed
http_error_count_threshold = 3

patch_version_base = {
    "major": 0,
    "minor": 1,
    "patch": 21
}

# ===========
# Functions
# ===========
def get_modified_date_from_url(url_string: str) -> str:
    """
    Gets a zip file that contains a hon.exe file, then extracts the modified date of that hon.exe file

    Attributes:
        url_string: the URL string to make a request to
    """
    try:
        with request.urlopen(url_string) as response:
            with zipfile.ZipFile(BytesIO(response.read()), 'r') as zip_file:
                for hon_exe_file in zip_file.filelist:
                    year = hon_exe_file.date_time[0]
                    month = hon_exe_file.date_time[1]
                    day = hon_exe_file.date_time[2]
                    modified_date = datetime(year, month, day)
                    modified_date_string = modified_date.strftime("%Y-%m-%d")
                    return modified_date_string
    # Raise the error in this function to let the main loop of the script handle the exception
    except HTTPError as exception:
        raise

def get_latest_client_version() -> str:
    """
    Returns a string containing the latest HoN client version

    Reference: https://github.com/djuresic/rctbot-discord/blob/master/rctbot/hon/masterserver.py
    """
    url_string = "http://masterserver.naeu.heroesofnewerth.com/patcher/patcher.php?version=0.0.0.0&os=wac&arch=i686"
    with request.urlopen(url_string) as response:
        content = response.read()
        deserialized_content = phpserialize.loads(content)
        version_string = deserialized_content[0][b'latest_version'].decode()
        return version_string


# ======================
# Main part of script
# ======================
latest_client_version = get_latest_client_version()

# Open output file to write to
with open(output_file_path, 'a+') as output_file:
    # Reference for reading & overwriting a file: https://stackoverflow.com/a/2424410
    text = output_file.read()
    output_file.seek(0)
    output_file.write(text)
    output_file.truncate()

    # Counter to keep track of 404 errors
    http_404_error_count = 0

    while (True):
        # Construct URL string
        patch_string = f'{patch_version_base.get("major")}.{patch_version_base.get("minor")}.{patch_version_base.get("patch")}'
        url_string = f'{url_string_prefix}/{patch_string}/{url_string_suffix}'

        try:
            modified_date = get_modified_date_from_url(url_string)
        except HTTPError:
            http_404_error_count += 1
            # Increment major version & set minor & patch versions to 0
            if (http_404_error_count >= http_error_count_threshold):
                patch_version_base["major"] = patch_version_base.get("major") + 1
                patch_version_base["minor"] = 0
                patch_version_base["patch"] = 0
                
            # Set patch version to 0 & increment minor version, then start the next loop iteration
            else:
                patch_version_base["minor"] = patch_version_base.get("minor") + 1
                patch_version_base["patch"] = 0
            continue

        formatted_final_patch_string = f'{patch_string} {modified_date}'
        
        # Print to console & append to file
        print(formatted_final_patch_string)
        output_file.write(formatted_final_patch_string + "\n")

        # Loop end condition check
        if (latest_client_version == patch_string):
            break

        # Increment counter
        patch_version_base["patch"] = patch_version_base.get("patch") + 1

        # Reset HTTP Error counter
        http_404_error_count = 0



