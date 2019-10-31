import shutil
import requests
import zipfile
import os


DEFAULT_URL = "https://github.com/AviH0/LabSupportInterface/archive/master.zip"
UPDATE_FILE = 'update.zip'

TEMP_DIR = ".update_data"
ARCHIVE_ROOT_NAME = "LabSupportInterface-master"


def do_update():
    print("Updating LabSupportClient...\n")
    download_update()
    extract_update()
    copy_update()
    clean_up()
    print("Update successful.")


def download_update():
    print("Fetching update... ", end='')
    r = requests.get(DEFAULT_URL, stream=True)
    with open(UPDATE_FILE, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
    print("done.")


def extract_update():
    print("Extracting... ", end='')
    with zipfile.ZipFile(UPDATE_FILE, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR)
    print("done.")


def copy_update():
    print("Copying... ", end='')
    recursive_overwrite(os.path.join(TEMP_DIR, ARCHIVE_ROOT_NAME), ".")
    print("done.")


def clean_up():
    print("Removing update files... ", end='')
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    os.remove(UPDATE_FILE)
    print("done.")


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        shutil.copyfile(src, dest)


