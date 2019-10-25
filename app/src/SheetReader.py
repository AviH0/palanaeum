try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    print("Please ensure you have the packages: oauth2client, gspread installed before using.\n"
          "you can install them by pasting the following command into your shell:\n"
          "python -m pip install gspread oauth2client")
    exit(1)

# Share spreadsheet with following email address: lab-support@lab-support-intro2cs.iam.gserviceaccount.com
# Then paste the name of the spreadsheet in the following variable:
CREDENTIALS_DIRECTORY = 'app/credentials/Lab Support Intro2CS-273f7439f27c.json'
NAME_OF_SPREADSHEET = "Intro2CS - Lab Support Queue - Edit"


class SheetReader:
    FINISHED = '3'
    NO_SHOW = '2'
    ARRIVED = '1'
    DEFAULT = ''

    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/drive']
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_DIRECTORY,
                                                                     scope)
            client = gspread.authorize(creds)

            # Find a workbook by name and open the first sheet
            # Make sure you use the right name here.
            self.sheet = client.open(NAME_OF_SPREADSHEET).get_worksheet(1)
        except FileNotFoundError:
            print("Please ensure client secret json file is present in credentials directory")

    def get_current_rows(self):
        return self.sheet.get_all_values()[4:]

    def stu_finished(self, index):
        self.sheet.update_cell(5 + index, 5, self.FINISHED)

    def stu_no_showed(self, index, time):
        self.sheet.update_cell(5 + index, 5, self.NO_SHOW)
        self.sheet.update_cell(5 + index, 4, time)

    def reset_stu(self, index):
        self.sheet.update_cell(5 + index, 5, self.DEFAULT)
        self.sheet.update_cell(5 + index, 4, self.DEFAULT)

    def stu_arrived(self, index):
        self.sheet.update_cell(5 + index, 5, self.ARRIVED)

    def remove_stu(self, index):
        self.sheet.delete_row(5 + index)
        self.sheet.append_row([])
