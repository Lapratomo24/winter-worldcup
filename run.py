import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random

from strings import opening_title, closing_remark
from strings import cyan_colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('winter_world_cup')

venues = SHEET.worksheet('venues')
groups = SHEET.worksheet('groups')
fixture_a = SHEET.worksheet('fixture_a')
fixture_b = SHEET.worksheet('fixture_b')
fixture_c = SHEET.worksheet('fixture_c')
fixture_d = SHEET.worksheet('fixture_d')
fixture_e = SHEET.worksheet('fixture_e')
fixture_f = SHEET.worksheet('fixture_f')
fixture_g = SHEET.worksheet('fixture_g')
fixture_h = SHEET.worksheet('fixture_h')

opening_title()
print(cyan_colored("Winter World Cup Is Coming".center(80)))