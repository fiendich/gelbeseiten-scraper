import os
import requests
from .parser import GelbeSeitenParser
from .utils import ensure_output_directory


class Scraper:
    SEARCH_URL = "https://www.gelbeseiten.de/suche/"
    AJAX_SEARCH_URL = "https://www.gelbeseiten.de/ajaxsuche"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

    def __init__(self, output_directory):
        self.output_directory = output_directory
        ensure_output_directory(self.output_directory)

    def _get_total_results(self, what, place):
        search_url = f"{self.SEARCH_URL}{what}/{place}" if place else f"{self.SEARCH_URL}{what}/bundesweit"
        try:
            response = requests.get(search_url, headers={'User-Agent': self.USER_AGENT})
            response.raise_for_status()
            total_treffer = GelbeSeitenParser.parse_total_results(response.text)
            print(f"Total businesses found: {total_treffer}")
            return total_treffer
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the search request: {e}")
            return None

    def get_businesses(self, what, place=None, umkreis=-1):
        total_treffer = self._get_total_results(what, place)
        if not total_treffer:
            return

        headers = {
            'User-Agent': self.USER_AGENT,
            'cookie': 'your-cookie-data-here'
        }

        iterations = (total_treffer + 9) // 10

        output_txt = os.path.join(self.output_directory, f"{what}_{place or 'bundesweit'}.txt")

        with open(output_txt, 'w', encoding='utf-8') as file:
            for position in range(1, iterations * 10 + 1, 10):
                body = {
                    "umkreis": umkreis,
                    "verwandt": False,
                    "WAS": what,
                    "WO": place,
                    "position": position,
                    "anzahl": 10,
                    "sortierung": "relevanz",
                }

                try:
                    response = requests.post(self.AJAX_SEARCH_URL, headers=headers, data=body)
                    response.raise_for_status()

                    html = response.json().get("html")
                    if not html:
                        print(f"No HTML content found at position {position}.")
                        continue

                    businesses = GelbeSeitenParser.parse_businesses(html)
                    for name, address in businesses:
                        file.write(f"{name}, {address}\n")
                        print(f"Processed: {name}, {address}")

                except requests.exceptions.RequestException as e:
                    print(f"An error occurred during iteration at position {position}: {e}")

        print(f"Completed processing for '{what}'.")
