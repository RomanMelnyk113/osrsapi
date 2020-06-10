class PriceInfo:
    def __init__(
        self, curr_trend, trend_today, trend_30, trend_90, trend_180
    ):
        self.curr_trend = curr_trend
        self.trend_today = trend_today
        self.trend_30 = trend_30
        self.trend_90 = trend_90
        self.trend_180 = trend_180

    def price(self):
        return self.curr_trend.price
