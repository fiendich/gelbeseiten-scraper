# Gelbeseiten Scraper

This project is a web scraper designed to collect business information from [Gelbeseiten](https://www.gelbeseiten.de/). It efficiently scrapes business names and addresses based on search queries, handles pagination to retrieve all available results, and saves the data to text files.

## Features

- Scrapes business names and addresses using specified search queries.
- Automatically handles pagination to ensure all available results are retrieved.
- Saves results to text files in the `data/` directory for easy access.

## Installation

To get started with the Gelbeseiten Scraper, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/gelbeseiten-scraper.git
    cd gelbeseiten-scraper
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper and collect business information:

1. Navigate to the project directory.
2. Execute the following command:

    ```bash
    python src/main.py
    ```

This will scrape business information for the specified categories (e.g., `Bergbau`, `Stahl Industrie`, `Verlag Industrie`) and save the results in the `data/` directory.

## Considerations and Theoretical Solutions

During the development of this project, several potential solutions and improvements were considered to enhance its functionality. Some of these solutions were not implemented due to technical limitations, scope, or practicality. Below are the theoretical solutions and the reasons why they were not pursued:

### 1. **Extracting Emails from Business Listings**
   - **Theoretical Solution**: Utilize advanced tools like ChatGPT-4 or similar AI models to search for company emails using only their name and address. The AI could potentially interact with various data sources or search engines to locate these emails.
   - **Challenges**: While AI models like ChatGPT-4 can generate queries and perform web searches, they currently lack the capability to directly interact with external APIs or browse the web autonomously. Additionally, attempts to extract emails using traditional methods, such as regex searches within Google results, encounter limitations. For instance, after making approximately 259 requests, Google may issue a 429 error, indicating too many requests, which halts further scraping. Even when using automation tools like Selenium, these efforts often run into issues such as captchas, which prevent continued operation.

### 2. **Handling Dynamic Content with Selenium**
   - **Theoretical Solution**: Selenium, a web automation tool, could be used to interact with dynamically loaded content that may not be fully captured by simple HTTP requests. This would allow for more comprehensive data scraping, particularly on websites that rely heavily on JavaScript.
   - **Challenges**: While Selenium offers robust capabilities, it introduces significant overhead in terms of setup, execution speed, and resource consumption. Given that the current scope of this project deals primarily with static content, the added complexity of integrating Selenium was deemed unnecessary.

### 3. **Using Microsoft Azure OpenAI and Google Maps Places API**
   - **Theoretical Solution**: The optimal approach could involve leveraging Microsoft Azure's OpenAI services, which include web search capabilities, to find business emails and other details. Additionally, using the Google Maps Places API for text search could potentially replace Gelbeseiten as a data source, offering more comprehensive and up-to-date business information.
   - **Challenges**: While this approach could be highly effective, it introduces potential cost implications, especially if scaled to large datasets. Additionally, the complexity of implementing and managing these APIs would require more advanced development and maintenance efforts.

### 4. **Storing Results in a Database**
   - **Theoretical Solution**: Instead of saving the results in text files, scraped data could be stored in a database such as SQLite or PostgreSQL. This would facilitate more complex queries, data manipulation, and potentially better scalability.
   - **Challenges**: For the current project scope, storing results in simple text files is sufficient. Introducing a database would require additional setup and configuration, adding complexity that is not necessary for the current use case.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
