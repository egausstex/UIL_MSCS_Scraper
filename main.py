from uil_results import UILResults

contest = "CAL"
conference = "5A"
meet_level = "R"
meet_div = 3
years = [2017, 2019]

results = UILResults(contest, conference, meet_level, meet_div, years)
results.agg_data()
results.print_results()
results.write_csv("results.csv")
