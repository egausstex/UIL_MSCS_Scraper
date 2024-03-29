import csv
from uil_scraper import UILScraper
from uil_extractor import UILExtractor


class UILResults:
    def __init__(
        self,
        contest: str,
        conference: str,
        meet_level: str,
        meet_div: int,
        year_start: int,
        year_end: int = None,
    ) -> None:
        self.contest = contest
        self.conference = conference
        self.meet_level = meet_level
        self.meet_div = meet_div
        self.year_start = year_start
        self.year_end = year_end
        self.header = []
        self.rows = []

    def agg_data(self):
        if self.year_end:
            for year in range(self.year_start, self.year_end + 1):
                self.get_data(
                    year, self.conference, self.meet_level, self.meet_div, self.contest
                )
        else:
            self.get_data(
                self.year_start,
                self.conference,
                self.meet_level,
                self.meet_div,
                self.contest,
            )

    def get_data(self, year: int, conference, meet_level, meet_div, contest):
        scraper = UILScraper(
            year, self.conference, self.meet_level, self.meet_div, self.contest
        )
        scraper.get_html()
        extractor = UILExtractor(scraper)
        extractor.extract_individual_results()
        self.set_header(extractor.data["header"])
        self.add_rows(extractor.data["rows"])

    def set_header(self, header: list):
        if self.header != header:
            print(f"Different headers, overwriting with {header}...")
            self.header = header
        else:
            print("Headers are the same.")

    def add_rows(self, rows: list):
        self.rows += rows

    def print_results(self):
        print(self.header)
        for index, row in enumerate(self.rows):
            print(index, row, sep=" | ")

    def write_csv(self, filepath: str) -> None:
        """Write extracted data into a csv file"""
        # Write list of lists to csv file
        with open(filepath, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.header)
            csvwriter.writerows(self.rows)
