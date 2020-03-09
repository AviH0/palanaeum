import sys
import os

import requests

from app.src.updates import updater

UPDATER_URL = 'https://github.com/AviH0/LabSupportInterface/releases/download/Latest/Updater_Windows.exe'

UPDATER_FILE = 'Update.exe'


def fetch_updater():
    print("Fetching updater... ", end='')
    r = requests.get(UPDATER_URL, stream=True)
    with open(UPDATER_FILE, 'wb') as f:
        for chunk in r.iter_content(chunk_size=None):
            f.write(chunk)
    print("done.")

if __name__ == '__main__':
    updates_disabled = False
    if len(sys.argv) > 1:
        updates_disabled = sys.argv[1] == "--no-updates"
    if not updates_disabled and updater.check_for_updates():
        fetch_updater()
        os.execv(UPDATER_FILE, ['a'])
    from app.src import GUI
    gui = GUI.Gui()


