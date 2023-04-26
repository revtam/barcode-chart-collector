from abc import ABC, abstractmethod


class Exchange(ABC):

    @abstractmethod
    def get_exchange_name(self):
        pass

    @abstractmethod
    def get_all_symbols_data(self):
        """
            @return [symbol, increment unit, last price] list
            Returns all symbols, their price increment units and their current prices as strings
        """
        pass