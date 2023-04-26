

from exchange_interface import Exchange
import okex.spot_api as spot
from secrets_manager import Api_keys


class Okex(Exchange):

    def __init__(self):
        self.name = "OKEX"
        self.client = spot.SpotAPI(
            Api_keys.okex_public, Api_keys.okex_private, Api_keys.okex_passphrase, False)

    def get_exchange_name(self):
        return self.name

    def get_all_symbols_data(self):
        result_dict = {elem["instrument_id"]: [elem["instrument_id"],
                                               elem["tick_size"]] for elem in self.client.get_coin_info()}
        for each_ticker in self.client.get_ticker():
            result_dict[each_ticker["instrument_id"]].append(
                each_ticker["last"])
        return list(result_dict.values())
