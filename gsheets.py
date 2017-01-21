import gspread
from oauth2client.service_account import ServiceAccountCredentials

# MAGIC VALUES
CHART_DATA_TITLE = "Charts"

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

class googleSheet():
	def __init__(self, key):
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)
		self.gc = gspread.authorize(credentials)
		self.sheet = self.gc.open_by_key(key)

	def update_value(self, cell, value):
		"""
		Params
		------
		cell : String {'age', 'salary', '..'}
		"""


	def get_chart_data(self):
		"""
		Returns
		-------
		data : list of lists 
		"""
		worksheet = self.sheet.worksheet(CHART_DATA_TITLE)
		return worksheet.get_all_values()
		