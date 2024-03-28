from html.parser import HTMLParser
from bs4 import BeautifulSoup
import csv


class UILExtractor:
    """Create a UILExtractor class"""

    def __init__(self, UILScraper) -> None:
        self.raw_data = UILScraper
        self.data = []

    def extract_individual_results(self):
        """Extract individual contestant results from HTML file"""

        soup = BeautifulSoup(self.raw_data, "html.parser")
        # Find first table and get all table rows
        for tr in soup.table.findAll("tr"):
            row = []
            # Find all table data cells
            for td in tr.findAll("td"):
                # Convert object to string and strip whitespace characters
                data_string = str(td.string).strip()
                row.append(data_string)
            self.data.append(row)

    def write_csv(self, filepath: str) -> None:
        """Write extracted data into a csv file"""

        # Write list of lists to csv file
        with open(filepath, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(self.data)
