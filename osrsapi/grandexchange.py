import logging
from collections import OrderedDict
from http import HTTPStatus
from json.decoder import JSONDecodeError

import requests

from .const import get_by_id_url, get_graph_by_id_url
from .item import Item
from .pricetrend import PriceTrend
from .priceinfo import PriceInfo

logger = logging.getLogger(__name__)


class GameItemNotFound(Exception):
    pass


class GameItemParseError(Exception):
    pass


class GrandExchange:
    @staticmethod
    def item(id, is_rs3=False):
        uri = get_by_id_url(id=id, is_rs3=is_rs3)
        graph_uri = get_graph_by_id_url(id=id, is_rs3=is_rs3)
        db_name = "RS3" if is_rs3 else "OSRS"
        try:
            response = requests.get(uri)
            response_graph = requests.get(graph_uri)
        except requests.HTTPError as e:
            logger.error("OSRS API request error: ", str(e))
            raise GameItemNotFound(f"Unable to find item from {db_name} with id {id}.")

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise GameItemNotFound(f"Unable to find item from {db_name} with id {id}.")

        try:
            logger.info("Item response", response.text)
            json_data = response.json()
            item = json_data.get("item")
        except JSONDecodeError as e:
            msg = f"Error during parsing game item object. Item from {db_name} with id {id}."
            details = 'No details'
            if response.text:
                details = response.text
            logger.exception(f"{msg}. Details: {details}", exc_info=True)
            raise GameItemParseError(msg)

        try:
            logger.info("Item response_graph", response_graph.text)
            graph_json_data = response_graph.json()
            daily_data = graph_json_data.get("daily")
        except JSONDecodeError as e:
            msg = f"Error during parsing game item daily info. Item from {db_name} with id {id}."
            details = 'No details'
            if response.text:
                details = response.text
            logger.exception(f"{msg}. Details: {details}", exc_info=True)
            raise GameItemParseError(msg)

        name = item["name"]
        description = item["description"]
        is_mem = bool(item["members"])
        type = item["type"]
        type_icon = item["typeIcon"]

        # price info/trends
        current = item["current"]
        today = item["today"]
        day30 = item["day30"]
        day90 = item["day90"]
        day180 = item["day180"]

        curr_trend = PriceTrend(current["price"], current["trend"], None)
        trend_today = PriceTrend(today["price"], today["trend"], None)
        trend_30 = PriceTrend(None, day30["trend"], day30["change"])
        trend_90 = PriceTrend(None, day90["trend"], day90["change"])
        trend_180 = PriceTrend(None, day180["trend"], day180["change"])

        price_info = PriceInfo(
            curr_trend, trend_today, trend_30, trend_90, trend_180, daily_180_prices=OrderedDict(daily_data)
        )

        return Item(id, name, description, is_mem, type, type_icon, price_info, is_rs3=is_rs3)
