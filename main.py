from uil_results import UILResults

years = [i for i in range(2005, 2023)]
contest = ["NUM", "CAL", "MTH", "CSC"]
conference = ["1A", "2A", "3A", "4A", "5A"]
meet_level = ["D", "R", "S"]
district_nums = [i for i in range(1, 35)]
meet_level_num = {"R": [1, 2, 3, 4], "D": district_nums}

for year in years:
    results = UILResults(contest, conference, meet_level, meet_level_num, year)
    results.agg_data()
    # results.print_results()
    filename = ".\data\\" + str(year) + "_UIL_Results.csv"
    results.write_csv(filename)
    print(f"Done scraping {year}!")
