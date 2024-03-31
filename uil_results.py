import csv
from uil_scraper import UILScraper
from uil_extractor import UILExtractor


class UILResults:
    def __init__(
        self,
        contests: str | list,
        conferences: str | list,
        meet_level: str,
        meet_div: int,
        years: int | list,
    ) -> None:
        self.contests = contests
        self.conferences = conferences
        self.meet_level = meet_level
        self.meet_div = meet_div
        self.years = years
        self.header = []
        self.rows = []
        self.year_range = None

    def agg_data(self):
        self.create_year_range()
        self.create_param_range()

        for year in self.year_range:
            for conference in self.conferences:
                for contest in self.contests:
                    self.get_data(year, conference, contest)

    def create_year_range(self) -> None:
        """Creates a list with the year(s) to scrape the UIL website."""
        if type(self.years) == int:
            print("You have specified a single year")
            self.year_range = [self.years]
        elif type(self.years) == list and len(self.years) == 2:
            print(
                f"You have specified a range of years {self.years[0]} to {self.years[1]}"
            )
            self.year_range = list(range(self.years[0], self.years[1] + 1))
        else:
            print("Invalid input.")
        print(self.year_range)

    def create_param_range(self) -> None:
        if type(self.conferences) == str:
            self.conferences = [self.conferences]
        if type(self.contests) == str:
            self.contests = [self.contests]

    def get_data(self, year: int, conference: str, contest: str):
        print(
            f"Scraping {year}, {conference}, {contest}, {self.meet_level}, {self.meet_div}"
        )
        scraper = UILScraper(year, conference, self.meet_level, self.meet_div, contest)
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
