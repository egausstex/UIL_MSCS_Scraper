import requests

# Query parameters
payload = {
    "s_year": "2017",
    "s_conference": "5A",
    "s_level_id": "R",
    "s_level_nbr": "3",
    "s_event_abbr": "CAL",
    "s_submit_sw": "X",
}
# Requests object
r = requests.get(
    "https://utdirect.utexas.edu/nlogon/uil/vlcp_pub_arch.WBX", params=payload
)

# Write html page into a text file
with open("data.txt", "w") as text_file:
    text_file.write(r.text)
