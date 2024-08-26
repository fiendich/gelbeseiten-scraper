import unittest
from src.scraper.scraper import Scraper
from src.scraper.parser import GelbeSeitenParser

class TestScraper(unittest.TestCase):

    def test_parse_total_results(self):
        html = """<div class="mod-TrefferlisteInfo__headline">Wir haben 200 Treffer für Sie gefunden</div>"""
        result = GelbeSeitenParser.parse_total_results(html)
        self.assertEqual(result, 200)

    def test_parse_businesses(self):
        html = """
        <article class="mod mod-Treffer">
            <h2 class="mod-Treffer__name">Business Name</h2>
            <div class="mod-AdresseKompakt__adress-text">1234 Street, City, ZIP</div>
        </article>
        """
        businesses = GelbeSeitenParser.parse_businesses(html)
        self.assertEqual(businesses, [("Business Name", "1234 Street, City, ZIP")])

if __name__ == '__main__':
    unittest.main()
