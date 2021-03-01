import logging
from collections import OrderedDict

import requests

from .const import get_by_id_url, get_graph_by_id_url
from .item import Item
from .pricetrend import PriceTrend
from .priceinfo import PriceInfo

logger = logging.getLogger(__name__)


class GrandExchange:
    @staticmethod
    def item(id, is_rs3=False):
        uri = get_by_id_url(id=id, is_rs3=is_rs3)
        graph_uri = get_graph_by_id_url(id=id, is_rs3=is_rs3)

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

        price_info = PriceInfo(
            curr_trend, trend_today, trend_30, trend_90, trend_180, daily_180_prices=OrderedDict(graph_json_data)
        )

        return Item(id, name, description, is_mem, type, type_icon, price_info, is_rs3=is_rs3)
