import gspread
from oauth2client.service_account import ServiceAccountCredentials

# MAGIC VALUES
CHART_DATA_TITLE = "Charts"

# Basics
AGE_CELL = "B2"
SALARY_CELL = "B3"
SAVINGS_CELL = "B4"
PERCENT_SAVED_PER_MONTH = "B13"

# Advanced
PERCENT_INCREASE_SALARY = "B11"
PERCENT_SAVINGS_INTEREST = "B15"
PERCENT_REDUCED_EXP = "B16"
INFLATION_RATE = "B18"
DESIRED_RETIREMENT_AGE = "B19"

# CPF
O_ACC = "B6"
S_ACC = "B7"
M_ACC = "B8"
R_ACC = "B9"

# Major Loans

LOANS_M_REPAY = "D2"
LOANS_M_LEFT = "D3"

H_PRICE = "D6"
H_BUY_AGE = "D7"
H_PERCENT_LOAN = "D8"
H_LOAN_YEARS = "D9"
H_INTEREST_RATE = "D10"

class googleSheet():
	def __init__(self, key):
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)
		self.gc = gspread.authorize(credentials)
		self.sheet = self.gc.open_by_key(key)
		self.inputArea = self.sheet.get_worksheet(0)

	def update_cell(self, cell, value):
		"""
		Params
		------
		cell : String {'B2', 'B3', ..}
		value : Integer { 1, 500, 2000, .. }
		"""
		self.inputArea.update_acell(cell, value)
		
	def get_chart_data(self):
		"""
		Returns
		-------
		data : list of lists 
		"""
		worksheet = self.sheet.worksheet(CHART_DATA_TITLE)
		return worksheet.get_all_values()
		
