from uil_results import UILResults

years = [2019]
contest = ["CAL"]
conference = ["5A", "6A"]
meet_level = ["R", "S"]
district_nums = [23]
meet_level_num = {"R": [1, 2, 3, 4], "D": district_nums}

for year in years:
    results = UILResults(contest, conference, meet_level, meet_level_num, year)
    results.agg_data()
    # TODO allow creation of data folder
    filename = "data\\" + str(year) + "UIL_Results.csv"
    results.write_csv(filename)
    print(f"Done scraping {year}!")
