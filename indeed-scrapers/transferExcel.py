# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:43:45 2024

@author: user
"""

"""
This example scripts is for indeed job data JSON to .xls

"""
import json
import pandas as pd
from bs4 import BeautifulSoup

# Function to clean HTML tags from the text
def clean_html(raw_html):
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext

# Modified json_to_excel function to clean HTML tags in the 'description' field
def json_to_excel(json_file, excel_file):
    # Reading the JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Cleaning HTML tags from 'description' field
    for item in data:
        if 'description' in item:
            item['description'] = clean_html(item['description'])

    # Converting to pandas DataFrame
    df = pd.DataFrame(data)

    # Saving to Excel file
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    json_file = 'path_to_your_json_file.json'  # JSON file path
    excel_file = 'output.xlsx'                # Excel name (under the same path)
    json_to_excel(json_file, excel_file)
