records = [
    {"symbol": "AAPL", "price": 220},
    {"symbol": "GOOG", "price": 180},
    {"symbol": "AAPL", "price": 221},
    {"symbol": "MSFT", "price": 500},
    {"symbol": "AAPL", "price": 219},
]

def filter_symbol(records, symbol):
    for record in records:
        if record["symbol"] == symbol:
            yield record