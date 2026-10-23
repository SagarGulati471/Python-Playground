import requests
import threading
import time
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self):
        self.results = []
        self.current_working_threads = []


    def fetch_all_snp_companies(self, url):
        print('Fetching all S&P 500 companies...')
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print('Error fetching S&P 500 companies:', response.status_code)
            return f"Error occured while fetching the data {response}"

        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='table table-hover table-borderless table-sm').find('tbody')
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            symbol = cells[2].text.strip() if len(cells) > 0 else None
            company_name = cells[1].text.strip() if len(cells) > 1 else None
            # company_name = cells[0].text.strip() if len(cells) > 0 else None
            yield {'symbol': symbol, 'company_name': company_name}


    def fetch_symbol_price(self, symbol):
        print('----------')
        url = f'https://www.slickcharts.com/symbol/{symbol}'
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(response)
            return f"Error occured while fetching the data {response}"

        soup = BeautifulSoup(response.text, 'html.parser')
        row = soup.find('table', class_='table table-sm table-borderless').find('tbody').find('tr')
        if not row:
            return {'symbol': symbol, 'price': None}
        # Fetch the second table data tag which contains the price
        td_tags = row.find_all('td')
        price = td_tags[1].text.strip() if len(td_tags) > 1 else None
        print(f"price = {price}, symbol = {symbol}", end = '\n')
        return  {'symbol': symbol, 'price': price}
        

    def collect_symbol_prices(self):
        start = time.time()
        results = []
        current_working_threads = []
        for company in self.fetch_all_snp_companies('https://www.slickcharts.com/sp500'):
            symbol = company['symbol']
            thread = threading.Thread(target=lambda s: results.append(self.fetch_symbol_price(s)), args=(symbol,))
            current_working_threads.append(thread)
            thread.start()
            
        for thread in current_working_threads:
            thread.join()
        end = time.time()
        print(f"Fetched prices for {len(results)} symbols")
        print(f"Time taken to fetch all symbol prices: {end - start} seconds")
        return results



# Now we will be fetching the price of all the symbols in the S&P 500 concurrently using threads
# What should be args, since it will need to be changed for each symbol? 
# The args parameter should be a tuple containing the symbol for which we want to fetch the price.

wikiworker = WikiWorker()
wikiworker.collect_symbol_prices()