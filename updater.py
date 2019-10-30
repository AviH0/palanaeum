import shutil

import requests
import zipfile
from shutil import copy2
import os



url = "https://github.com/AviH0/LabSupportInterface/archive/master.zip"

file_path = 'update.zip'
r = requests.get(url, stream=True)
with open(file_path, 'wb') as f:
    for chunk in r.iter_content():
        f.write(chunk)

temp_path = ".update_data"
extra_dir_name = "LabSupportInterface-master"

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_path)

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

recursive_overwrite(os.path.join(temp_path, extra_dir_name), ".")
shutil.rmtree(temp_path, ignore_errors=True)
os.remove(file_path)