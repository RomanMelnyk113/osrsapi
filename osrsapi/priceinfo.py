from typing import List

class PriceInfo:
    def __init__(
            self,
            curr_trend: 'PriceTrend',
            trend_today: 'PriceTrend',
            trend_30: 'PriceTrend',
            trend_90: 'PriceTrend',
            trend_180: 'PriceTrend',
            daily_180_prices: List[int]
    ):
        self.curr_trend = curr_trend
        self.trend_today = trend_today
        self.trend_30 = trend_30
        self.trend_90 = trend_90
        self.trend_180 = trend_180
        self.daily_180_prices = daily_180_prices

    def price(self):
        return self.curr_trend.price

    def exact_price(self):
        return self.daily_180_prices[-1]
