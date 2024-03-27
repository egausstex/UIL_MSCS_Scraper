import requests

payload = {
    "s_year": "2017",
    "s_conference": "5A",
    "s_level_id": "R",
    "s_level_nbr": "3",
    "s_event_abbr": "CAL",
    "s_submit_sw": "X",
}
r = requests.get(
    "https://utdirect.utexas.edu/nlogon/uil/vlcp_pub_arch.WBX", params=payload
)

# Search request for lines that contain table and save the line numbers.
for line in r.iter_lines(decode_unicode=True):
    if "table" in line:
        print(line)
