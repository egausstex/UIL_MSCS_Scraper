from uil_results import UILResults

contest = ["NUM", "CAL"]
conference = ["5A", "6A"]
meet_level = ["R", "S"]
meet_level_num = {
    "R": [
        2,
        4,
    ],
    "D": 4,
}
years = [2017, 2018]

results = UILResults(contest, conference, meet_level, meet_level_num, years)
results.agg_data()
results.print_results()
results.write_csv("results.csv")
