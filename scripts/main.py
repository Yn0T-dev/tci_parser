from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook
import pandas as pd
import requests
from xls2xlsx import XLS2XLSX
import os


# URL_TEMPLATES && FILE_NAME
URL_TEMPLATE = "http://tci72.ru/students/schedule/"
FILE_NAME = "./templates/temp.xlsx"


# Parse from url to xlsx
def parse(url = URL_TEMPLATE):
	result_list = {'link' : []}
	response = requests.get(url)
	print(response)


	# Getting response
	response = requests.get(URL_TEMPLATE)
	soup = bs(response.text, "html.parser")
	list_temp = soup.find_all('li', class_='file-download')


	# Creating DataFrame
	for temp in list_temp:
		result_list['link'].append('http://tci72.ru'+temp.a['href'])
	return result_list


# Export dataframe to excel 
df = pd.DataFrame(data=parse())
df.to_excel(FILE_NAME)


# Read file
data = './templates/temp.xlsx'
wb = load_workbook(data)


# Get sheet
sheet = wb['Sheet1']
sheet.title


# Vars for data from .xlsx table
link_street_energetikov_changes = sheet['B2'].value # Энергетиков изменения
link_street_energetikov_shedule = sheet['B3'].value # Энергетиков расписание
link_street_igrimskaya_changes = sheet['B4'].value # Игримская изменения
link_street_igrimskaya_schedule = sheet['B5'].value # Игримская расписание
link_vilage_yarkovo_changes = sheet['B6'].value # Ярково изменения
link_vilage_yarkovo_schedule = sheet['B7'].value # Ярково расписание


# Downloading files from Sheet1 (temp.xlsx)
def downloading():
	print('\nBeggining files download with requests')

	# Energetikov changes
	r_e_c = requests.get(link_street_energetikov_changes)
	with open ('./templates/street_energetikov_changes.pdf', 'wb') as f:  # --> coming soon
		f.write(r_e_c.content)

	# Energetikov schedule
	r_e_s = requests.get(link_street_energetikov_shedule)
	with open ('./templates/street_energetikov_schedule.pdf', 'wb') as f: # --> coming soon
		f.write(r_e_s.content)

	# Igrimskaya changes
	r_i_c = requests.get(link_street_igrimskaya_changes)
	with open ('./templates/street_igrimskaya_changes.docx', 'wb') as f: # --> coming soon
		f.write(r_i_c.content)

	# Igrimskaya schedule
	r_i_s = requests.get(link_street_igrimskaya_schedule)
	with open ('./templates/street_igrimskaya_schedule.xls', 'wb') as f:
		f.write(r_i_s.content)

	# Yarkovo changes
	r_v_c = requests.get(link_vilage_yarkovo_changes)
	with open ('./templates/vilage_yarkovo_changes.docx', 'wb') as f: # --> coming soon
		f.write(r_v_c.content)

	# Yarkovo schedule
	r_v_s = requests.get(link_vilage_yarkovo_schedule)
	with open ('./templates/vilage_yarkovo_schedule.xlsx', 'wb') as f: # --> coming soon
		f.write(r_v_s.content)

	# Message from downloading
	print('Downloading is end!\n')


# Saving files in main folder
downloading()


# Old file 
old_datafile_igr_sch = './templates/street_igrimskaya_schedule.xls'


# Converte .xls to .xlsx file
def converte_i():
	print('Beggining files to converte')
	x2x = XLS2XLSX('./templates/street_igrimskaya_schedule.xls')
	x2x.to_xlsx('./templates/street_igrimskaya_schedule.xlsx')
	os.system('rm ./templates/street_igrimskaya_schedule.xls || del street_igrimskaya_schedule.xls')
	print('Converte is end!')


# Converte file
converte_i()
