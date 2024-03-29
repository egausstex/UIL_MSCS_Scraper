from uil_results import UILResults

contest = "CAL"
conference = "5A"
meet_level = "R"
meet_div = 3
year_start = 2017
year_end = 2019

results = UILResults(contest, conference, meet_level, meet_div, year_start, year_end)
results.agg_data()
results.print_results()
results.write_csv("results.csv")
