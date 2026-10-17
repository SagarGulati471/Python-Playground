
def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished...")
        return result

    return wrapper


@log_execution
def process_records(records, source):
    print(f'processing {source}')
    return len(records)



result = process_records([1, 2, 3], source="market_data")
print(f"Result = {result}")



