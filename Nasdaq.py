class Nasdaq:

    # financials
    def financials(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/financials"

    # dividend history
    def dividend_history(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/dividend-history"

    # historical quote - not sure if i want to use this or not
    def historical_quote(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/historical"

    # earnings
    def earnings(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/earnings"

    # PE and PEG ratios
    def pe_peg_ratios(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/price-earnings-peg-ratios"

    # short interest - not sure if I will use this
    def short_interest(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/short-interest"

    # institutional holdings
    def institutional_holdings(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/institutional-holdings"

    # insider activity - not sure if I care about this
    def insider_activity(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/insider-activity"

    # revenue earnings per share
    def revenue_eps(self, ticker):
        return "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/revenue-eps"