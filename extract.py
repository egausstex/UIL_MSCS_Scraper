from html.parser import HTMLParser
from bs4 import BeautifulSoup
import csv

# Filepath for html file
filepath = "./data.txt"

data = []
# Read file
with open(filepath) as f:
    soup = BeautifulSoup(f, "html.parser")
    # Find first table and get all table rows
    for tr in soup.table.findAll("tr"):
        row = []
        # Find all table data cells
        for td in tr.findAll("td"):
            # Convert objec to string and strip whitespace characters
            data_string = str(td.string).strip()
            row.append(data_string)
        data.append(row)

# Write list of lists to csv file
with open("out.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)
