import requests
import threading
import time
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self, url):
       self.url = url

    def fetch_all_snp_companies(self):
        print('Fetching all S&P 500 companies...\n')
        response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response.status_code != 200:
            print('Error fetching S&P 500 companies:', response.status_code)
            raise Exception(f"Error occured while fetching the data {response}")

        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='table table-hover table-borderless table-sm').find('tbody')
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            symbol = cells[2].text.strip() if len(cells) > 2 else None
            company_name = cells[1].text.strip() if len(cells) > 1 else None
            yield {'symbol': symbol, 'company_name': company_name}

class PriceWorker(threading.Thread):

    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.result = None
        self.error = None
        self.url = f'https://www.slickcharts.com/symbol/{symbol}'


    def run(self):

        try:
            response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            if response.status_code != 200:
                print(f'Error fetching price for {self.symbol}: {response.status_code}')
                self.error = f"Error occured while fetching the data {response}"
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            row = soup.find('table', class_='table table-sm table-borderless').find('tbody').find('tr')
            if not row:
                self.error = f"No row found for {self.symbol}"
                return 
            self.error = None
            # Fetch the second table data tag which contains the price
            td_tags = row.find_all('td')
            price = td_tags[1].text.strip() if len(td_tags) > 1 else None
            self.result = {'symbol': self.symbol, 'price': price}
        except Exception as e:
            self.error = str(e)
            self.result = {'symbol': self.symbol, 'price': None}
            return


URL = 'https://www.slickcharts.com/sp500'
wikiworker = WikiWorker(URL)


# perf counter is better than time.time() for measuring elapsed time because 
# it provides higher resolution and is not affected by system clock updates.
start = time.perf_counter()
current_workers = []
for company in wikiworker.fetch_all_snp_companies():
    print(f'company fetched: {company}')

    price_worker = PriceWorker(company['symbol'])
    price_worker.start()
    current_workers.append(price_worker)

for worker in current_workers:
    worker.join()
    print(f'Price fetched for {worker.symbol}: {worker.result}')
end = time.perf_counter()
print(f"Total time taken to fetch prices for all companies: {end - start} seconds \n")