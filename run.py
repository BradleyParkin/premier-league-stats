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


def get_games_played():
    """
    User to enter how many games a team has played
    """
    print("Enter games played for each team")
    print("Arsenal, Man City, Newcastle, Tottenham, Man United")
    print("Example: 23,56,78,98,65\n")

    data_str = input("Enter your data here: ")
    
    games_played = data_str.split(",")
    validate_data(games_played)


def validate_data(values):
    """
    Inside the try, this raises a ValueError if the strings
    do not match how many colums there are in the sheet
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f'Exactly 5 enteries are required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invald data: {e} please try again.\n')


get_games_played()
