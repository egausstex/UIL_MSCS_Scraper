from html.parser import HTMLParser
from uil_scraper import UILScraper
from bs4 import BeautifulSoup
import csv


class UILExtractor:
    """Create a UILExtractor class"""

    def __init__(self, scraper: UILScraper) -> None:
        self.scraper = scraper
        self.data = {
            "header": [
                "contestant",
                "school",
                "score",
                "place",
                "points",
                "medal",
                "advance",
                "meet_level",
                "level_num",
                "year",
                "event",
                "conference",
            ],
            "rows": None,
        }

    def extract_individual_results(self, meet_level: str):
        self.data["rows"] = []
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
            if index != 0:
                # Add extra element if results are from state
                if meet_level == "S":
                    row.insert(6, "")
                self.data["rows"].append(
                    row
                    + [
                        self.scraper.meet_level,
                        self.scraper.level_num,
                        self.scraper.year,
                        self.scraper.event,
                        self.scraper.conference,
                    ]
                )

    def write_csv(self, filepath: str) -> None:
        """Write extracted data into a csv file"""

        # Write list of lists to csv file
        with open(filepath, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(self.data)
