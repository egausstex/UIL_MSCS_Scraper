import csv


class UILResults:
    def __init__(self) -> None:
        self.header = []
        self.rows = []

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
