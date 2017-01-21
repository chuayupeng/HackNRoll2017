import gspread
from oauth2client.service_account import ServiceAccountCredentials

CHART_DATA_TITLE = "Charts"

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
		
