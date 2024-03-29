from uil_scraper import UILScraper
from uil_extractor import UILExtractor
from uil_results import UILResults

year_start = 2017
year_end = 2019

results = UILResults()

for year in range(year_start, year_end + 1):
    scraper = UILScraper(year, "5A", "R", 3, "CAL")
    scraper.get_html()
    extractor = UILExtractor(scraper)
    extractor.extract_individual_results()
    results.set_header(extractor.data["header"])
    results.add_rows(extractor.data["rows"])

results.print_results()
results.write_csv("results.csv")
