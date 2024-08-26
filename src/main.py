from scraper.scraper import Scraper

def main():
    scraper = Scraper(output_directory="data")
    scraper.get_businesses("Bergbau")
    scraper.get_businesses("Stahl Industrie")
    scraper.get_businesses("Verlag Industrie")

if __name__ == "__main__":
    main()
