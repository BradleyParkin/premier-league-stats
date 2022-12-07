import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('premier_leauge_stats')


def get_games_by_date():
    """
    User to enter any date in the 2021/2022 football 
    season and pull games played on that date
    """
    print("Enter any date between 13/08/2021 and 22/05/2022")
    print("Data should be in this format 00/00/0000")
    print("Example 13/04/2022\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_games_by_date()
