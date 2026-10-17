import datetime
from collections import defaultdict

data = '''101,AAPL,BUY,10,150.50,2026-09-20
102,MSFT,SELL,5,420,2026-09-21
103,AAPL,BUY,20,151,2026-09-22
104,GOOG,BUY,abc,180,2026-09-22
105,AAPL,SELL,5,152,2026-09-23
106,MSFT,BUY,10,400,2026-09-23
107,GOOG,BUY,10,180,2026-09-24
108,AAPL,BUY,0,155,2026-09-24
109,MSFT,BUY,10,-5,2026-09-24
110, ,BUY,10,100,2026-09-24
111,TSLA,BUY,10,100,2026-02-30'''


class MarketDataProcessor:

    def __init__(self):
        self.symbol_summary_map = defaultdict(lambda: {'quantity': float, buy_value: float})
        self.symbol_buy_value_map = defaultdict(float)
    
    def parse_and_validate(self, line):
        
        line = line.split(',')
        if len(line) != 6:
            return False
        
        trade_id  = line[0].strip()
        symbol    = line[1].strip()
        side      = line[2].strip().upper()
        quantity  = line[3].strip()
        price     = line[4].strip()
        timestamp = line[5].strip()
        
        # Validating trade_id
        try:
            trade_id = int(trade_id)
            if trade_id <= 0:
                return False
        except ValueError:
            return False
        
        # Validating symbol
        if symbol == '':
            return False
        
        # Validating side
        if side not in ['BUY', 'SELL']:
            return False
        
        # Validating quantity
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return False
        except ValueError:
            return False
        
        # Validating price
        try:
            price = float(price)
            if price <= 0:
                return False
        except ValueError:
            return False
        
        # Validating timestamp
        try:
            timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
        except ValueError:
            return False
        
        result = {
           'trade_id' : trade_id,
           'symbol': symbol,
           'side': side,
           'quantity': quantity,
           'price': price,
           'timestamp': timestamp
        }
        return result
    
    
    def add_record(self, line):
        
        row = self.parse_and_validate(line)
        if not row:
            return
        
        if row['side'] == 'BUY':
            symbol = row['symbol']
            quantity = row['quantity']
            price = row['price']
            self.symbol_summary_map[symbol]['quantity'] += quantity
            self.symbol_summary_map[symbol]['buy_value'] += (quantity * price)
            self.symbol_buy_value_map['symbol'] += (quantity * price)
        

    def get_symbol_summary(self):
        return self.symbol_summary_map

    def get_top_symbol(self):
        return sorted(self.symbol_buy_value_map.items(), key = lambda x: (-x[1], x[0]))[0][0]


def process_data(data):
    mdp = MarketDataProcessor()
    data = data.split('\n')
    for line in data:
        mdp.parse_and_validate(line)
    
    print(mdp.get_symbol_summary())
    print(mdp.get_top_symbol())
        
process_data(data)
    