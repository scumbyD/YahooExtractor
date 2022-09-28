from Universe.GetUniverse import EquityData as ed
from Extractor.GetData import CallAPI as ca

if __name__ == '__main__':

    tickers = ed(index='dow')

    df_dic = {}  # create dictionary of dataframes to store history in

    for t in tickers.df.Symbol.tolist():  # calling API - not using lambda to pause btwn calls
        #  add pause here to vary call time spacing
        ticker_history = ca(ticker=t).get_history()
        df_dic[t] = ticker_history

    #  Will need to add transformer class

    #  Will need to add loader class


