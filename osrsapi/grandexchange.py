import logging

import requests

from . import const
from .item import Item
from .pricetrend import PriceTrend
from .priceinfo import PriceInfo

logger = logging.getLogger(__name__)

class GrandExchange:
    @staticmethod
    def item(id):
        uri = const.GE_BY_ID + str(id)
        graph_uri = const.GE_GRAPH_BY_ID + str(id) + const.JSON_SUFFIX

        try:
            response = requests.get(uri)
            response_graph = requests.get(graph_uri)
        except requests.HTTPError as e:
            logger.error("OSRS API request error: ", str(e))
            raise Exception("Unable to find item with id %d." % id)

        json_data = response.json()["item"]
        graph_json_data = response_graph.json()["daily"]

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

        graph_data_list = list(graph_json_data.values())

        price_info = PriceInfo(
            curr_trend, trend_today, trend_30, trend_90, trend_180, daily_180_prices=graph_data_list
        )


        return Item(id, name, description, is_mem, type, type_icon, price_info)
