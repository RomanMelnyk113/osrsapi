import logging

logger = logging.getLogger(__name__)


class PriceTrend:
    _money_shorthands = {"k": 1000, "m": 1000000, "b": 1000000000}

    def __init__(self, price, trend, change):
        self.price = self._extract_price(price)
        self.trend = trend
        self.change = self._extract_change(change)

    def _extract_price(self, price):
        if price is None:
            return None

        price = str(price).replace(" ", "").replace(",", "")

        last = price[-1]  # Get the last character
        # check if this price is in shorthand notation. EX. '1.6m'
        if last in PriceTrend._money_shorthands.keys():
            # if it is, convert it to be a floating point num.
            # EX. '1.6m' -> 1000000 * 1.6 -> 1600000.0
            return PriceTrend._money_shorthands[last] * float(price[:-1])

        return float(price)

    def _extract_change(self, change):
        if change is None:
            return None

        try:
            return float(change[:-1].replace(",",""))
        except ValueError as e:
            logger.error(f'PriceTrend._extract_change error: {str(e)}')
            return None

    def __str__(self):
        v = vars(self)
        details = ", ".join([f"{n}={v}" for n, v in v.items() if v is not None])
        return f"PriceTrend({details})"

    def __repr__(self):
        return self.__str__()
