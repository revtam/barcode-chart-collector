import re

from kucoin_handler import Kucoin
from okex_handler import Okex

MIN_PRICE_MULTIPL = 15  # Barcode chart that has a price less than MIN_PRICE_MULTIPL * increment + min_price
MARKETS = ["BTC", "USDT", "ETH"]

if __name__ == "__main__":
    exchanges = [Kucoin(), Okex()]
    
    results = []
    for each_exchange in exchanges:
        counter_per_exchange = 0
        for each_market in each_exchange.get_all_symbols_data():
            increment = float(each_market[1])
            last_price = float(each_market[2])
            symbol = each_market[0]
            if last_price < MIN_PRICE_MULTIPL * increment and re.match(f".*-({'|'.join(MARKETS)})", symbol):
                digested_symbol = re.search("(.*)-(.*)", symbol)
                symbol = f"{each_exchange.get_exchange_name()}: {digested_symbol.group(1)}/{digested_symbol.group(2)}"
                results.append(symbol)
                counter_per_exchange += 1
        print(f"{each_exchange.get_exchange_name()}: {counter_per_exchange} found")

    print("Combined results:\n" + ", ".join(results))

    input()
    
