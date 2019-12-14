import sys

try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import requests
except ImportError:
    print("Please ensure you have the packages: oauth2client, gspread installed before using.\n"
          "you can install them by pasting the following command into your shell:\n"
          "python -m pip install gspread oauth2client")
    exit(1)

# Share spreadsheet with following email address: lab-support@lab-support-intro2cs.iam.gserviceaccount.com
# Then paste the name of the spreadsheet in the following variable:
CREDENTIALS_DIRECTORY = 'app/credentials/Lab Support Intro2CS-273f7439f27c.json'
NAME_OF_SPREADSHEET = "Intro2CS - Lab Support Queue - Edit"


def authenticate(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except gspread.exceptions.APIError:
            args[0].reauth()
            return inner(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            print("Connection error, please check network connection.", file=sys.stderr)
    return inner


class SheetReader:
    FINISHED = '3'
    NO_SHOW = '2'
    ARRIVED = '1'
    DEFAULT = ''

    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        self.scope = ['https://www.googleapis.com/auth/drive']
        try:
            self.creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_DIRECTORY, self.scope)
            self.client = gspread.authorize(self.creds)

            # Find a workbook by name and open the second sheet
            # Make sure you use the right name here.
            self.sheet = self.client.open(NAME_OF_SPREADSHEET).get_worksheet(1)
        except FileNotFoundError:
            print("Please ensure client secret json file is present in credentials directory")
            exit(1)

    def reauth(self):
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(NAME_OF_SPREADSHEET).get_worksheet(1)

    @authenticate
    def get_current_rows(self):
        return self.sheet.get_all_values()[4:]

    @authenticate
    def stu_finished(self, index):
        self.sheet.update_cell(5 + index, 5, self.FINISHED)

    @authenticate
    def stu_no_showed(self, index, time):
        self.sheet.update_cell(5 + index, 5, self.NO_SHOW)
        self.sheet.update_cell(5 + index, 4, time)

    @authenticate
    def reset_stu(self, index):
        self.sheet.update_cell(5 + index, 5, self.DEFAULT)
        self.sheet.update_cell(5 + index, 4, self.DEFAULT)

    @authenticate
    def stu_arrived(self, index):
        self.sheet.update_cell(5 + index, 5, self.ARRIVED)

    @authenticate
    def remove_stu(self, index):
        self.sheet.delete_row(5 + index)
        self.sheet.append_row([])
