from uil_results import UILResults

contest = ["NUM", "CAL"]
conference = ["5A", "6A"]
meet_level = ["D", "R", "S"]
district_nums = [i for i in range(1, 6)]
meet_level_num = {
    "R": [2, 3],
    "D": district_nums,
}
years = [2017, 2018]

results = UILResults(contest, conference, meet_level, meet_level_num, years)
results.agg_data()
results.print_results()
results.write_csv("results.csv")
