from html.parser import HTMLParser
from uil_scraper import UILScraper
from bs4 import BeautifulSoup
import csv


class UILExtractor:
    """Create a UILExtractor class"""

    def __init__(self, scraper: UILScraper) -> None:
        self.scraper = scraper
        self.data = []

    def extract_individual_results(self):
        """Extract individual contestant results from HTML file"""

        soup = BeautifulSoup(self.scraper.html, "html.parser")
        # Find first table and get all table rows
        for index, tr in enumerate(soup.table.findAll("tr")):
            row = []
            # Find all table data cells
            for td in tr.findAll("td"):
                # Convert object to string and strip whitespace characters
                data_string = str(td.string).strip()
                row.append(data_string)
            if index == 0:
                self.data.append(row + ["Year", "Event"])
            else:
                self.data.append(row + [self.scraper.year, self.scraper.event])

    def write_csv(self, filepath: str) -> None:
        """Write extracted data into a csv file"""

        # Write list of lists to csv file
        with open(filepath, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(self.data)
