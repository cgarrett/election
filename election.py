import urllib.request
import zipfile
import os, errno
import csv

class Election(object):

	def __init__(self):
		"""
		Initialize class
		"""
		self.results_url = 'http://www.ok.gov/elections/support/ok_results_state_csv.zip'
		self.file_name = 'ok_results_state_csv.zip'
		self.data_path = '.'

	def get_file(self):
		"""
		Download election results.
		"""
		try:
			urllib.request.urlretrieve(self.results_url,self.file_name)
			print('Election results retrieved.')
		except:
			pass

	def extract_csv(self):
		"""
		Extract CSV from zip file.
		"""
		try:
			zip_ref = zipfile.ZipFile(self.file_name)
			zip_ref.extractall(self.data_path)
			zip_ref.close()
			print('Election results extracted.')
		except:
			pass

	def delete_zip(self):
		"""
		Remove original zip file.
		"""
		try:
			os.remove(self.file_name)
			print('Zip file deleted.')
		except OSError:
			print('Error deleting {}'.format(self.file_name))

	def display_election_results(self):
		with open('ok_results_state.csv','r') as f_obj:
			reader = csv.DictReader(f_obj, delimiter=',')
			for row in reader:
				print(row['race_description'])
				print(row['cand_name'])

if __name__ == '__main__':
	e = Election()
	# e.get_file()
	# e.extract_csv()
	# e.delete_zip()
	e.display_election_results()