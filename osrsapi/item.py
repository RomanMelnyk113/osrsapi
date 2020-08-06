from typing import OrderedDict

from .const import get_icon_url


class Item:
    _items = {}
    _name_to_id = {}

    def __init__(self, id, name, description, is_mem, type, type_icon, price_info, is_rs3=False):
        self.id = id
        self.name = name
        self.description = description
        self.is_mem = is_mem
        self.type = type
        self.type_icon = type_icon
        self.price_info = price_info
        self.version = 'rs3' if is_rs3 else 'osrs'

        # self.icon = const.GE_ICON + str(self.id)
        # self.large_icon = const.GE_LARGE_ICON + str(self.id)
        self.icon = get_icon_url(id=id, is_rs3=is_rs3)
        self.large_icon = get_icon_url(id=id, large=True, is_rs3=is_rs3)

    def price(self):
        return self.price_info.price()

    @property
    def exact_price(self):
        return self.price_info.exact_price()

    def daily_prices(self) -> OrderedDict[int, int]:
        return self.price_info.daily_180_prices
