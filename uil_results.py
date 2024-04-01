import csv
from uil_scraper import UILScraper
from uil_extractor import UILExtractor


class UILResults:
    def __init__(
        self,
        contests: str | list,
        conferences: str | list,
        meet_levels: str,
        meet_level_nums: dict,
        years: int | list,
    ) -> None:
        self.contests = contests
        self.conferences = conferences
        self.meet_levels = meet_levels
        self.meet_level_nums = meet_level_nums
        self.years = years
        self.header = []
        self.rows = []

    def agg_data(self):
        self.create_year_range()
        self.create_param_range()

        for year in self.years:
            for conference in self.conferences:
                for contest in self.contests:
                    for meet_level in self.meet_levels:
                        # Check if meet_level is "S"
                        if meet_level == "D":
                            for num in self.meet_level_nums["D"]:
                                print(meet_level, num)
                                self.get_data(
                                    year, conference, contest, meet_level, num
                                )
                        elif meet_level == "R":
                            for num in self.meet_level_nums["R"]:
                                self.get_data(
                                    year, conference, contest, meet_level, num
                                )
                        elif meet_level == "S":
                            num = 1
                            self.get_data(year, conference, contest, meet_level, num)

    def create_year_range(self) -> None:
        """Creates a list with the year(s) to scrape the UIL website."""
        if type(self.years) == int:
            print("You have specified a single year")
            self.years = [self.years]
        elif type(self.years) == list:
            print("You have given a list of years")
        else:
            print("Invalid input.")

    def create_param_range(self) -> None:
        if type(self.conferences) == str:
            self.conferences = [self.conferences]
        if type(self.contests) == str:
            self.contests = [self.contests]
        if type(self.meet_level_nums) == dict:
            for key, value in self.meet_level_nums.items():
                if type(self.meet_level_nums[key]) == int:
                    self.meet_level_nums[key] = [value]
        else:
            print("Invalid input for meet_level_nums.")

    def get_data(
        self,
        year: int,
        conference: str,
        contest: str,
        meet_level: str,
        meet_level_num: str,
    ):
        print(
            f"Scraping {year}, {conference}, {contest}, {meet_level}, {meet_level_num}"
        )
        scraper = UILScraper(year, conference, meet_level, meet_level_num, contest)
        scraper.get_html()
        extractor = UILExtractor(scraper)
        extractor.extract_individual_results(meet_level)
        self.set_header(extractor.data["header"])
        self.add_rows(extractor.data["rows"])

    def set_header(self, header: list):
        if self.header != header:
            print(f"Different headers, overwriting with {header}...")
            self.header = header
        # else:
        #     print("Headers are the same.")

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
