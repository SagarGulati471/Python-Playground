import datetime
from collections import defaultdict

data = '''101,AAPL,BUY,10,150.50,2026-09-24 10:30:00
102,MSFT,SELL,5,420.00,2026-09-24 10:31:00
103,AAPL,BUY,20,151.00,2026-09-24 10:35:00
104,GOOG,BUY,abc,180.00,2026-09-24 10:40:00
105,AAPL,SELL,5,152.00,2026-09-24 10:45:00'''


class TradeAnalyzer:

    def __init__(self):
        self.total_buy_value = 0
        self.symbol_summary = defaultdict(int)

    
    def add_trade(self, line):
        row = self.is_valid(line)
        if not row:
            return
        
        if row['side'] == 'BUY':
            self.total_buy_value += (row['quantity'] *  row['price'])
        self.symbol_summary[row['symbol']] += row['quantity']
        

    def is_valid(self, line):
        line = line.split(',')
        
        if len(line) != 6:
            return False
        trade_id  = line[0].strip()
        symbol    = line[1].strip()
        side      = line[2].strip()
        quantity  = line[3].strip()
        price     = line[4].strip()
        timestamp = line[5].strip()
        
        
        # Validating trade_id
        try:
            trade_id = int(trade_id)
            if trade_id < 0:
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
            if quantity < 0:
                return False
        except ValueError:
            return False
        
        # Validating price
        try:
            price = float(price)
            if price < 0:
                return False
        except ValueError:
            return False
        # Validating timestamp
        
        try:
            timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError as v:
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
    
        
    def get_total_buy_value(self):
        return self.total_buy_value


    def get_symbol_summary(self):
        return self.symbol_summary
        

def process_trades(data):
    ta = TradeAnalyzer()
    
    data = data.split('\n')
    for row in data:
        # print(row)
        ta.add_trade(row)
    
    print(ta.get_total_buy_value())
    print(ta.get_symbol_summary())
    
    # Just for my testing, was trying to see if we can access the elements in defaultdict just like we access them in normal dict
    dict_ = ta.get_symbol_summary()
    print(dict_.keys())
    print(dict_.values())
    print(dict_['AAPL'])
process_trades(data)