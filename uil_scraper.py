import requests


class UILScraper:
    """Create a UILScraper class"""

    def __init__(
        self, year: int, conference: str, meet_level: str, level_num: int, event: str
    ) -> None:
        self.year = year
        self.conference = conference
        self.meet_level = meet_level
        self.level_num = level_num
        self.event = event

    def get_html(self) -> None:
        """Send a request to server and return html page"""
        # Query parameters
        payload = {
            "s_year": str(self.year),
            "s_conference": self.conference,
            "s_level_id": self.meet_level,
            "s_level_nbr": str(self.level_num),
            "s_event_abbr": self.event,
            "s_submit_sw": "X",
        }

        # Requests object
        self.html = requests.get(
            "https://utdirect.utexas.edu/nlogon/uil/vlcp_pub_arch.WBX", params=payload
        ).text

    def write_html(self, filepath: str) -> None:
        """Write the self.html object to an html file."""
        # Write html page into a text file
        with open(filepath, "w") as text_file:
            text_file.write(self.html)
