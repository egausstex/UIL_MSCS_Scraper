from uil_scraper import UILScraper
from uil_extractor import UILExtractor


year_start = 2017
year_end = 2019

scraper = UILScraper(2019, "5A", "R", 3, "CAL")
scraper.get_html()

extractor = UILExtractor(scraper)
extractor.extract_individual_results()

# uil_extractor.write_csv("results.csv")
