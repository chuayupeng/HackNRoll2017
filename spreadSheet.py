import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-a74ef0cc4a6b.json', scope)
spreadsheet_to_open = '12UCWPoJ46pMkE5DGZJiy303xQ1GYUGyHB8R5uf6TuPM'

gc = gspread.authorize(credentials)
full_sheet = gc.open_by_key(spreadsheet_to_open)

inputArea = full_sheet.get_worksheet(0)

#Basic Info
age = inputArea.acell('B2')
salary = inputArea.acell('B3')
currSavings = inputArea.acell('B4')
inputArea.update_acell('B2', 30)

#CPF
OA = inputArea.acell('B6')
SA = inputArea.acell('B7')
MA = inputArea.acell('B8')

#%
