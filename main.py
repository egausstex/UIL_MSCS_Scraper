from uil_scraper import UILScraper
from uil_extractor import UILExtractor

uil_scraper = UILScraper(2021, "5A", "R", 3, "CAL")
uil_scraper.get_html()
uil_scraper.write_html("response.html")

uil_extractor = UILExtractor(uil_scraper.results)
uil_extractor.extract_individual_results()
uil_extractor.write_csv("results.csv")
