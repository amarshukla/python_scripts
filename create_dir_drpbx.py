from xlrd import open_workbook
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

class DropboxFolderCreation:
	"""
	This class is responsible for creating empty directories in  dropbox account.
	"""

	def __init__(self):
		# set your dropbox app key here
		self.app_key = 'jkapc1edmhkgkpl'
		# set your dropbox app secret key here
		self.app_secret = 'gxvndbml6qcypff'
		# set your xls path here such as /home/amar/Desktop/myfile.xlsx
		self.xls_path = '/home/amar/Downloads/landwatch_dropbox.xls'


	def login_dropbox(self):
		"""
		Authorize dropbox using Oauth2
		Follow instructions and authorise your dropbox account to app.
		"""

		APP_KEY = self.app_key
		APP_SECRET = self.app_secret

		auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

		authorize_url = auth_flow.start()
		print ("1. Go to: " + authorize_url)
		print ("2. Click \"Allow\" (you might have to log in first).")
		print ("3. Copy the authorization code.")
		auth_code = input("Enter the authorization code here: ").strip()
		try:
			oauth_result = auth_flow.finish(auth_code)
		except Exception as e:
			print('Error: %s' % (e,))
		return oauth_result


	def read_xls(self):
		"""
		read xls and extract folder names
		"""

		wb = open_workbook(self.xls_path).sheet_by_index(0)
		directory_list = []
		# if xls contains data from row 2 then set start_rowx=1
		# else set it to 0 as below
		# first argument is set to 0 since we want to read column 1 of xls
		xls_data = wb.col_values(0, start_rowx=0)
		return xls_data

	

	def create_dirs_on_dropbox(self):
		"""
		Create empty directories in Dropbox account using API v2
		"""

		dirs = self.read_xls()
		token = self.login_dropbox()
		dbx = dropbox.Dropbox(token.access_token)
		xls_data = self.read_xls()
		if xls_data:
			for dir_name in xls_data:
				try:
					dbx.files_create_folder("/"+dir_name, False)
					print("created "+ dir_name + " on dropbox")
				except Exception as e:
					print("could not create dir with name", dir_name)
		else:
			print("could not read data from xls file")
		print('Successfully created directories in your dropbox account ')

	
dbx_instance = DropboxFolderCreation()
dbx_instance.create_dirs_on_dropbox()
