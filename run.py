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


def get_games_lost():
    """
    User to enter how many games a team has lost
    """
    while True:
        print("Enter how many games each team has lost")
        print("Arsenal, Man City, Newcastle, Tottenham, Man United")
        print("Example: 23,56,78,98,65\n")

        data_str = input("Enter your data here: ")
        
        games_lost = data_str.split(",")
        
        if validate_data(games_lost):
            print("Your entry is correct")
            break

    return games_lost


def update_games_lost_worksheet(data):
    """
    Will update the games_lost worksheet with any 
    data that is provided by the user
    """
    print("Updating the Games Lost spreadsheet\n")
    games_lost_worksheet = SHEET.worksheet("games_lost")
    games_lost_worksheet.append_row(data)
    print("Games Lost spreadsheet has been updated correctly!\n")


def get_games_won():
    """
    User to enter how many games a team has won
    """
    while True:
        print("Enter how many games each team has won")
        print("Arsenal, Man City, Newcastle, Tottenham, Man United")
        print("Example: 23,56,78,98,65\n")

        data_str = input("Enter your data here: ")
        
        games_won = data_str.split(",")
        
        if validate_data(games_won):
            print("Your entry is correct")
            break

    return games_won


def update_games_won_worksheet(data):
    """
    Will update the games_won worksheet with any 
    data that is provided by the user
    """
    print("Updating the Games Won spreadsheet\n")
    games_won_worksheet = SHEET.worksheet("games_won")
    games_won_worksheet.append_row(data)
    print("Games Won spreadsheet has been updated correctly!\n")


def calculate_win_percentage(games_played_row):
    """
    Calculate the win percentage of each team
    """
    print("Calculating the win percentage!...\n")
    games_won = SHEET.worksheet("games_won").get_all_values()
    games_won_row = games_won[-1]
    
    win_percentage_data = []
    for games_played, games_won in zip(games_played_row, games_won_row):
        win_percentage = int(games_won) / games_played * 100
        win_percentage_data.append(win_percentage)
    
    return win_percentage_data


def update_win_percentage_worksheet(data):
    """
    Will update the win_percentage worksheet with any 
    data that is provided by the user
    """
    print("Updating the Win Percentage spreadsheet\n")
    win_percentage_worksheet = SHEET.worksheet("win_percentage")
    win_percentage_worksheet.append_row(data)
    print("Win Percentage spreadsheet has been updated correctly!\n")


def master():
    """
    Run all the program functions
    """
    """
    Get games played will update information for how many
    games each team has played.
    """
    data = get_games_played()
    games_played = [int(num) for num in data]
    update_games_played_worksheet(games_played)
    """
    Get games lost will update information for how many
    games each team has lost.
    """
    data = get_games_lost()
    games_lost = [int(num) for num in data]
    update_games_lost_worksheet(games_lost)
    """
    Get games won will update information for how many
    games each team has won.
    """
    data = get_games_won()
    games_won = [int(num) for num in data]
    update_games_won_worksheet(games_won)
    """
    Caulcate the games win percentage
    """
    new_win_data = calculate_win_percentage(games_played)
    print(new_win_data)
    update_win_percentage_worksheet(new_win_data)


print("Welcome to the Premier Leauge data Automation\n")
master()
