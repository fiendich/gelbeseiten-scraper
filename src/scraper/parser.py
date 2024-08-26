from bs4 import BeautifulSoup

class GelbeSeitenParser:

    @staticmethod
    def parse_total_results(html):
        soup = BeautifulSoup(html, "lxml")
        result_headline = soup.find(class_="mod-TrefferlisteInfo__headline")
        if result_headline:
            total_treffer_text = result_headline.text.strip()
            return int(''.join(filter(str.isdigit, total_treffer_text)))
        return 0

    @staticmethod
    def parse_businesses(html):
        soup = BeautifulSoup(html, "lxml")
        businesses = []
        for article in soup.find_all('article', class_='mod mod-Treffer'):
            name_tag = article.find('h2', class_='mod-Treffer__name')
            address_tag = article.find('div', class_='mod-AdresseKompakt__adress-text')

            if name_tag and address_tag:
                name = name_tag.text.strip()
                address = ', '.join(address_tag.stripped_strings).split('(')[0].strip()
                businesses.append((name, address))

        return businesses
