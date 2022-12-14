import pandas as pd


class EquityData(object):

    def __init__(self, index):

        self.df = self.get_df(index)

    @classmethod
    def get_df(cls, index):  # does this need to be cls??
        #  read in as a dataframe as yfinance calls are returned as dataframes
        df = pd.read_csv(f'Universe/{index}.csv')  # need to update to os join and explain why
        return df
