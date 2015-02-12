#!/usr/bin/env python3

import sys
import os
import subprocess
import datetime
from urllib.request import urlopen

API_URL = "http://www.sublimetext.com/docs/3/api_reference.html"
TIDY_URL = "http://www.paehl.com/open_source/?download=tidy.zip"

tidy_args = ["-utf8", "--indent", 'auto', "--newline", 'LF']


def download_tidy():
    print("Downloading tidy.exe")
    try:
        res = urlopen(TIDY_URL)
        import zipfile
        with zipfile.ZipFile(res) as z:
            z.extract("tidy.exe")
    except Exception as e:
        print("Unable to download (%s)" % e)
        return 0
    return 1


def get_current_utc_timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")


def main():
    if not sys.platform == "win32":
        print("Currently only verified to work on Windows.")
        return 1
    html_source = urlopen(API_URL).read().decode()

    # Download tidy application
    if not os.path.exists("tidy.exe") and not download_tidy():
        print("\ntidy.exe is required to tidy the html source.")
        print("Please download and extract it manually from here:")
        print("http://www.paehl.com/open_source/?HTML_Tidy_for_Windows")
        return 2

    htmlpath = "api.html"
    p = subprocess.Popen(["tidy"] + tidy_args, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)

    stdout, stderr = p.communicate(html_source)
    if stderr:
        print("The following errors/warnings were emitted by tidy.exe:")
        print(stderr)
    if p.returncode > 1:
        print("The program existed with return code", p.returncode)
        return

    with open(htmlpath, 'w') as f:
        f.write("<!-- Downloaded at %s -->\n" % get_current_utc_timestamp())
        f.write(stdout)
    print("Tidied HTML written to", htmlpath)

if __name__ == '__main__':
    main()
