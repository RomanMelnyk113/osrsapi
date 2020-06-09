import requests

from . import const
from .item import Item
from .pricetrend import PriceTrend
from .priceinfo import PriceInfo


class GrandExchange(object):
    @staticmethod
    def item(id):
        uri = const.GE_BY_ID + str(id)

        try:
            response = requests.get(uri)
        except requests.HTTPError:
            raise Exception("Unable to find item with id %d." % id)

        json_data = response.json()["item"]

        name = json_data["name"]
        description = json_data["description"]
        is_mem = bool(json_data["members"])
        type = json_data["type"]
        type_icon = json_data["typeIcon"]

        # price info/trends
        current = json_data["current"]
        today = json_data["today"]
        day30 = json_data["day30"]
        day90 = json_data["day90"]
        day180 = json_data["day180"]

        curr_trend = PriceTrend(current["price"], current["trend"], None)
        trend_today = PriceTrend(today["price"], today["trend"], None)
        trend_30 = PriceTrend(None, day30["trend"], day30["change"])
        trend_90 = PriceTrend(None, day90["trend"], day90["change"])
        trend_180 = PriceTrend(None, day180["trend"], day180["change"])

        price_info = PriceInfo(
            curr_trend, trend_today, trend_30, trend_90, trend_180
        )

        return Item(id, name, description, is_mem, type, type_icon, price_info)
