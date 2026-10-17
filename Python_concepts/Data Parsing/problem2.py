from collections import defaultdict

data = [
    {"trade_id": 101, "customer": "Alice", "symbol": "AAPL", "side": "BUY",  "quantity": 10, "price": 150.0},
    {"trade_id": 102, "customer": "Bob",   "symbol": "MSFT", "side": "BUY",  "quantity": 5,  "price": 400.0},
    {"trade_id": 103, "customer": "Alice", "symbol": "AAPL", "side": "SELL", "quantity": 4,  "price": 155.0},
    {"trade_id": 104, "customer": "Charlie","symbol": "GOOG","side": "BUY",  "quantity": 20, "price": 180.0},
    {"trade_id": 105, "customer": "Bob",   "symbol": "MSFT", "side": "SELL", "quantity": 2,  "price": 410.0},
    {"trade_id": 106, "customer": "Alice", "symbol": "MSFT", "side": "BUY",  "quantity": 8,  "price": 395.0},
    {"trade_id": 107, "customer": "Charlie","symbol": "AAPL", "side": "BUY",  "quantity": 15, "price": 152.0},
]


class TradeAnalytics:

    def __init__(self, trades):
        self.customer_total_buy_value_map = defaultdict(int)
        self.symbols_quantity_map = defaultdict(int)
        
    def process_record(self, row):
        quantity = row['quantity']
        if row['side'] == 'BUY':
            buy_price = row['price']
            self.customer_total_buy_value_map[row['customer']] +=  (quantity * buy_price)
        self.symbols_quantity_map[row['symbol']] += quantity
         
    def get_customer_buy_value(self):
        for customer, buy_value in self.customer_total_buy_value_map.items():
            print(f'cusomer {customer} has total_buy value of {buy_value}')

    def get_top_customer(self):
        return sorted(self.customer_total_buy_value_map.items(),key=lambda x: (-x[1], x[0]))[0]

    def get_symbol_quantity(self):
        for symbol, total_quantity in self.symbols_quantity_map.items():
            print(f'Symbol {symbol} has total quantity of {total_quantity}')
    

def process_data(data):
    ta = TradeAnalytics(data)
    for row in data:
        ta.process_record(row)
    
    ta.get_customer_buy_value()
    print(ta.get_top_customer())
    ta.get_symbol_quantity()
    
process_data(data)