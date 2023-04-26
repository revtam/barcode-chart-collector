from kucoin.client import Market

from exchange_interface import Exchange
from secrets_manager import Api_keys


class Kucoin(Exchange):

    def __init__(self):
        self.name = "KUCN"
        self.client = Market(key=Api_keys.kucoin_public,
                             secret=Api_keys.kucoin_private, passphrase=Api_keys.kucoin_passphrase)

    def get_exchange_name(self):
        return self.name

    def get_all_symbols_data(self):
        result_dict = {elem["symbol"]: [elem["symbol"], elem["priceIncrement"]]
                       for elem in self.client.get_symbol_list()}
        for each_ticker in self.client.get_all_tickers()["ticker"]:
            result_dict[each_ticker["symbol"]].append(
                each_ticker["last"])
        return list(result_dict.values())
