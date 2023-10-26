"""
fceb --> first course eleventh class base
"""
import os
from openpyxl import load_workbook
import pandas as pd
from datetime import datetime


# Read file
data = "./templates/street_igrimskaya_schedule.xlsx" # idk how replace files
wb = load_workbook(data)


# Get sheet 
sheet = wb['1 курс база 11']
sheet.title


# Get day from table
def get_day_fceb():

    fceb_day_values = ['A5', 'A17', 'A29', 'A41', 'A53', 'A65']
    fceb_day_list = []
    for fdplace in fceb_day_values:
        fceb_day_list.append(sheet[fdplace].value)
    return fceb_day_list


# Get group
def get_groups_fceb():

    fceb_group_values = ['C4', 'E4', 'G4', 'I4', 'K4']
    fceb_group_list = []
    for fgplace in fceb_group_values:
        fceb_group_list.append(sheet[fgplace].value)
    return fceb_group_list


# Get number
def get_number_item_fceb():

    fceb_number_values = ['B5', 'B7', 'B9', 'B11', 'B13', 'B15']
    fceb_number_list = []
    for fnplace in fceb_number_values:
        fceb_number_list.append(sheet[fnplace].value)
    return fceb_number_list


# Get item
def get_item_fceb():
    pass
