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
    while True:
        print("Enter games played for each team")
        print("Arsenal, Man City, Newcastle, Tottenham, Man United")
        print("Example: 23,56,78,98,65\n")

        data_str = input("Enter your data here: ")
        
        games_played = data_str.split(",")
        
        if validate_data(games_played):
            print("Your entry is correct")
            break

    return games_played


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
        return False
   
    return True


def update_games_played_worksheet(data):
    """
    Will update the games_played worksheet with any 
    data that is provided by the user
    """
    print("Updating the Games Played spreadsheet\n")
    games_played_worksheet = SHEET.worksheet("games_played")
    games_played_worksheet.append_row(data)
    print("Games Played spreadsheet has been updated correctly!\n")


data = get_games_played()
games_played = [int(num) for num in data]
update_games_played_worksheet(games_played)

